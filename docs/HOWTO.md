# AS400 / IBM i UI automation — HOWTO

Green-screen (TN5250 / TN3270) automation options for this repo.

**Primary for IBM Host On-Demand (`.hod`) GUI:** the stdlib package [`as400_hod`](as400_hod/) (section 0 below) — **no pip packages**.

Other options use packages from `requirements.txt` (s3270-based, Robot, MCP) or external Java/native tools.

## Shared prerequisites

1. **Python 3.10+** (setup verified on 3.12)
2. For **`.hod` GUI automation**: a running IBM Host On-Demand session window (Windows)
3. For **protocol / s3270 stacks**: **`s3270` / `wc3270`** from [x3270](http://x3270.bgp.nu/)  
   - Windows example path: `C:\wc3270\`
4. Network reachability to the IBM i host (TN5250 often port **23**, TLS often **992**) when not using a pre-opened HOD session

```powershell
# Optional: third-party stacks only (not needed for as400_hod)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

| Option | Needs pip? | Role |
|--------|------------|------|
| **`as400_hod` (stdlib)** | No | Selenium-like control of a live HOD `.hod` window |
| `p5250` + `p3270` | Yes | Headless 5250 via s3270 |
| `py3270` | Yes | Low-level x3270/s3270 |
| `robotframework` + Mainframe3270 | Yes | Keyword suites |
| `ibmi-mcp` | Yes | MCP server for AI agents |
| tn5250j / 5250ng / ACS | Outside venv | Alternate emulators / macros |

---

## 0. as400_hod — stdlib Host On-Demand driver (recommended for `.hod`)

Package: [`as400_hod/`](as400_hod/). **Python standard library only** (`ctypes` for Win32 / UI Automation). No entries in `requirements.txt`.

**Detailed how-to and usage samples:** [docs/USAGE.md](docs/USAGE.md)

Attaches to an **already open** IBM Host On-Demand window, drives it in the **background** (PostMessage — does not steal focus from other apps), and supports Selenium-like click / type / get-text / wait.

### Features

| Goal | API |
|------|-----|
| Attach | `HodDriver.attach(title_contains=".hod")` |
| Click cell | `driver.click(row=6, col=53)` |
| Type / AID keys | `driver.send_keys("USER", Keys.TAB, Keys.ENTER)` |
| Screen text | `driver.get_screen_text()` (UIA, then clipboard fallback) |
| Find by text | `driver.find_element(By.TEXT, "Sign On")` |
| Find by cell | `driver.find_element(By.ROW_COL, (5, 10))` |
| Wait / verify | `driver.wait_until_text_contains("Main Menu", timeout=20)` |
| Window closed | raises **`HodWindowClosedError`** and stops further steps |

### Quick start

```powershell
# Open your .hod session in Host On-Demand first, then:
python examples/attach_and_read.py --title ".hod"
python -m unittest tests.test_as400_hod -v
```

```python
from as400_hod import HodDriver, By, Keys, HodWindowClosedError

driver = HodDriver.attach(
    title_contains=".hod",
    cell_size=(9, 16),   # calibrate to HOD font
    origin=(0, 0),       # client offset to top-left of terminal grid
)

try:
    driver.click(row=6, col=53)
    driver.send_keys("MYUSER")
    driver.send_keys(Keys.TAB)
    driver.send_keys("MYPASS")
    driver.send_keys(Keys.ENTER)
    driver.wait_until_text_contains("Main Menu", timeout=20)
    print(driver.get_screen_text())
except HodWindowClosedError:
    # .hod window was closed — stop the script
    raise
finally:
    driver.quit()  # detaches only; does not close HOD
```

### Text strategies

- **`auto`** (default): UI Automation tree under the HOD HWND; if empty, Ctrl+A / Ctrl+C clipboard fallback
- **`uia`**: UIA only (best when Java Access Bridge exposes the terminal)
- **`clipboard`**: hotkey copy only (shares the system clipboard briefly; does not move focus)

### Limitations

- Java AWT may ignore posted mouse/key messages on some HOD builds; quality is build-dependent. Default policy never steals focus.
- UIA text quality depends on Java Access Bridge / accessibility exposure.
- Clipboard fallback can race with the user’s paste buffer.
- Calibrate `cell_size` and `origin` once per HOD font/window size for accurate row/col clicks.
- Automates the **existing GUI session**, not a headless TN5250 connection (see p5250 below for that).

---

## 1. p5250 (headless AS/400 via s3270)

[GitHub](https://github.com/simonfaltum/p5250) · [PyPI](https://pypi.org/project/p5250/)

Selenium-style Python client for IBM i. Uses `s3270` + `p3270`, with 5250-oriented keys (F1–F24, roll, etc.).

```python
from p5250 import P5250Client

client = P5250Client(
    hostName="your-as400.example.com",
    hostPort="23",
    path=r"C:\wc3270\\",   # omit if s3270 is on PATH
    codePage="cp037",
)

if not client.connect():
    raise SystemExit("Connection failed")

try:
    client.printScreen()
    client.sendText("MYUSER")
    client.sendTab()
    client.sendText("MYPASS")
    client.sendEnter()
    title = client.readTextAtPosition(1, 2, 20)
    client.sendF(3)
finally:
    client.disconnect()
    client.endSession()
```

### Constructor

```python
P5250Client(
    luName=None,
    hostName="localhost",
    hostPort="23",
    modelName="3279-2",
    verifyCert="yes",
    enableTLS="no",
    codePage="cp037",
    path=None,
    timeoutInSec=20,
)
```

### API cheat sheet

| Goal | Method |
|------|--------|
| Connect / disconnect | `connect()`, `disconnect()`, `endSession()` |
| Type / Tab / Enter | `sendText()`, `sendTab()`, `sendEnter()` |
| Function keys | `sendF(n)` (`1`–`24`) |
| Cursor | `moveTo(row, col)`, `moveToFirstInputField()` |
| Read | `readTextAtPosition()`, `readTextArea()`, `getScreen()` |
| Wait / verify write | `waitForField()`, `trySendTextToField()` |
| Page | `rollUp()`, `rollDown()` |
| Capture | `saveScreen()`, `printScreen()` |

Coordinates are screen **row / col** (typically 24×80).

```powershell
python -c "from p5250 import P5250Client; c=P5250Client(hostName='YOUR_HOST', path=r'C:\wc3270\\'); print(c.connect()); c.printScreen(); c.endSession()"
```

---

## 2. p3270

[GitHub (fork)](https://github.com/simonfaltum/p3270) · dependency of `p5250`

Same family as p5250 (`P3270Client`), aimed at classic **3270** hosts. Prefer **p5250** for AS/400 unless you are talking to a 3270 mainframe.

```python
from p3270 import P3270Client

client = P3270Client(hostName="mainframe.example.com", path=r"C:\wc3270\\")
client.connect()
client.sendText("LOGON")
client.sendEnter()
client.disconnect()
client.endSession()
```

API mirrors p5250 for most send/read/move helpers.

---

## 3. py3270

[PyPI](https://pypi.org/project/py3270/)

Thin Python API over `x3270` / `s3270` / `wc3270`. Good for custom drivers; **3270-oriented** (not a full 5250 stack).

```python
from py3270 import Emulator

# visible=True uses GUI (wc3270/x3270); False uses s3270 headless
em = Emulator(visible=False, timeout=30)
em.connect("mainframe.example.com:23")
em.wait_for_field()
em.send_string("MYUSER")
em.send_enter()
print(em.string_get(1, 1, 40))
em.terminate()
```

Useful methods: `connect`, `send_string`, `send_enter`, `send_pf(n)`, `move_to`, `string_get`, `wait_for_field`, `save_screen`, `terminate`.

---

## 4. Robot Framework + Mainframe3270

[PyPI](https://pypi.org/project/robotframework-mainframe3270/) · [docs](https://github.com/MarketSquare/Robot-Framework-Mainframe-3270-Library)

Keyword-driven tests on top of x3270/s3270. Mature for **3270**; usable against hosts that accept 3270-style sessions. For pure IBM i 5250 flows, prefer p5250 or tn5250j.

```robotframework
*** Settings ***
Library    Mainframe3270

*** Test Cases ***
Sign On Smoke
    Open Connection    your-host.example.com
    Wait Field Detected
    Write Bare    MYUSER
    Send Enter
    Page Should Contain String    Welcome
    Take Screenshot
    Close Connection
```

```powershell
.\.venv\Scripts\Activate.ps1
robot path\to\suite.robot
```

Common keywords: `Open Connection`, `Close Connection`, `Write` / `Write Bare`, `Send Enter`, `Send PF`, `Read`, `Page Should Contain String`, `Wait Field Detected`, `Take Screenshot`.

Put `wc3270` / `s3270` on `PATH` (Windows default often `C:\Program Files\wc3270`).

---

## 5. ibmi-mcp

[GitHub](https://github.com/WhitehornLtd/ibmi-mcp) · [PyPI](https://pypi.org/project/ibmi-mcp/)

MCP server that exposes TN5250 tools to AI agents (Claude, Cursor, etc.). Native 5250 session — no s3270 required for this package.

**Note:** This project pins `mcp>=1.0.0,<2` because `ibmi-mcp` still imports `FastMCP`.

### Env config

| Variable | Required | Default | Meaning |
|----------|----------|---------|---------|
| `IBMI_HOST` | yes | — | Hostname / IP |
| `IBMI_PORT` | no | `23` | TN5250 port |
| `IBMI_SSL` | no | `false` | TLS |
| `IBMI_USER` / `IBMI_PASSWORD` | no | — | Auto-signon |
| `IBMI_CODEPAGE` | no | `cp037` | EBCDIC |
| `IBMI_SSH_TUNNEL` | no | `false` | Tunnel via SSH |
| `IBMI_SSH_*` | no | — | SSH key / known_hosts / port |

### Run from this venv

```powershell
$env:IBMI_HOST = "your-as400.example.com"
$env:IBMI_USER = "MYUSER"
$env:IBMI_PASSWORD = "MYPASS"
.\.venv\Scripts\ibmi-mcp.exe
```

### MCP tools

| Tool | Purpose |
|------|---------|
| `connect` / `disconnect` | Session lifecycle |
| `read_screen` | Screen text + input field metadata |
| `send_keys` | Type into current field |
| `send_key` | Enter, F1–F24, Tab, PageUp/Down, … |
| `set_cursor` | Move to row/col |
| `upload_file` / `download_file` | IFS via SFTP |

Register with an MCP client pointing the command at `.venv\Scripts\ibmi-mcp.exe` and pass the env vars above.

---

## 6. tn5250j (outside venv — Java)

[Site](https://tn5250j.github.io/) · [GitHub](https://github.com/tn5250j/tn5250j)

Open-source **true 5250** emulator. Automate via:

- Recorded **macros** (`macros` file with mnemonics like `[enter]`, `[pf3]`)
- Embed the JAR and drive the session API from Java / TestNG
- Jython scripts against the running emulator

```text
# Example macro line (concept)
macro1.LOGIN=MYUSER[tab]MYPASS[enter]
```

Install a JDK, download the tn5250j release JAR, and launch the GUI or embed it in a Java test project. See community write-ups on adapting tn5250j for TestNG/Allure-style UI automation.

---

## 7. 5250ng (outside venv — native)

[5250ng.com](https://5250ng.com/)

Modern Qt/C++ TN5250 client with:

- Full RFC 1205 5250 protocol + TLS
- **5250Script** (expect-style scripting over screens/fields/keys)
- Embedded **MCP** server for agent control

Build from source (CMake 3.16+, C++17, Qt 6.5+) or use release binaries when available. Prefer this when you want a dedicated 5250 product with scripting + MCP rather than Python+s3270.

---

## 8. IBM Access Client Solutions (outside venv — vendor)

IBM’s official client. Use **macros / recorded scripts** inside ACS for light automation and demos. Less ideal for CI than p5250 / tn5250j / MCP, but zero extra stack if ACS is already mandated.

---

## Which to use?

| Goal | Pick |
|------|------|
| Automate an open IBM HOD `.hod` window (stdlib, Selenium-like) | **`as400_hod`** |
| Headless Python scripts against AS/400 like Selenium | **p5250** |
| Robot keyword suites (3270-style) | **Mainframe3270** |
| Custom low-level x3270 control | **py3270** |
| AI / Cursor / Claude driving green screen | **ibmi-mcp** (or 5250ng MCP) |
| Java CI + authentic 5250 | **tn5250j** |
| Expect-style 5250 scripts + modern UI | **5250ng** |
| Quick record inside corporate ACS | **IBM ACS macros** |

---

## Security

Do not commit credentials. Prefer env vars or a gitignored `.env`:

`AS400_HOST`, `AS400_USER`, `AS400_PASSWORD`, or the `IBMI_*` names for ibmi-mcp.

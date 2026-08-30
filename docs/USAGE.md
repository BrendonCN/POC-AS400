# as400_hod — Detailed usage guide

Selenium-style automation for an **already open** IBM Host On-Demand (`.hod`) window.

- **Language:** Python 3.10+ on Windows  
- **Dependencies:** none (stdlib + `ctypes` only)  
- **Overview / alternatives:** see [HOWTO.md](../HOWTO.md)

---

## 1. Prerequisites

1. Install Python 3.10+ (no `pip install` needed for this package).
2. Open your Host On-Demand session so a window whose title includes `.hod` (or your session name) is visible.
3. From the repo root, ensure Python can import the package:

```powershell
cd C:\Users\lette\Documents\GitHub\POC-AS400
python -c "from as400_hod import HodDriver; print('ok')"
```

If you run scripts from another folder, add the repo root to `PYTHONPATH` or keep `sys.path` insertion as in `examples/attach_and_read.py`.

### Optional: better screen text via UI Automation

Enable **Java Access Bridge** for the JRE that runs HOD so `get_screen_text()` can read the accessibility tree. If UIA returns empty text, the driver falls back to clipboard copy (Ctrl+A / Ctrl+C) when `text_strategy="auto"`.

---

## 2. Quick start

```powershell
# Dump screen from whatever .hod window is open
python examples/attach_and_read.py --title ".hod"
```

```python
from as400_hod import HodDriver, By, Keys, HodWindowClosedError

driver = HodDriver.attach(title_contains=".hod")

try:
    print(driver.get_screen_text())
    driver.send_keys(Keys.ENTER)
except HodWindowClosedError:
    print("HOD window was closed — stopping.")
finally:
    driver.quit()  # detaches only; does not close HOD
```

---

## 3. Attaching to a window

`HodDriver.attach(...)` finds a top-level window and binds the driver to its HWND.

| Argument | Meaning |
|----------|---------|
| `title_contains` | Substring match on window title (common: `".hod"`) |
| `title_equals` | Exact title match |
| `title_regex` | Regex string or compiled pattern |
| `hwnd` | Use an explicit HWND (skips search) |
| `process_name_contains` | Filter by process image path (e.g. `"java"`) |
| `cell_size` | `(width_px, height_px)` of one terminal character cell |
| `origin` | `(x, y)` client offset of the top-left cell |
| `text_strategy` | `"auto"` \| `"uia"` \| `"clipboard"` |
| `key_pause` | Delay between posted keys (seconds) |
| `focus_policy` | `"background"` only (default); `"steal"` is not implemented |

```python
# By title substring
driver = HodDriver.attach(title_contains="mysession.hod")

# Exact title
driver = HodDriver.attach(title_equals="IBM Host On-Demand - mysession.hod")

# Regex
driver = HodDriver.attach(title_regex=r".*\.hod$")

# Known HWND (e.g. from Spy++ / your own EnumWindows)
driver = HodDriver.attach(hwnd=12345678)

# Prefer a java.exe HOD process
driver = HodDriver.attach(
    title_contains=".hod",
    process_name_contains="java",
)
```

If nothing matches, `HodAutomationError` is raised.

`driver.hwnd` exposes the bound handle. `driver.quit()` marks the driver closed so further calls raise `HodWindowClosedError` (it does **not** kill HOD).

---

## 4. Coordinates: row / col vs pixels

Terminal positions are **1-based** (row 1 = top, col 1 = left), same idea as classic 24×80 screens.

```text
Client area of HOD window
┌─────────────────────────────────────┐
│ origin (origin_x, origin_y)         │
│   ┌───┬───┬───┐                     │
│   │1,1│1,2│ … │  each cell is       │
│   ├───┼───┼───┤  cell_size wide/tall│
│   │2,1│2,2│ … │                     │
│   └───┴───┴───┘                     │
└─────────────────────────────────────┘
```

```python
driver = HodDriver.attach(
    title_contains=".hod",
    cell_size=(9, 16),   # calibrate to your HOD font
    origin=(0, 0),       # nudge if the grid is inset by toolbars/borders
)

# Click the center of cell (row=6, col=53)
driver.click(row=6, col=53)

# Or click raw client pixels
driver.click(x=120, y=80)
```

**Calibrating `cell_size`:** click a known field with `click(x=..., y=...)` or measure one character in the HOD client area, then set `cell_width` / `cell_height` so `row_col_to_client` lands on the right cells.

---

## 5. Typing and keys (`send_keys`)

Works like Selenium: mix plain strings and `Keys.*` tokens.

```python
from as400_hod import Keys

driver.send_keys("MYUSER")
driver.send_keys(Keys.TAB)
driver.send_keys("secret")
driver.send_keys(Keys.ENTER)

# One call
driver.send_keys("MYUSER", Keys.TAB, "secret", Keys.ENTER)

# Function keys (F1–F24)
driver.send_keys(Keys.F3)   # often Exit
driver.send_keys(Keys.F12)  # Cancel
driver.send_keys(Keys.PAGE_DOWN)
```

### Available `Keys`

| Category | Tokens |
|----------|--------|
| Editing | `ENTER`, `TAB`, `BACKSPACE`, `DELETE`, `ESCAPE` |
| Nav | `HOME`, `END`, `PAGE_UP`, `PAGE_DOWN`, `ARROW_*` |
| AID | `F1` … `F24` |
| Modifiers | `CONTROL`, `SHIFT`, `ALT` (posted as key taps; chords use internal helpers for clipboard) |

Input is sent with **Win32 `PostMessage`** to the HOD HWND so other apps keep focus. Some Java AWT builds ignore posted messages; if clicks/keys do nothing, that is a HOD/JVM limitation, not a missing `pip` package.

---

## 6. Reading and verifying text

### Full screen

```python
screen = driver.get_screen_text()
print(screen)

if "Sign On" in screen:
    print("On sign-on panel")
```

### Slice at row/col

```python
# Read 10 characters starting at row 1, col 2
title = driver.get_text_at(1, 2, 10)
```

### Text strategy

```python
# Default: UIA, then clipboard if empty
HodDriver.attach(title_contains=".hod", text_strategy="auto")

# UIA only
HodDriver.attach(title_contains=".hod", text_strategy="uia")

# Clipboard only (Ctrl+A / Ctrl+C). Does not steal focus, but uses the system clipboard briefly.
HodDriver.attach(title_contains=".hod", text_strategy="clipboard")
```

### Waits (assertion-style)

```python
from as400_hod import HodTimeoutError

try:
    driver.wait_until_text_contains("Main Menu", timeout=20, poll=0.5)
    driver.wait_until_text_gone("Please wait", timeout=30)
except HodTimeoutError as e:
    print("Condition not met:", e)
```

If the `.hod` window closes during a wait, you get `HodWindowClosedError` instead (automation should stop).

---

## 7. Finding elements (Selenium-like)

### By visible text

```python
from as400_hod import By, ElementNotFoundError

el = driver.find_element(By.TEXT, "Sign On")
print(el.text, el.location)  # location → (row, col)
el.click()

# All matches
for el in driver.find_elements(By.TEXT, "Option"):
    print(el)
```

### By row/col

```python
field = driver.find_element(By.ROW_COL, (6, 53))
field.click()
field.send_keys("MYUSER", Keys.TAB)
```

`HodElement` methods:

| Method / property | Behavior |
|-------------------|----------|
| `.text` | Cached match text, or re-read from screen |
| `.location` | `(row, col)` |
| `.click()` | Click that cell |
| `.send_keys(...)` | Click then type |

```python
try:
    driver.find_element(By.TEXT, "Does Not Exist")
except ElementNotFoundError:
    print("Not on this screen")
```

---

## 8. Window closed → stop

Every public action checks `IsWindow(hwnd)`. If the session window is gone:

```python
from as400_hod import HodWindowClosedError

try:
    driver.send_keys(Keys.ENTER)
    driver.get_screen_text()
except HodWindowClosedError:
    # Message: "HOD window is closed; automation stopped"
    raise SystemExit(2)
```

Pattern for multi-step scripts:

```python
def step(name, fn):
    try:
        fn()
    except HodWindowClosedError:
        print(f"Stopped at step: {name}")
        raise

step("login", lambda: driver.send_keys("USER", Keys.TAB, "PASS", Keys.ENTER))
step("wait menu", lambda: driver.wait_until_text_contains("Main Menu"))
```

---

## 9. End-to-end samples

### Sample A — Sign-on smoke (credentials from env)

```python
import os
from as400_hod import HodDriver, Keys, HodWindowClosedError, HodTimeoutError

USER = os.environ["AS400_USER"]
PASSWORD = os.environ["AS400_PASSWORD"]

driver = HodDriver.attach(
    title_contains=".hod",
    cell_size=(9, 16),
    text_strategy="auto",
)

try:
    # Adjust row/col to your Sign On layout
    driver.click(row=6, col=53)
    driver.send_keys(USER, Keys.TAB, PASSWORD, Keys.ENTER)
    driver.wait_until_text_contains("Main Menu", timeout=30)
    print("Login OK")
    print(driver.get_screen_text())
except HodWindowClosedError:
    print("HOD closed — abort")
except HodTimeoutError:
    print("Did not reach Main Menu")
    print(driver.get_screen_text())
finally:
    driver.quit()
```

### Sample B — Find label, type into nearby field

```python
from as400_hod import HodDriver, By, Keys

driver = HodDriver.attach(title_contains=".hod")

label = driver.find_element(By.TEXT, "User")
# Click a few columns to the right of the label (layout-dependent)
driver.click(row=label.row, col=label.col + 20)
driver.send_keys("MYUSER", Keys.TAB)
```

### Sample C — Navigate with F-keys and verify

```python
from as400_hod import HodDriver, Keys

driver = HodDriver.attach(title_contains=".hod")

driver.send_keys(Keys.F3)  # exit current screen
driver.wait_until_text_gone("Working...", timeout=10)
driver.send_keys("1", Keys.ENTER)
assert "Option 1" in driver.get_screen_text()
```

### Sample D — Safe loop until window dies

```python
import time
from as400_hod import HodDriver, HodWindowClosedError

driver = HodDriver.attach(title_contains=".hod")

try:
    while True:
        print("---")
        print(driver.get_screen_text()[:200])
        time.sleep(2)
except HodWindowClosedError:
    print("Session ended")
finally:
    driver.quit()
```

### Sample E — CLI demo shipped in the repo

```powershell
python examples/attach_and_read.py --title ".hod"
python examples/attach_and_read.py --hwnd 12345678 --strategy clipboard
python examples/attach_and_read.py --cell-w 10 --cell-h 18 --origin-y 40
```

---

## 10. Exceptions reference

| Exception | When |
|-----------|------|
| `HodWindowClosedError` | HWND invalid / window closed / after `quit()` |
| `ElementNotFoundError` | `find_element` had no match |
| `HodTimeoutError` | `wait_until_*` timed out |
| `HodAutomationError` | Base / attach failed / unsupported focus policy |

```python
from as400_hod import (
    HodDriver,
    By,
    Keys,
    HodElement,
    HodAutomationError,
    HodWindowClosedError,
    ElementNotFoundError,
    HodTimeoutError,
)
```

---

## 11. Troubleshooting

| Symptom | What to try |
|---------|-------------|
| `No matching HOD window found` | Confirm the session is open; check title in Taskbar; try `title_contains` with part of the real title; pass `hwnd=` |
| Clicks miss the field | Recalibrate `cell_size` and `origin`; try `click(x=..., y=...)` once to probe |
| Keys/clicks do nothing | HOD Java may ignore `PostMessage`; confirm the HWND is the terminal window, not a splash/parent |
| Empty `get_screen_text()` | Enable Java Access Bridge; or `text_strategy="clipboard"`; ensure HOD supports Select All / Copy |
| Clipboard steals paste content | Brief race is expected with clipboard strategy; prefer UIA when possible |
| Script continues after close | It should not — catch `HodWindowClosedError` and exit |

---

## 12. Tests

No HOD window required:

```powershell
python -m unittest tests.test_as400_hod -v
```

---

## 13. What this is / is not

**Is:** GUI automation of a live Host On-Demand `.hod` window, Selenium-shaped API, background-friendly input, hard stop on closed window.

**Is not:** A headless TN5250 client (use `p5250` / s3270 from [HOWTO.md](../HOWTO.md) for that), and not a focus-stealing `SendInput` bot.

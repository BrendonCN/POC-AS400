# Selenium — Getting Through reCAPTCHA

Reference notes on reCAPTCHA handling with Selenium web automation.

> **Note:** This repo’s `as400_hod` package uses a **Selenium-like** API for IBM Host On-Demand (`.hod`) windows — not browser Selenium. This document covers **browser** Selenium + reCAPTCHA only.

---

## Short answer

You **cannot reliably pass real reCAPTCHA with Selenium alone**. reCAPTCHA is designed to block bots. For **your own app in test**, use official test keys or disable CAPTCHA. For other cases, the common approach is to inject a token from a solving service — but that only makes sense when you **own/control the site** or have explicit permission.

---

## 1. Best option for testing: Google test keys

If you control the app, use Google’s always-pass test keys:

| Key | Value |
|-----|--------|
| Site key | `6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXJiZCy` |
| Secret key | `6LeIxAcTAAAAAGG-vFI1TnRWxMZF7JWDYe_g7mUI` |

Any “solve” attempt always succeeds. No Selenium tricks needed.

Also common in dev/staging:

- Turn CAPTCHA off behind an env flag
- Whitelist test IPs / users

---

## 2. reCAPTCHA v2 (checkbox) — what Selenium can do

You can **click the checkbox**, but if Google shows an image challenge, Selenium won’t solve it reliably.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for reCAPTCHA iframe
iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='recaptcha/api2/anchor']"))
)
driver.switch_to.frame(iframe)

# Click "I'm not a robot"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
).click()

driver.switch_to.default_content()
```

Often this still fails because Google detects automation (WebDriver flag, behavior, IP, etc.).

---

## 3. Token injection (common in test automation)

reCAPTCHA puts a token in a hidden field: `g-recaptcha-response`. After you have a valid token (from test keys, your backend, or a licensed solving service), inject it:

```python
token = "YOUR_RECAPTCHA_TOKEN"

# Make the hidden textarea visible and set the token
driver.execute_script("""
    const textarea = document.getElementById('g-recaptcha-response');
    textarea.style.display = 'block';
    textarea.value = arguments[0];
""", token)

# If the page uses a callback:
driver.execute_script("___grecaptcha_cfg.clients[0].callback(arguments[0]);", token)
```

Then submit the form as usual.

### Flow with a solving service (2Captcha, Anti-Captcha, etc.)

1. Read `sitekey` from the page (`data-sitekey` on `.g-recaptcha`)
2. Send `sitekey` + page URL to the service
3. Get back a token
4. Inject the token and submit

This is slow, costs money, and is **not appropriate** for sites you don’t own.

---

## 4. reCAPTCHA v3 (invisible / score-based)

v3 runs in the background and returns a score. Selenium cannot “click through” it.

Options:

- **Test environment:** disable v3 or mock verification on the server
- **Automation:** use a token from a solving service that supports v3, then inject it the same way

---

## 5. What usually does *not* work (and why)

| Approach | Problem |
|----------|---------|
| `undetected-chromedriver` | Breaks often; against Google ToS |
| Disabling WebDriver flag only | Google uses many other signals |
| Auto-clicking images | Unreliable; fragile |
| Bypassing production CAPTCHA | Often illegal / against ToS |

---

## 6. Practical recommendation

| Scenario | What to do |
|----------|------------|
| You own the app (dev/QA) | Test keys, disable CAPTCHA, or mock server-side verification |
| CI/CD for your site | Backend test endpoint that skips CAPTCHA in test |
| Scraping / third-party sites | Don’t automate CAPTCHA bypass — use official APIs instead |
| Must automate a site you control in prod-like env | Token injection + licensed solving service |

---

## 7. Minimal end-to-end pattern (your site + solving service)

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://your-test-site.com/login")

sitekey = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
page_url = driver.current_url

# Pseudocode — each service has its own API
token = get_token_from_service(sitekey, page_url)

driver.execute_script(
    "document.getElementById('g-recaptcha-response').value = arguments[0];",
    token
)

driver.find_element(By.ID, "submit-btn").click()
```

---

## Version-specific notes

| Version | Behavior | Selenium approach |
|---------|----------|-------------------|
| **v2 checkbox** | User clicks “I’m not a robot”; may show image challenge | Switch to iframe, click anchor; inject token if challenge appears |
| **v2 invisible** | Triggered on form submit | Token injection only |
| **v3** | Invisible score-based | Server-side mock in test, or token from solving service |

---

## Related docs in this repo

- [`docs/HOWTO.md`](HOWTO.md) — AS400 / IBM i automation options (includes Selenium-like `as400_hod`)
- [`docs/USAGE.md`](USAGE.md) — `as400_hod` API reference

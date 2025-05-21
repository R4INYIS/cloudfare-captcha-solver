## 🛡️ Cloudflare Turnstile Solver – Shadow DOM Handler

This project is a Python automation script that simulates user interaction to **bypass Cloudflare Turnstile challenges** by locating and triggering the validation input inside **nested Shadow DOM elements**. It uses Selenium with `undetected-chromedriver` to reduce detection and access deeply embedded iframe and shadow-root structures.

---

### 📦 Features

* Automatically detects and interacts with Cloudflare Turnstile challenges.
* Navigates through **Shadow DOM** and nested **iframes** using Selenium.
* Clicks the challenge input using JavaScript execution.
* Built to work with the official [2Captcha Cloudflare demo page](https://2captcha.com/es/demo/cloudflare-turnstile).
* Uses `undetected-chromedriver` to avoid automation detection.

---

### ✅ Requirements

* Python 3.8+
* Google Chrome
* Chromedriver (automatically handled by `undetected-chromedriver`)

#### Python Libraries

Install the required libraries using:

```bash
pip install selenium undetected-chromedriver
```

---

### ⚙️ Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/cloudflare-turnstile-automation/
cd cloudflare-turnstile-automation
```

2. **Edit the script (optional):**

If you're testing on a different page or domain that uses Turnstile, make sure to update the `URL` value:

```python
URL = "https://your-target-site.com/turnstile"
```

---

### ▶️ How to Run

Start the script by running:

```bash
python main.py
```

The script will:

* Launch a Chrome window in automation mode.
* Load the target page with the Cloudflare Turnstile challenge.
* Access and interact with Shadow DOM layers and embedded iframe.
* Trigger the Turnstile validation click using JavaScript.

---

### ⚠️ Disclaimer

This project is for **educational and testing purposes only**. Automating security challenges like Turnstile may violate website terms of service. Always use responsibly and only where you are authorized to do so.

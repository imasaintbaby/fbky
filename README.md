<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1000&color=76e033&center=true&vCenter=true&width=700&lines=Meta+AI+Auto+OTP+%7C+Mr-SxR;Speciality+%C3%97+Reliability" alt="Typing SVG" />

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Open Source](https://img.shields.io/badge/Open%20Source-✓-76e033?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

</div>

---

## 📌 About

**Meta AI Auto OTP** is a Python-based automation tool developed under the **Mr-SxR** brand. It triggers OTP (One-Time Password) delivery to phone numbers through Meta AI's registration flow. The tool supports two separate automation modes — **API-based** (fast, headless HTTP requests) and **Selenium-based** (real browser automation) — giving you full flexibility depending on your use case.

> 🔧 This tool was built with a focus on **reliability, speed, and configurability** — supporting multi-threading, proxy rotation, multi-format file input, and a fully configurable `Setting.json` to skip all interactive prompts.

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🔄 **Dual Mode** | API automation for speed, Selenium browser automation for reliability |
| ⚡ **Multi-Threaded** | Process multiple numbers concurrently with configurable thread count |
| 🌐 **Proxy Support** | Single or multiple proxies with round-robin rotation and authenticated proxy tunneling |
| 📂 **Multi-Format Input** | Reads phone numbers from `.txt`, `.csv`, and `.xlsx` files with auto column detection |
| 🔁 **OTP Resend** | Configurable resend count to send multiple OTPs per number |
| 🕵️ **User-Agent Rotation** | 11 device profiles across Android, iOS, iPad, KaiOS, Windows Phone, and BlackBerry |
| ⚙️ **Configurable Settings** | All options can be pre-configured via `Setting.json` to skip interactive prompts |
| 🛠️ **Work Modes (Selenium)** | Both, Resend-Only, or Create-Only modes for existing/new accounts |
| 🌍 **Multiple Browsers** | Chrome, Edge, Firefox, Brave, and Opera support (Selenium mode) |
| 📊 **Real-Time Status** | Live counter showing checked, success, failed, and error counts |
| 📝 **Auto File Management** | Success/Failed numbers saved to separate files, remaining numbers auto-updated |

---

## ⚙️ Installation

```bash
git clone https://github.com/Mr-SxR/Meta-Auto-OTP.git
cd Meta-Auto-OTP
pip install -r requirements.txt
python main.py
```

---

## 📋 Requirements

- Windows OS (primary support)
- Google Chrome (for Selenium mode, other browsers optional)

---

## ▶️ How It Works

```
Run main.py
    ↓
Select Mode → API (Fast) or Selenium (Browser)
    ↓
Load phone numbers from file (.txt / .csv / .xlsx)
    ↓
Configure User-Agent, Proxy, OTP Resend, Threads
    ↓
Numbers are processed concurrently via thread pool
    ↓
OTP is triggered through Meta AI registration flow
    ↓
Results saved → Success_Numbers.txt / Failed_Numbers.txt
```

---

## 🗂️ Project Structure

```
├── main.py              # Entry point and main menu
├── api_bot.py           # API-based automation logic (HTTP requests)
├── selenium_bot.py      # Selenium browser automation logic
├── shared_core.py       # Shared utilities, counters, setup menus
├── config.py            # Terminal colors, UI elements, logo
├── file_reader.py       # Phone number file parsing (txt/csv/xlsx)
├── proxy_manager.py     # Proxy loading and configuration
├── proxy_helper.py      # Local proxy tunnel for authenticated proxies
├── token_extractor.py   # HTML token extraction from Meta pages
├── user_agents.py       # User-Agent string generators (11 profiles)
├── Setting.json         # Configuration file (all settings)
├── Number_List.txt      # Input: phone numbers (one per line)
├── Success_Numbers.txt  # Output: successfully processed numbers
├── Failed_Numbers.txt   # Output: failed numbers
├── requirements.txt     # Python dependencies
└── LICENSE              # MIT License
```

---

## 🔧 Configuration

Edit `Setting.json` to pre-configure all options and skip interactive prompts:

```json
{
    "api_settings": {
        "file_input_settings": {
            "always_use_txt": false,
            "use_multiple_excel_files": false
        },
        "proxy_settings": {
            "ask_for_proxy": true,
            "default_proxy": ""
        },
        "user_agent_settings": {
            "ask_for_user_agent": true,
            "default_user_agent": "none"
        },
        "otp_settings": {
            "ask_for_resend_count": true,
            "default_resend_count": 1
        },
        "thread_settings": {
            "ask_for_threads": true,
            "default_threads": 20
        }
    }
}
```

> 💡 Set any `ask_for_*` to `false` and provide `default_*` values to run without user prompts — useful for fully automated execution.

---

## 🌐 Proxy Formats

The tool supports multiple proxy input formats:

| Format | Example |
|--------|---------|
| **IP:Port** | `192.168.1.1:8080` |
| **IP:Port:User:Pass** | `192.168.1.1:8080:admin:pass123` |
| **Full URL** | `http://admin:pass123@192.168.1.1:8080` |

> 🔐 Authenticated proxies are handled through a local HTTP CONNECT tunnel — no browser extensions needed.

---

## 🕵️ User-Agent Profiles

| # | Profile | Description |
|---|---------|-------------|
| 01 | Android 4-6 | Old Android devices |
| 02 | Android 7-11 | Mid-range Android |
| 03 | Android 12-15 | Modern Android |
| 04 | iOS Old | iPhone iOS 10-12 |
| 05 | iOS Medium | iPhone iOS 13-15 |
| 06 | iOS New | iPhone iOS 16-18 |
| 07 | iPad Old | iPad iOS 10-13 |
| 08 | iPad New | iPadOS 15-18 |
| 09 | KaiOS | Feature phones |
| 10 | Windows Phone | Lumia devices |
| 11 | BlackBerry | BB10 & legacy |

---

## 📄 Output Files

| File | Description |
|------|-------------|
| `Success_Numbers.txt` | Numbers that received OTP successfully |
| `Failed_Numbers.txt` | Numbers that failed during processing |
| `Number_List.txt` | Updated in real-time with remaining unprocessed numbers |

---

## ⚠️ Disclaimer

This tool is provided for **educational and research purposes only**. Use it responsibly and in accordance with Meta's Terms of Service. The developer is not responsible for any misuse of this tool.

---

## 📬 Contact

[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/sifathub)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/+8801858094178)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/sifathub)

---

<div align="center">

*Developed & Open-Sourced by **[Mr-SxR](https://github.com/Mr-SxR)** — Speciality & Reliability*

</div>

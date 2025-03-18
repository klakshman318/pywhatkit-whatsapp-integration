# WhatsApp Message Automation using PyWhatKit & GitHub Actions

This repository demonstrates how to automate sending WhatsApp messages using Python's [pywhatkit](https://github.com/Ankit404butfound/PyWhatKit) library, integrated with GitHub Actions and a self-hosted runner.

## 📌 Features
- Send WhatsApp messages automatically via Python.
- Leverages `pywhatkit` to use WhatsApp Web.
- Runs using **GitHub Actions** with a **self-hosted runner** (GUI support required).
- One-time WhatsApp Web login (QR code scan), session persisted.

## 🚀 How It Works
1. Clone the repo and set up a Python script with `pywhatkit`.
2. Configure a GitHub Actions workflow.
3. Set up a self-hosted runner with browser support.
4. Run the workflow to send messages automatically.

## 🛠️ Requirements
- Python 3.10+
- `pywhatkit` library
- Self-hosted GitHub Actions runner (with GUI/browser access)
- WhatsApp Web login (QR code scan once)

## 📂 Project Structure
```bash
.
├── send_message.py                # Python script to send WhatsApp message via pywhatkit
├── requirements.txt               # Python dependencies file
├── README.md                      # Project documentation
└── .github
    └── workflows
        └── send-message.yml       # GitHub Actions workflow to run the message script
```

## 📦 Installation & Usage

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Script Locally (Test)

```bash
python send_message.py
```

### 3. Set Up Self-Hosted Runner
Follow GitHub’s official guide for setting up a self-hosted runner.

### 4. Trigger GitHub Action
Go to GitHub → Actions tab → Run the workflow manually.

## ❓ FAQ

### 1. Why do I need a self-hosted runner?
`pywhatkit` opens WhatsApp Web in a browser, which is not supported on GitHub's cloud runners. A self-hosted runner with GUI/browser support is required.

### 2. Do I need to scan the WhatsApp QR code every time?
No, you only need to scan the QR code once. The session will persist unless you log out or clear browser data.

### 3. Can I schedule messages instead of sending instantly?
Yes! Use `pywhatkit.sendwhatmsg(phone_no, message, time_hour, time_min)` for scheduled messages.

## 🛠️ Troubleshooting

- **Error: Browser not opening or script hangs**
  - Ensure your self-hosted runner machine has a GUI and a default browser installed.
  - Try running the script locally first to verify.

- **QR Code appears every time**
  - Make sure your browser retains session/cookies. Don’t clear site data for WhatsApp Web.

- **GitHub Action stuck on 'Running'**
  - Check that your self-hosted runner is active and terminal window is running `./run.sh`.

- **Permission Denied (Linux)**
  - Run: `chmod +x ./run.sh` and `chmod +x ./config.sh`

## 🤝 Contributing

Contributions are welcome! If you find a bug or have a feature request, open an issue or submit a pull request.

1. Fork the repo
2. Create a new branch
3. Commit changes
4. Push and create a PR

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![GitHub Actions](https://github.com/klakshman318/pywhatkit-whatsapp-integration/actions/workflows/send-message.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)

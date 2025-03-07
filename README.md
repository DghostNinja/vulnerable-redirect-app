

# 🚀 Vulnerable Open Redirect Testing App

A simple **Flask-based vulnerable web application** designed for **testing Open Redirect vulnerabilities**. This app is intentionally vulnerable, making it ideal for penetration testing and security research.

---

## 🔹 Features
- Simulates **Open Redirect** issues using common redirect parameters.
- Supports testing with **various payloads**.
- Runs inside a **Docker container** for easy deployment.
- Logs all requests for **better debugging**.

---

## 📂 Folder Structure
```
/vulnerable-redirect-app
│── Dockerfile                # Contains Docker build instructions
│── vulnerable_redirect_app.py # The vulnerable Flask app
│── requirements.txt           # Dependencies (Flask)
│── README.md                  # Documentation
└── .gitignore                 # Excludes unnecessary files
```

---

## 🚀 Quick Start Guide
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DghostNinja/vulnerable-redirect-app.git
cd vulnerable-redirect-app
```

### 2️⃣ Build and Run with Docker
```bash
docker build -t vulnerable-redirect .
docker run -p 5000:5000 vulnerable-redirect
```
[!](screenshots/builda.png)
[!](screenshots/buildb.png)
[!](screenshots/buildc.png)

### 3️⃣ Test for Open Redirect
Visit the following URL in your browser or use `curl`:
```
http://localhost:5000/redirect?url=http://evil.com
```
✅ If vulnerable, it will **redirect you to `http://evil.com`**.

---

## ⚠️ Disclaimer
**This project is for educational and ethical testing purposes only!** Do **not** use it on production systems without proper authorization.

---

## 🤝 Contributing
Feel free to submit **issues or pull requests** to improve this tool!

📧 **Contact:** [https://github.com/DghostNinja/]


# 🚨 AI Phishing Detector

This directory contains essential information about the **AI Phishing Detector** — a robust security tool built during the Innovation Phase at Broskieshub.com.  
It proactively monitors Gmail inboxes, leveraging a fine-tuned BERT machine learning model to detect phishing emails through intelligent text, keyword, and URL analysis.

***

### ➡️ View Main Project Repository

To explore the full codebase, documentation, installation guide, and live demo, view the dedicated repository:

🔗 [AI Phishing Detector](https://github.com/ultrew/Ai_Phishing_Detector)

***

### 🧠 What Makes It Unique?

- **Automated Gmail Monitoring:** Scans inboxes every 5 minutes using Gmail API integration for real-time security.
- **AI-Powered Detection:** Employs a fine-tuned BERT transformer model for advanced phishing prediction and probability scoring.
- **Multifaceted Analysis:** Flags risky keywords, suspicious URLs, common phishing patterns, and manages trusted domain filtering.
- **Actionable Alerts & Labeling:** Instantly labels phishing emails, sends notification alerts, and safely whitelists known domains.
- **Interactive Dashboard:** Web dashboard lets users view, search, filter, and export scan history with intuitive controls.
- **Full Data Control:** Uses an SQLite database with soft-delete, undo functions, and CSV export for convenience.

***

### 🧩 Architecture Snapshot

- **Gmail Watcher:** A background Python script fetching emails and sending them for analysis.
- **Flask API & Dashboard:** Hosts the detection model and serves scan data with a sleek front-end.
- **Shared Database:** Robust record keeping for both components with easy management.

***

### ⚙️ Tech Stack

- Python (core logic, Gmail integration)
- Flask (API and dashboard)
- SQLAlchemy (database ORM)
- Transformers (Hugging Face BERT model)
- Google Cloud Gmail API (OAuth credentials)
- HTML (interactive dashboard)

***

### 📹 Demonstration

A step-by-step video demo showcasing phishing detection in action, dashboard insights, and CSV exports is provided in the repository.

***

End of report.
This version is concise, highlights distinctive features, and is formatted for clarity. It is ideal for professional presentations, GitHub README.md, or sharing on your portfolio or LinkedIn. If you need a more technical breakdown or prefer a shorter summary, let me know![1]

[1](https://github.com/ultrew/Ai_Phishing_Detector)

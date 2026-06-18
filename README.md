# BigQuery Release Notes Explorer 🚀

A premium, interactive web dashboard for real-time exploring, searching, and sharing Google BigQuery release notes. 

Built with **Python Flask** on the backend and a stunning **glassmorphic vanilla HTML, JavaScript, and CSS** frontend.

![BigQuery Release Notes Explorer](https://img.shields.io/badge/Stack-Flask%20%7C%20HTML5%20%7C%20CSS3%20%7C%20JS-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Dynamic Feed Parsing**: Automatically fetches and parses Google Cloud's official BigQuery Atom XML feed.
- **Granular Classification**: Detects and breaks down multiple announcements, features, issues, and deprecations published under the same day.
- **Premium Glassmorphic UI**: Sleek dark mode visual design built with HSL tailored colors, responsive card grids, custom Google Fonts (`Outfit`, `Inter`), and subtle ambient glow effects.
- **Real-Time Search & Filtering**: Instantly filter updates by category chips or perform substring searches across the title, body content, and release date.
- **Loading State Feedback**: Smooth, non-blocking skeleton card loaders and interactive rotating spin animations on the feed refresh controller.
- **X/Twitter Composer Integration**: Quick share button on every update card that strips HTML formatting, applies a template within character limits, auto-generates hashtags (`#BigQuery`, `#GoogleCloud`), and pre-populates X/Twitter web intent compositor with a target anchor link.

---

## 📂 Project Directory Structure

```text
├── app.py                  # Flask backend server & XML parser
├── requirements.txt        # Python dependencies
├── .gitignore              # Version control configuration exclusions
├── templates/
│   └── index.html          # Dashboard HTML view & JS search/filter engine
└── static/
    └── style.css           # Premium HSL styling system & animations
```

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.8 or higher installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/bigquery-release-explorer.git
   cd bigquery-release-explorer
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the dashboard:**
   Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! If you want to extend this tracker to support multiple Google Cloud services, feel free to submit a pull request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

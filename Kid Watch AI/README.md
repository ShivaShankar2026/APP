# 🛡️ Kid Watch AI — YouTube Kids Sentiment & Safety Analysis

## 🌐 Live Demo

**[Launch the app →](https://app-production-11f0.up.railway.app/)**

A Django web application that analyzes YouTube video comments for sentiment and flags content that may be unsafe for children — combining NLP sentiment analysis with a child-safety keyword filter, wrapped in a YouTube-style interface.

**GitHub repo:** https://github.com/ShivaShankar2026/App

---

## 📌 Project Overview

Parents and platforms struggle to know what kids are actually exposed to in video comment sections. This project:

- Takes a YouTube video URL as input
- Fetches the video and its comments via the YouTube Data API
- Runs sentiment analysis (VADER) on the video and each comment
- Runs each comment through a **child-safety keyword filter** — flagging bullying language, adult content, violence, and grooming-pattern phrases
- Displays results in a YouTube-style interface, with flagged comments automatically blurred/redacted
- Gives admins a dashboard to manage users and review aggregate sentiment trends

---

## ✨ Features

- 🔐 User registration with admin approval workflow (Pending → Accepted/Declined)
- 🔎 Paste any YouTube URL to analyze its comments
- 😀 Sentiment classification: Very Positive → Very Negative (VADER)
- 🛡️ Child-safety keyword filter — flags bullying, adult content, violence, and personal-info/grooming-pattern requests
- 🙈 Automatic blur/redaction of flagged comments in the UI
- 📺 YouTube-style interface — video embed, comment feed, related-videos sidebar
- 👤 User profile management with photo upload
- ⭐ In-app feedback system with its own sentiment scoring
- 📊 Admin dashboard — user management, search history, sentiment pie chart

---

## 🛠 Technologies Used

- **Backend:** Python 3.10, Django 4.1.5
- **Database:** MySQL
- **NLP:** VADER Sentiment Analysis (`vaderSentiment`)
- **Safety filtering:** Custom keyword-based classifier (`child_safety_filter.py`)
- **APIs:** YouTube Data API v3 (`google-api-python-client`)
- **Frontend:** Django Templates, Bootstrap 5
- **Other:** `beautifulsoup4`, `langdetect`, `requests`

---

## 📂 Project Structure

```
App/
│
├── manage.py
├── requirements.txt
├── Procfile                        # for Railway/Render deployment
├── youtube_kids.sql                # database schema/export
│
├── ytksa/                          # Django settings package
│   ├── settings.py                 # reads secrets from env vars
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── adminapp/                       # Admin dashboard app
├── mainapp/                        # Public-facing pages
├── userapp/                        # User features
│   ├── views.py
│   ├── models.py
│   ├── urdu_sentiment.py
│   └── child_safety_filter.py      # keyword-based child-safety filter
│
├── assets/
│   ├── templates/                  # HTML templates (YouTube-style UI)
│   └── static/
│
└── media/                          # user-uploaded photos
```

---

## ⚙️ Local Setup

### Clone the repository
```bash
git clone https://github.com/ShivaShankar2026/App.git
cd App
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Set required environment variables
```bash
# Windows PowerShell
$env:DJANGO_SECRET_KEY="your-secret-key"
$env:DJANGO_DEBUG="True"
$env:DB_NAME="youtube_kids"
$env:DB_HOST="localhost"
$env:DB_USER="root"
$env:DB_PASSWORD="your-mysql-password"
$env:YOUTUBE_API_KEY="your-youtube-api-key"
```

### Set up the database
```bash
# Create a MySQL database named youtube_kids, then:
python manage.py migrate
# Or import the provided schema directly:
mysql -u root -p youtube_kids < youtube_kids.sql
```

### Run
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000`

---

## 🛡️ How Child-Safety Filtering Works

Every comment fetched from a YouTube video is checked against `child_safety_filter.py`, which scans for:

| Category | Examples |
|---|---|
| Bullying | insults, "nobody likes you", threats |
| Adult content | explicit/sexual terms |
| Violence | weapons, threats of harm |
| Grooming patterns | requests for personal info, "keep this secret" phrasing |

Flagged comments are **not deleted** — they're blurred in the UI with a visible "⚠ Flagged" tag and the matched category, so a supervising adult can still review them if needed, while keeping the default view child-safe.

This is a first-line, free, no-API filter. It can be extended with Google's Perspective API for deeper toxicity scoring.

---

## 🌐 Deployment

This project is configured to deploy on **Railway** (or Render/PythonAnywhere with adjustments):

1. Push to GitHub (already done — see repo link above)
2. Connect the repo on [railway.app](https://railway.app)
3. Add a MySQL database in the same Railway project
4. Set the environment variables listed above in Railway's dashboard
5. Railway builds using the included `Procfile`:
   ```
   web: gunicorn ytksa.wsgi --log-file -
   ```   
6. Generate a public domain under Settings → Networking

---

## 👨‍💻 Author

**Kondrathi Shiva Shankar**

- B.Tech Computer Science & Engineering
- Python Developer
- AI/ML & Computer Vision Enthusiast

GitHub: https://github.com/ShivaShankar2026

LinkedIn: https://www.linkedin.com/in/kondrathi-shiva-shankar-8008ss/

---

## 📄 License

This project is developed for educational purposes.

MIT License

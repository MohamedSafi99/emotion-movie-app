# 🎬 Mood-Based Movie Recommender

This is a full-stack web application that recommends movies based on your current **mood or feeling**. Whether you're happy, sad, relaxed, or adventurous — this app helps you find the perfect movie match!

Built using:

- 🧠 **Django** (Python) as the backend API
- ⚛️ **React** as the frontend
- 🌐 **TMDb API** to fetch real movie data
- 🧠 (Optional ML model: planned for future to enhance smart mood-to-genre mapping)

## 📸 Demo

> ▶️ Watch the demo video: [Link to your video on Google Drive or YouTube]

---

## 💡 Features

- Select your mood from a predefined list (e.g., Happy, Sad, Romantic, Angry, etc.)
- Get a personalized movie recommendation with:
  - 🎥 Title & Poster
  - 📝 Overview
  - 🔗 Link to watch the trailer
- Clean, modern, responsive UI
- Works seamlessly on mobile and desktop

---

## 🚀 How to Run Locally

### Prerequisites:

- Python 3.10+
- Node.js & npm
- (Recommended: Use a virtual environment for Python)

### Backend Setup (Django)

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt

# Run the backend server
python manage.py runserver

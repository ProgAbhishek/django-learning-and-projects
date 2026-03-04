# Weather App

A minimalist Django  project that fetches the current weather for any city using the OpenWeather API and renders a glassmorphism-style single-page interface.

## Features
- Search for any city and display its temperature, conditions, icon, and current date
- Metric units (°C) fetched via OpenWeather's `/weather` endpoint
- Default city fallback (`Kathmandu`) so the UI always shows data
- Graceful handling of missing or malformed API responses

## Tech Stack
- Python 3.11+
- Django 6.0.2
- Requests 2.32.5
- OpenWeather REST API

## Project Structure
```
Weather-App/
├── README.md
├── weatherproject/
│   ├── db.sqlite3
│   ├── manage.py
│   ├── weatherapp/
│   │   ├── templates/weatherapp/index.html
│   │   ├── urls.py
│   │   └── views.py
│   └── weatherproject/
│       ├── settings.py
│       └── urls.py
└── env/ (optional virtual environment)
```

## Prerequisites
- Python 3.11 or newer
- A free OpenWeather API key (https://openweathermap.org/api)

## Setup
1. **Clone the project**
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd Weather-App/weatherproject
   ```
2. **Create & activate a virtual environment**
   ```bash
   python -m venv env
   # Windows PowerShell
   .\env\Scripts\Activate.ps1
   ```
3. **Install dependencies**
   ```bash
   pip install django==6.0.2 requests==2.32.5
   ```
4. **Configure your OpenWeather key**
   - Replace the placeholder key inside `weatherapp/views.py` with your own key, **or** load it from an environment variable and reference it from there before committing the project to GitHub.
5. **Run database migrations (SQLite)**
   ```bash
   python manage.py migrate
   ```
6. **Start the dev server**
   ```bash
   python manage.py runserver
   ```



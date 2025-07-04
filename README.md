# Django News Website

A simple Django-based news website that fetches real-time news using the NewsAPI.

---

## Features

- Browse top news headlines in real-time
- View news details
- Responsive UI with Django templates

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/newswebsite-python-django-newsapi.git
cd newswebsite-python-django-newsapi/newsproject
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the `newsproject` directory with your NewsAPI key:

```
NEWSAPI_KEY=your_actual_newsapi_key_here
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Project Structure
```
newsproject/
    manage.py
    .env
    db.sqlite3
    requirements.txt
    newsapp/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
        urls.py
        templates/
            newsapp/
                base.html
                index.html
                detail.html
        static/
            newsapp/
                css/
                js/
                images/
    newsproject/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```
---

## License

This project is licensed under the MIT License.

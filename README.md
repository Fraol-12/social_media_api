Social Media API

A fully functional RESTful Social Media API built with Django and Django REST Framework (DRF).
Implements user authentication, posts, comments, follows, likes, and notifications. Designed to be secure, modular, and scalable, closely simulating real-world backend scenarios.

🚀 Features Implemented (Task 0)

Custom User Model with profile and followers

Token-based Authentication (DRF)

User Registration & Login

Profile Retrieval & Update

Secure-by-default API configuration

Planned Features (Structure Ready)

Posts & Comments

Follow System & User Feed

Likes & Notifications

Production-ready deployment configuration

🛠 Tech Stack

Python: 3.14

Django: 6.0

Django REST Framework (DRF)

DRF Token Authentication

SQLite (development)

Optional: PostgreSQL for production

📂 Project Structure
social_media_api/
│
├── accounts/                  # User authentication and profile management
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── posts/                     # Posts, Comments, Likes
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── urls.py
│   └── views.py
│
├── notifications/             # Notification system
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── social_media_api/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
└── README.md
⚙️ Installation & Setup

Clone the repository

git clone https://github.com/<your-username>/social_media_api.git
cd social_media_api

Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Install dependencies

pip install -r requirements.txt
# Or manually
pip install django djangorestframework djangorestframework-authtoken django-filter

Apply migrations

python manage.py makemigrations
python manage.py migrate

Create a superuser

python manage.py createsuperuser

Run the development server

python manage.py runserver

Server URL: http://127.0.0.1:8000/

🔐 Authentication

This API uses Token Authentication.
Include the header in requests that require authentication:

Authorization: Token <your_token>
📌 API Endpoints (Task 0)
Register User

POST /api/accounts/register/

Request:

{
  "username": "john",
  "email": "john@email.com",
  "password": "strongpassword"
}

Response:

{
  "id": 1,
  "username": "john",
  "email": "john@email.com"
}
Login

POST /api/accounts/login/

Request:

{
  "username": "john",
  "password": "strongpassword"
}

Response:

{
  "token": "your_token_here",
  "username": "john"
}
User Profile

GET /api/accounts/profile/

Headers:

Authorization: Token <your_token>

Response:

{
  "id": 1,
  "username": "john",
  "email": "john@email.com",
  "bio": "",
  "profile_picture": null
}
🧠 Architecture Decisions

Custom User Model for extensibility

Token Authentication for stateless API design

Default Permission: IsAuthenticated for secure-by-default behavior

Modular Apps: (accounts, posts, notifications) for clean separation of concerns

SQLite for development; easy switch to PostgreSQL for production

📈 Next Steps / Tasks

Implement Posts & Comments

Implement Follow System & Feed

Implement Likes & Notifications

Deploy to production (Heroku, Render, AWS)

📜 License

Part of the ALX Backend Web Development Program
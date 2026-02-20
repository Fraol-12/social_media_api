# Social Media API

A RESTful Social Media API built with Django and Django REST Framework.

This project implements user authentication and profile management as the foundational step toward building a fully featured social media backend system.

---

## 🚀 Features Implemented (Task 0)

- Custom User Model
- Token-Based Authentication
- User Registration
- User Login
- Profile Retrieval & Update
- Secure-by-default API configuration

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- DRF Token Authentication
- SQLite (development)

---

## 📂 Project Structure

```
social_media_api/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── social_media_api/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
```

### 3. Install dependencies

```bash
pip install django djangorestframework
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run development server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication

This API uses Token Authentication.

Include the following header in authenticated requests:

```
Authorization: Token <your_token>
```

---

## 📌 API Endpoints

### Register User

**POST**
```
/api/accounts/register/
```

Request body:

```json
{
  "username": "john",
  "email": "john@email.com",
  "password": "strongpassword"
}
```

Response:

```json
{
  "id": 1,
  "username": "john",
  "email": "john@email.com"
}
```

---

### Login

**POST**
```
/api/accounts/login/
```

Request body:

```json
{
  "username": "john",
  "password": "strongpassword"
}
```

Response:

```json
{
  "token": "your_token_here",
  "username": "john"
}
```

---

### User Profile

**GET**
```
/api/accounts/profile/
```

Headers:
```
Authorization: Token <your_token>
```

Response:

```json
{
  "id": 1,
  "username": "john",
  "email": "john@email.com",
  "bio": "",
  "profile_picture": null
}
```

---

## 🧠 Architecture Decisions

- Custom User Model created at project start to allow extensibility.
- Token authentication chosen for simplicity and stateless API design.
- Default permission set to `IsAuthenticated` to enforce secure-by-default behavior.

---

## 📈 Next Steps

- Posts & Comments
- Follow System
- Feed Generation
- Likes & Notifications
- Production Deployment

---

## 📜 License

This project is part of the ALX Backend Web Development program.
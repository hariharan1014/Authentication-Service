# 🔐 Authentication Service API

A RESTful Authentication Service built using Flask that provides secure user authentication and authorization using JSON Web Tokens (JWT). The project follows a clean service-layer architecture and implements essential authentication features such as registration, login, profile management, password management, token refresh, logout with JWT blacklisting, and account deletion.

---

## 🚀 Features

- User Registration
- User Login
- JWT Access Token Authentication
- JWT Refresh Token Authentication
- Protected Routes
- View User Profile
- Update Username & Email
- Change Password
- Logout (JWT Blacklisting)
- Delete User Account
- Password Hashing using Flask-Bcrypt
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Input Validation
- Custom JWT Error Handlers
- Swagger / OpenAPI Documentation (Flasgger)

---

## 🛠️ Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy ORM
- PostgreSQL
- Flask-JWT-Extended
- Flask-Bcrypt
- Flasgger (Swagger / OpenAPI)
- python-dotenv

---

## 📂 Project Structure

```
Authentication-Service/
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── README.md
├── .env
│
├── models/
│   └── user.py
│
├── routes/
│   └── auth_routes.py
│
├── services/
│   └── auth_service.py
│
├── utils/
│   ├── security.py
│   ├── validation.py
│   └── token_blacklist.py
│
└── instance/
```

---

## 🏗️ Architecture

```
Client (Postman / Frontend)
            │
            ▼
      Flask Routes
            │
            ▼
      Service Layer
            │
            ▼
     SQLAlchemy ORM
            │
            ▼
    PostgreSQL Database
```

---

## 🔑 Authentication Flow

### Register

```
POST /register
```

Creates a new user after validating the input.

---

### Login

```
POST /login
```

Returns

- Access Token
- Refresh Token

---

### View Profile

```
GET /profile
```

Requires a valid Access Token.

---

### Update Profile

```
PUT /profile
```

Allows updating

- Username
- Email

---

### Change Password

```
PUT /profile/password
```

Requirements

- Current Password
- New Password

The new password cannot be the same as the current password.

---

### Refresh Access Token

```
POST /refresh
```

Requires a valid Refresh Token and returns a new Access Token.

---

### Logout

```
POST /logout
```

Blacklists the current Access Token so it cannot be used again.

---

### Delete Account

```
DELETE /profile
```

Deletes the authenticated user's account and revokes the current Access Token.

---

## 🔒 Security Features

- Passwords are hashed using Flask-Bcrypt.
- JWT Authentication using Access & Refresh Tokens.
- JWT Blacklisting for secure logout.
- Protected endpoints using JWT decorators.
- Input validation before database operations.
- Duplicate username and email checks.
- Password verification before password changes.
- Custom JWT error handlers for consistent API responses.

---

## 📖 API Documentation

Swagger UI is integrated using **Flasgger**.

After running the application, open

```
http://127.0.0.1:5000/apidocs/
```

to view the interactive API documentation.

> **Note:** Due to a compatibility issue between Flask 3.x and the current Flasgger release, some Swagger UI static assets may not render correctly. The API itself remains fully functional.

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Authentication-Service
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure the environment variables in `.env`

Example

```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=postgresql://username:password@localhost/database_name
```

Run the application

```bash
python app.py
```

---

## 🧪 Tested APIs

- Register User
- Login User
- View Profile
- Update Profile
- Change Password
- Refresh Token
- Logout
- Delete User
- JWT Error Responses
- Token Blacklisting
- Protected Routes

All endpoints were tested using **Postman**.

---

## 🚀 Future Improvements

- Redis-based Token Blacklisting
- Email Verification
- Forgot Password
- Password Reset via Email
- Role-Based Access Control (RBAC)
- Docker Support
- Unit Testing
- CI/CD Pipeline
- Cloud Deployment (AWS / Render / Railway)

---

## 👨‍💻 Author

**Hariharan R**

Backend Developer | Python | Flask | REST APIs | PostgreSQL

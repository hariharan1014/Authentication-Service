# Authentication Service

A production-style Authentication Service built using Flask and PostgreSQL as part of my Python Backend Developer learning roadmap.

## Features

- User Registration
- User Login
- Password Hashing using Flask-Bcrypt
- JWT Access Token Generation
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Duplicate Username & Email Validation
- Service Layer Architecture

## Tech Stack

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Bcrypt
- Flask-JWT-Extended
- python-dotenv

## Project Structure

```
Authentication Service/
│
├── app.py
├── config.py
├── extensions.py
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
└── utils/
    ├── validation.py
    └── security.py
```

## Completed Features

### Registration
- Validate registration data
- Check duplicate username and email
- Hash password using Bcrypt
- Store user in PostgreSQL

### Login
- Verify user credentials
- Verify password using Bcrypt
- Generate JWT Access Token

## Next Steps

- Protected Routes
- User Profile API
- Refresh Tokens
- Logout Strategy
- Swagger Documentation
- Testing

## Learning Goals

This project is part of my journey toward becoming a Python Backend Developer by building production-style backend applications while learning clean architecture and backend engineering principles.
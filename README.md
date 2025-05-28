# My App MVC – Flask-based User Management System

## Overview

This is a simple yet fully modular **MVC-structured application** built with **Flask**, designed to demonstrate best practices in clean architecture and Python backend development. The system manages user data in a local **SQLite3** database, with endpoints to register and retrieve users via a RESTful API.

The project includes a layered structure with clear separation of responsibilities:
- **Model**: Database schema and domain entities
- **View**: Request validation, response formatting, and interface handling
- **Controller**: Business logic
- **Driver**: Infrastructure components like the database connector

## Features

- Register a new user (name, age, height)
- Retrieve users by name (query parameter)
- Automatic database creation on startup
- Persistent SQLite3 local database with safe directory creation
- Modular, testable architecture following Clean Code and SRP principles

## Endpoints

### `POST /rota/user/post`

Registers a new user.

**Payload:**
```json
{
  "usuario": {
    "nome": "igor",
    "idade": 34,
    "altura": 1.83
  }
}
````

**Response:**

```json
{
  "success": true,
  "Type": "User",
  "count": 1,
  "attributes": {
    "name": "igor",
    "age": 34,
    "height": 1.83
  }
}
```

---

### `GET /rota/user/get?name=igor`

Retrieves all users matching the given name.

**Response:**

```json
{
  "success": true,
  "Type": "User",
  "count": 1,
  "attributes": [
    {
      "nome": "igor",
      "idade": 34,
      "altura": 1.83
    }
  ]
}
```

## Project Structure

```
my-app-mvc/
│
├── run.py                         # Flask app runner
├── database/                      # SQLite3 database folder
│   └── db.sqlite
│
├── driver/
│   ├── db_connector.py           # DB abstraction (connect, cursor)
│   ├── db_setup.py               # Table creation logic
│   └── paths.py                  # OS-agnostic DB path setup
│
├── model/
│   ├── user.py                   # User entity + repository
│
├── controller/
│   └── user_controller.py        # Encapsulates logic for user registration and lookup
│
├── src/
│   └── main/
│       ├── server/
│       │   └── server.py         # Flask app instance
│       └── routes/
│           └── users.py          # Route factory (`create_user_routes`)
│
└── src/views/
    └── user_view.py              # Input/output logic and validations
```

## Setup & Usage

### 1. Install dependencies

> No dependencies are needed beyond Flask and Python 3.9+

```bash
pip install flask
```

### 2. Run the application

```bash
python run.py
```

### 3. Test the endpoints

Using `curl`:

```bash
curl -X POST http://127.0.0.1:3001/rota/user/post \
  -H "Content-Type: application/json" \
  -d '{"usuario": {"nome": "igor", "idade": 34, "altura": 1.83}}'

curl "http://127.0.0.1:3001/rota/user/get?name=igor"
```

## Notes

* All database connections are safely opened and closed inside the controller logic.
* The system will automatically create the `database/` folder and the SQLite3 file if it doesn't exist.
* Prepared statements are used to prevent SQL injection vulnerabilities.

## Author

**Igor Caetano Diniz**
Machine Learning Engineer | Software Engineer | Data Consultant

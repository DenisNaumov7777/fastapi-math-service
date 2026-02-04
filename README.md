# 🧮 MathOps Service (FastAPI)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-green)
![Status](https://img.shields.io/badge/Status-Production_Ready-success)
![License](https://img.shields.io/badge/License-Apache_2.0-blue)

**Author:** Denis Naumov  
**Location:** Cologne, Germany 🇩🇪

## 📖 Overview

**MathOps Service** is a lightweight, high-performance microservice built with **FastAPI**. It provides a robust REST API for mathematical operations along with a user-friendly web interface.

This project demonstrates **Enterprise-grade** backend practices, including:
* **Strict Type Validation** (Pydantic & Python Type Hints).
* **Middleware Integration** (CORS, Process Time Logging).
* **Global Error Handling** (JSON responses for validation and logic errors).
* **Interactive Documentation** (Swagger UI).
* **Modular Architecture** (Separation of concerns).

## 🛠 Tech Stack

* **Framework:** FastAPI
* **Server:** Uvicorn (ASGI)
* **Frontend:** Jinja2 + Bootstrap 4
* **Language:** Python 3.10+

## 🚀 Installation & Run

### 1. Clone the repository
```bash
git clone [https://github.com/DenisNaumov7777/fastapi-math-service.git](https://github.com/DenisNaumov7777/fastapi-math-service.git)
cd fastapi-math-service

```

### 2. Install dependencies

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt

```

### 3. Start the server

```bash
fastapi dev main.py

```

*(The server will start at `http://127.0.0.1:8080`)*

## 📚 API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, visit:

* **Swagger UI:** [http://127.0.0.1:8080/docs](https://www.google.com/search?q=http://127.0.0.1:8080/docs)
* **ReDoc:** [http://127.0.0.1:8080/redoc](https://www.google.com/search?q=http://127.0.0.1:8080/redoc)

## 🧪 Usage Examples

### Web Interface

Open `http://127.0.0.1:8080/` in your browser to use the graphical calculator.

### API Endpoints (cURL)

**Division (Success):**

```bash
curl "[http://127.0.0.1:8080/div?num1=10&num2=2](http://127.0.0.1:8080/div?num1=10&num2=2)"
# Response: 5

```

**Division (Error Handling):**

```bash
curl -i "[http://127.0.0.1:8080/div?num1=5&num2=0](http://127.0.0.1:8080/div?num1=5&num2=0)"
# Response: 400 Bad Request
# {"detail": "Cannot divide by zero"}

```

## 📂 Project Structure

```text
fastapi-math-service/
├── Maths/              # Mathematical Logic Package
│   ├── __init__.py     # Exports functions
│   └── mathematics.py  # Pure Python logic
├── templates/          # Frontend Templates
│   └── index.html      # UI with Bootstrap & JS
├── main.py             # Application Entry Point
├── requirements.txt    # Dependencies
└── README.md           # Documentation

```

---

*Developed with ❤️ in Cologne.*

```

---

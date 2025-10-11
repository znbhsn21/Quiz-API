# Quiz API 🚀

This project is a Django-based REST API for managing quizzes. It allows users to retrieve questions, add new questions (admin), submit answers, and register new accounts. Authentication is handled using JWT (JSON Web Tokens).

## 🚀 Key Features

- **Question Management**:
    - Retrieve all quiz questions.
    - Add new questions to the database (admin access required).
- **Answer Submission**:
    - Submit answers to the quiz and receive a score. Requires user authentication.
- **User Authentication**:
    - User registration endpoint.
    - JWT authentication for secure access to protected endpoints.
    - Token refresh mechanism for continuous session management.
- **RESTful API**:
    - Follows REST principles for easy integration with frontend applications.
- **Admin Interface**:
    - Django admin panel for managing questions and users.

## 🛠️ Tech Stack

- **Backend**:
    - Django
    - Django REST Framework
    - Django REST Framework Simple JWT
- **Database**:
    - Configurable via `settings.py` (e.g., SQLite, PostgreSQL, MySQL)
- **Core**:
    - Python
- **Utilities**:
    - `manage.py` (Django command-line tool)

## 📦 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd quizapi
    ```

2.  Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3.  Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5.  Apply migrations:

    ```bash
    python manage.py migrate
    ```

6.  Create a superuser (admin account):

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create an admin user.

### Running Locally

1.  Start the development server:

    ```bash
    python manage.py runserver
    ```

    The API will be accessible at `http://127.0.0.1:8000/`.

2.  Access the Django admin panel at `http://127.0.0.1:8000/admin/` and log in with the superuser credentials created earlier.

## 💻 Usage

### API Endpoints

-   **GET /questions/**: Retrieve all questions.
-   **POST /add_questions/**: Add a new question (admin access required).
    -   Requires authentication and appropriate permissions.
-   **POST /submit/**: Submit answers and get the score (authentication required).
    -   Requires a JSON payload with user answers.
-   **POST /register/**: Register a new user.
    -   Requires username and password.
-   **POST /token/**: Obtain JWT token (authentication required).
    -   Requires username and password.
-   **POST /token/refresh/**: Refresh JWT token.
    -   Requires a valid refresh token.

### Example Usage (using `curl`)

1.  **Register a new user:**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}' http://127.0.0.1:8000/register/
    ```

2.  **Obtain a JWT token:**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}' http://127.0.0.1:8000/token/
    ```

    This will return a JSON response containing `access` and `refresh` tokens.

3.  **Submit answers (requires authentication):**

    ```bash
    curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <access_token>" -d '[{"question_id": 1, "answer": "a"}, {"question_id": 2, "answer": "b"}]' http://127.0.0.1:8000/submit/
    ```

    Replace `<access_token>` with the actual access token obtained in the previous step.

## 📂 Project Structure

```
quizapi/
├── manage.py               # Django management script
├── quizapi/                # Core project directory
│   ├── __init__.py
│   ├── settings.py           # Project settings
│   ├── urls.py               # Project URL configuration
│   ├── asgi.py               # ASGI configuration
│   └── wsgi.py               # WSGI configuration
├── quiz/                   # Quiz app directory
│   ├── __init__.py
│   ├── models.py             # Data models
│   ├── views.py              # API views
│   ├── serializers.py        # Data serializers
│   ├── urls.py               # App URL configuration
│   ├── migrations/           # Database migrations
│   │   └── ...
│   ├── apps.py               # App configuration
│   ├── admin.py              # Admin panel configuration
│   └── tests.py              # Tests
├── venv/                   # Virtual environment directory (not in repo)
├── db.sqlite3              # SQLite database (if used)
└── requirements.txt        # Project dependencies
```


## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Push your changes to your fork.
5.  Submit a pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contact

Zenab Adnan - zenabadnan10@gmail.com

## 💖 Thanks Message

Thank you for checking out this project! We hope it's helpful for your quiz management needs.



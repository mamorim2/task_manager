Task Manager API

A simple task management system built with Django & Django REST Framework (DRF) using Test-Driven Development (TDD). Users can create, read, update, and delete tasks, assign tasks to users, filter by status/due date, and authenticate via JWT tokens.

🚀 Features

✔ CRUD operations for tasks✔ JWT authentication for user access✔ Filtering and ordering by status and due date✔ Pagination for listing tasks efficiently✔ Dockerized environment for easy deployment✔ 100% Test Coverage using Pytest

📂 Project Structure

task_manager/
│── task_manager/       # Main project settings
│── tasks/              # App handling tasks
│── users/              # JWT authentication
│── tests/              # Unit tests
│── requirements.txt    # Python dependencies
│── Dockerfile          # Docker setup
│── docker-compose.yml  # Multi-container setup
│── README.md           # Project documentation

🛠️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/mamorim2/task_manager.git
cd task_manager

2️⃣ Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up the Database

python manage.py migrate

5️⃣ Create a Superuser

python manage.py createsuperuser

Follow the prompts to create an admin user.

6️⃣ Run the Development Server

python manage.py runserver

Now visit http://127.0.0.1:8000/admin/ to access the Django Admin.

🐳 Docker Setup (Optional)

If you prefer running via Docker:

docker-compose up --build

This will start both the PostgreSQL database and the Django API.

🔒 Authentication (JWT)

This API uses JWT tokens for authentication.

Obtain a Token

POST /api/auth/token/

Request

{
  "username": "your_username",
  "password": "your_password"
}

Response

{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}

Refresh Token

POST /api/auth/token/refresh/

Request

{
  "refresh": "your_refresh_token"
}

Response

{
  "access": "new_access_token"
}

Use Token for Authentication

For API requests, include the token in the headers:

Authorization: Bearer your_access_token

📀 API Endpoints

1️⃣ Task Endpoints

Method

Endpoint

Description

Authentication

GET

/api/tasks/

List all tasks (paginated)

✅ Required

POST

/api/tasks/

Create a new task

✅ Required

GET

/api/tasks/{id}/

Retrieve task details

✅ Required

PUT

/api/tasks/{id}/

Update an existing task

✅ Required

DELETE

/api/tasks/{id}/

Delete a task

✅ Required

2️⃣ Task Filtering & Ordering

Tasks can be filtered by status and due_date:

GET /api/tasks/?status=completed
GET /api/tasks/?due_date=2025-01-01

Tasks can also be ordered by created_at or due_date:

GET /api/tasks/?ordering=due_date
GET /api/tasks/?ordering=-created_at  # Descending order

🧠 Running Tests

To ensure everything is working correctly, run:

pytest --cov=tasks

or with Django’s built-in test runner:

python manage.py test

✅ Ensures all components are tested✅ Includes authentication, permissions, and API tests

📖 API Documentation

This project includes Swagger API docs using drf-yasg.

To view the documentation, start the server and visit:

http://127.0.0.1:8000/swagger/

or

http://127.0.0.1:8000/redoc/

💡 Future Improvements

🔹 Rate limiting to prevent API abuse
🔹 Background task processing (Celery + Redis)
🔹 Frontend (React or Angular) for UI
🔹 Role-based permissions

📝 License

This project is licensed under the MIT License.

💬 Need Help?

If you have any questions, feel free to open an issue on GitHub.


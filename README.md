# Little Lemon Web Application

A Django web application built for the Meta Back-End Developer Capstone. The project includes menu management, table-booking APIs, and token authentication.

## Technologies

- Python
- Django
- Django REST Framework
- SQLite for local development
- MySQL configuration

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/SUJAY300/Little-Lemon-Web-Application.git
cd Little-Lemon-Web-Application
```

### 2. Create and activate a virtual environment

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the database

The default configuration uses SQLite for local development.

```bash
python manage.py makemigrations restaurant
python manage.py migrate
```

Create an administrator account if needed:

```bash
python manage.py createsuperuser
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/` | API root |
| GET | `/api/menu/` | List menu items |
| GET | `/api/menu/<id>/` | Retrieve a menu item |
| POST | `/api/menu/` | Create a menu item |
| PUT / PATCH | `/api/menu/<id>/` | Update a menu item |
| DELETE | `/api/menu/<id>/` | Delete a menu item |
| `/` | `/api/bookings/` | Table-booking endpoint |
| POST | `/api/auth/users/` | User registration |
| POST | `/api/auth/token/login/` | Obtain an authentication token |

Authentication requirements depend on the endpoint and its configured permissions.

## MySQL Configuration

For a MySQL setup, create the database and configure the required environment variables using `.env.example` as a reference. Install any required database driver and apply the migrations after configuring the connection.

Do not commit database credentials, secret keys, or your local `.env` file.

## Running Tests

Run the project's Django tests with:

```bash
python manage.py test
```

## Notes

- The Django REST Framework browsable API is available for interactive endpoint exploration.
- SQLite is intended for local development; verify the MySQL configuration separately if required by the assessment rubric.
- Run the application and review the relevant endpoints before submission.

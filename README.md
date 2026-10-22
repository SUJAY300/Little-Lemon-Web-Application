<<<<<<< HEAD
# Little Lemon Back-End Developer Capstone

A Django REST Framework project for the Meta Back-End Developer Capstone. It includes HTML templates, menu CRUD endpoints, table-booking endpoints, token authentication, MySQL configuration, and automated tests.

> This is a starter implementation. Run the setup and tests below, configure your own database, and understand/review the code before submitting it for peer review. Do not claim tests passed until you run them locally.

## Requirements

- Python 3.10+
- pip
- SQLite for quick local development, or MySQL 8+ for the MySQL rubric requirement
- Insomnia (optional, for API testing)

## 1. Create a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 2. Run locally with SQLite

SQLite is the default so you can run the project without a database server:

```bash
python manage.py makemigrations restaurant
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/about/`.

## 3. Configure MySQL

Create a database, for example:

```sql
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Set environment variables in your terminal. Do not commit credentials.

Windows PowerShell example:

```powershell
$env:DB_ENGINE="mysql"
$env:DB_NAME="littlelemon"
$env:DB_USER="your_mysql_user"
$env:DB_PASSWORD="your_mysql_password"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
$env:DJANGO_SECRET_KEY="replace-with-a-long-random-secret"
$env:DJANGO_DEBUG="True"
python manage.py migrate
python manage.py runserver
```

For a real deployment, set `DJANGO_DEBUG=False`, use a strong secret, and configure `DJANGO_ALLOWED_HOSTS`. Do not deploy with the development defaults.

## API endpoints

| Method | Endpoint | Purpose | Access |
|---|---|---|---|
| GET | `/api/menu/` | List menu items | Public |
| POST | `/api/menu/` | Create a menu item | Authenticated |
| GET | `/api/menu/<id>/` | Retrieve one item | Public |
| PUT/PATCH | `/api/menu/<id>/` | Update an item | Authenticated |
| DELETE | `/api/menu/<id>/` | Delete an item | Authenticated |
| GET | `/api/bookings/` | List bookings | Authenticated |
| POST | `/api/bookings/` | Create a booking | Authenticated |
| GET | `/api/bookings/<id>/` | Retrieve a booking | Authenticated |
| PUT/PATCH | `/api/bookings/<id>/` | Update a booking | Authenticated |
| DELETE | `/api/bookings/<id>/` | Delete a booking | Authenticated |
| POST | `/api/auth/users/` | Register a user | Public |
| POST | `/api/auth/token/login/` | Obtain an auth token | Public |
| POST | `/api/auth/token/logout/` | Invalidate token | Authenticated |

### Example menu item

```json
{
  "title": "Greek Salad",
  "price": "12.50",
  "inventory": 20
}
```

### Example booking

```json
{
  "name": "Alex",
  "no_of_guests": 2,
  "booking_date": "2030-04-28T19:00:00+05:30",
  "notes": "Window table"
}
```

## Authentication

Register a user with `POST /api/auth/users/`:

```json
{
  "username": "demo_user",
  "password": "Use-a-strong-password-123"
}
```

Then request a token with `POST /api/auth/token/login/`:

```json
{
  "username": "demo_user",
  "password": "Use-a-strong-password-123"
}
```

Send the returned token in protected requests:

```text
Authorization: Token YOUR_TOKEN_HERE
```

## Insomnia test plan

1. Create a request collection named `Little Lemon Capstone`.
2. `GET http://127.0.0.1:8000/api/menu/` — expect `200 OK`.
3. Register a user at `/api/auth/users/`.
4. Log in at `/api/auth/token/login/` and copy the returned token.
5. Add `Authorization: Token <token>` to protected requests.
6. `POST /api/menu/` with the sample menu JSON — expect `201 Created`.
7. `POST /api/bookings/` with the sample booking JSON — expect `201 Created`.
8. Try creating a menu item without a token — expect `401 Unauthorized` or `403 Forbidden`, depending on authentication negotiation.
9. Capture your own successful responses for your peer-review evidence.

## Run tests

```bash
python manage.py test restaurant
```

Tests use Django's test database. Run them locally and fix any environment-specific issues before submission.

## GitHub submission

Create a new repository under your own GitHub account. From the project folder:

```bash
git init
git add .
git commit -m "Build Little Lemon backend capstone"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Add a `README.txt` at the repository root listing the API paths for peer reviewers, for example:

```text
/api/menu/
/api/menu/1/
/api/bookings/
/api/auth/users/
/api/auth/token/login/
```

Commit and push the README file. Submit your own repository URL in Coursera.

## Rubric checklist

- [ ] Django renders static HTML pages.
- [ ] Project is committed to your Git repository.
- [ ] MySQL connection is configured and verified.
- [ ] Menu and table-booking endpoints work.
- [ ] Registration and token authentication work.
- [ ] Automated tests run successfully.
- [ ] Endpoints have been tested using Insomnia.

## Notes

- This project uses Django REST Framework's browsable API as well as JSON responses.
- Public users can read menu items; write operations require authentication.
- Booking data is hidden from anonymous users.
- The default SQLite mode is intended for quick local setup. Switch to MySQL and verify the connection before claiming the MySQL requirement is complete.
=======
# Little-Lemon-Web-Application
>>>>>>> ec31abf9cb72e6d3a154c23c8032290bacbad53d

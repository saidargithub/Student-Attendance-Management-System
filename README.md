# Student & Attendance Management System (Django + DRF)

A mini-project demonstrating a 3-tier Django architecture (Models, Views, Templates) with integrated Django REST Framework APIs.

## Features
- Student management: add, list, edit, delete
- Attendance management: mark daily attendance, view records, simple report
- Dashboard with totals and present/absent summary per date
- DRF APIs for students and attendance
- Basic authentication: login/logout (use superuser)

## Tech
- Django 5
- Django REST Framework
- SQLite
- Bootstrap 5

## Setup
1. Create and activate virtual environment (Windows PowerShell):
   - `python -m venv venv`
   - `./venv/Scripts/Activate.ps1`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Apply migrations:
   - `python manage.py migrate`
4. Create superuser (non-interactive example):
   - `setx DJANGO_SUPERUSER_USERNAME admin`
   - `setx DJANGO_SUPERUSER_EMAIL admin@example.com`
   - `setx DJANGO_SUPERUSER_PASSWORD adminpass`
   - Restart shell, then: `python manage.py createsuperuser --noinput`
5. Run server:
   - `python manage.py runserver`

Visit `http://127.0.0.1:8000/` and login via the navbar. Default pages:
- Dashboard: `/`
- Students: `/students/`
- Mark Attendance: `/attendance/mark/`
- Records: `/attendance/records/`
- Report: `/attendance/report/`
- Login: `/accounts/login/`

## API Endpoints
- `GET/POST /api/students/`
- `GET/PUT/PATCH/DELETE /api/students/{id}/`
- `GET/POST /api/attendance/`
- `GET/PUT/PATCH/DELETE /api/attendance/{id}/`

### Sample Attendance POST
```json
{
  "student_id": 1,
  "date": "2025-11-14",
  "present": true
}
```

## Folder Structure
- `school/` models, views, serializers, forms, urls
- `templates/` HTML templates (Bootstrap)
- `static/` CSS
- `school_mgmt/` project settings and root URLs

## Screenshots to Capture
Please capture and include these pages for submission:
- Dashboard (with date filter)
- Students list and add/edit form
- Mark Attendance page (with some students checked)
- Attendance Records (filtered by date/class)
- Attendance Report (showing counts)
- Optional: DRF list endpoints in browser (`/api/students/`, `/api/attendance/`)

On Windows, use Snipping Tool or `Win + Shift + S`. Save to a `screenshots/` folder locally and share.

## GitHub Push Instructions
We prepared the repo locally. To push to GitHub:
1. Create a new public repo on GitHub, e.g. `student-attendance-mgmt`.
2. Run:
   - `git remote add origin https://github.com/<YOUR_USERNAME>/student-attendance-mgmt.git`
   - `git branch -M main`
   - `git push -u origin main`

If your environment prompts for credentials, use a GitHub Personal Access Token (PAT) with `repo` scope as the password.

Alternatively, with a PAT set in the environment (PowerShell):
```powershell
$env:GITHUB_TOKEN = "<YOUR_PAT>"
git remote add origin "https://$env:GITHUB_TOKEN@github.com/<YOUR_USERNAME>/student-attendance-mgmt.git"
git push -u origin main
```

## Notes
- Designed for clarity of structure and functionality over completeness.
- You can enhance with charts, class models, pagination, and comprehensive reports.
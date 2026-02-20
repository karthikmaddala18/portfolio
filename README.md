# My Portfolio Website

Hey there! 👋 Welcome to the repository for my personal portfolio website. I built this project to showcase the skills I've learned, particularly in Python, Django, and full-stack development, while pursuing my B.Tech in CSE (AI & ML). 

## What This Project Does
This is a complete, data-driven web application. Rather than just a static HTML page, this site is backed by a PostgreSQL database and a Django admin panel, which means I can actually log in as an administrator to add new projects, update my bio, or manage certifications without ever touching the code again. 

### Key Features I Implemented:
- **Responsive Frontend**: Built with HTML, Tailwind CSS, and some JavaScript. It looks good on both phones and desktops.
- **Dynamic Routing**: Click on any project, and you are taken to a dedicated detail page that uses a custom URL slug generated from the project title (e.g., `/projects/mental-health-simulator/`).
- **Authentication**: I built a complete signup, login, and logout system. Not everyone can see everything—managing projects or viewing dashboard tools is strictly protected (`@login_required`).
- **Contact Form with Real Emails**: The contact page isn't just for show. Submitting a message stores it in the database and uses Django's `send_mail` via SMTP to push a notification directly to me, plus a nicely formatted automated reply back to the sender.
- **Django REST Framework (DRF)**: I added an API layer at `/api/` just to prove I can build endpoints for frontend consumption. It includes Token Authentication and uses ModelSerializers.
- **Dockerized**: If you hate dealing with local environments, I wrote a `Dockerfile` and `docker-compose.yml` so you can spin up the entire app (Django + Postgres) with one command.
- **CI/CD Pipeline**: There's a GitHub Actions workflow in `.github/workflows` that runs my test suite automatically every time I push to `main`. 

---

## How to Run It Locally

If you want to poke around the code, here is how to get it running on your own machine.

### 1. Clone & Setup Virtual Env
```bash
git clone <repository-url>
cd Portfolio/portfolio
python -m venv venv

# Activate it (Windows)
source venv/Scripts/activate 

# Activate it (Mac/Linux)
# source venv/bin/activate    
```

### 2. Install Packages
```bash
pip install -r requirements.txt
```

### 3. Database Stuff
Make sure you have PostgreSQL installed. For this to work out of the box, create a database called `portfolio_db` and make sure your Postgres user is `postgres` with the password `1013` (or just change these in `portfolio/settings.py` to match yours!).

Apply the migrations to create the tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create an Admin User
You'll need an admin account to test out the dashboard and the Django Admin panel:
```bash
python manage.py createsuperuser
```

### 5. Start the Server
```bash
python manage.py runserver
```
Then just open up `http://127.0.0.1:8000/` in your browser!

---

## Running with Docker instead?
If you have Docker Desktop installed, you can skip all of that manual setup. Just run:
```bash
docker-compose up --build
```
This handles Python, the dependencies, and the PostgreSQL database all at once. Once it says the server is running, you can access it at `http://localhost:8000`.

To run migrations inside Docker:
```bash
docker-compose exec web python manage.py migrate
```

---

## API Endpoints
I included a REST API for fun. The projects are public, but modifying them requires a token.
- `GET /api/projects/` -> Lists all projects
- `GET /api/projects/<slug>/` -> Details for a specific project
- `POST /api/contact/` -> Endpoint to submit a contact form (no auth needed)

---

## Tech Stack Summary
- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Frontend:** HTML, Tailwind CSS, Jinja2 Templates
- **DevOps:** Docker, GitHub Actions (CI)
- **Email Delivery:** SMTP (Gmail)

Thanks for checking out my work! Feel free to reach out if you have any questions.

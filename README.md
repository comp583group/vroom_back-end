# Django + PostgreSQL + Docker Starter

This is a starter backend for our app using **Django** + **PostgreSQL** inside **Docker**. You can use this to run the backend and build on top of it with models, APIs, and more.

---

## 🚀 Quick Start

### 1. Clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd django-backend
```

### 2. Start Docker containers
Make sure Docker Desktop is running then:
```bash
docker compose up --build
```
This will start the Django dev server at:

👉 http://localhost:8000


### 3. Contributing
When you pull new code, remember to rebuild with:
```bash
docker compose up --build
```


### 4. Creating Super users
Run command:
```bash
docker compose exec backend python manage.py createsuperuser
```
Then visit: http://localhost:8000/admin
I've added a super user already, lmk if you want the credentials but you can make more

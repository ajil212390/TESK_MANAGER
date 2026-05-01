# Team Task Manager

A robust, full-stack task management application built with Django and Django REST Framework. Role-based access control (Admin vs. Member), and a production-ready architecture designed for seamless deployment with PostgreSQL.

## ✨ Features

- **Role-Based Access Control (RBAC):** 
  - **Admins** can create projects, add members, and assign tasks.
  - **Members** can view their assigned projects, view tasks, and update task statuses (To Do, In Progress, Done).
- **Secure Authentication:** Fully stateless authentication using JSON Web Tokens (JWT).
- **Dynamic Dashboard:** Real-time analytics tracking total, completed, pending, and overdue tasks.
- **Modern UI/UX:** A premium dark-mode aesthetic featuring glassmorphism, smooth animations, and responsive design.
- **Production-Ready:** Pre-configured with `dj-database-url`, `whitenoise`, and `gunicorn` for instant deployment to cloud platforms like Railway.

## 🛠️ Technology Stack

- **Backend:** Python, Django, Django REST Framework (DRF)
- **Database:** SQLite (Local Development) / PostgreSQL (Production)
- **Authentication:** SimpleJWT (JSON Web Tokens)
- **Frontend:** HTML5, Vanilla JavaScript, CSS3 (Custom Glassmorphic Theme)
- **Deployment:** Gunicorn, Whitenoise, Railway

---

## 🚀 Local Development Setup

Follow these steps to run the application on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/team-task-manager.git
cd team-task-manager
```

### 2. Set up a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Create an Admin Account
```bash
python manage.py createsuperuser
```
*(Follow the prompts to set your email and password).*

### 6. Start the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to log in!

---

## 🌍 Live Deployment (Railway + PostgreSQL)

This project is perfectly configured to be deployed on [Railway](https://railway.app/).

1. **Push to GitHub:** Push this complete codebase to a public or private GitHub repository.
2. **Deploy on Railway:**
   - Go to Railway.app and create a new project.
   - Choose **"Deploy from GitHub repo"** and select your repository.
3. **Attach PostgreSQL:**
   - In your Railway project, click **New -> Database -> Add PostgreSQL**.
4. **Link the Database:**
   - Copy the `DATABASE_URL` variable from your new PostgreSQL block.
   - Paste it into the **Variables** tab of your Django App block.
   - *Django will automatically detect this variable and switch from SQLite to PostgreSQL!*
5. **Finalize:**
   - Railway will automatically run the database migrations (thanks to the included `Procfile`).
   - Go to the **Settings** tab of your Django app and click **Generate Domain** to get your live public URL.

### Creating a Live Admin
Once deployed, you will need to create an admin account on the live PostgreSQL database.
1. Open your Railway dashboard.
2. Click on your Django App block.
3. Go to the **Terminal** tab.
4. Run: `python manage.py createsuperuser` and follow the prompts.

---

## 📝 License
This project is open-source and available under the MIT License.

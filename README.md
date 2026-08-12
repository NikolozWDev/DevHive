# TheDevHive 🐝 by Nikoloz Gigiashvili

Live Website 👉 [thedevhive.onrender.com](https://thedevhive.onrender.com)
Note: This site is hosted on Render’s free tier, so the first load may feel slow. Registration/Login is disabled for public users as this project.

## Overview

**DevHive** is a full-stack Django-based web application where users can sign up, create discussion rooms, interact with others, and share knowledge on different topics.  

## Gallery

<p align="center">
  <img src="readme_images/Screenshot 2025-11-21 205734.png" width="280" />
  <img src="readme_images/Screenshot 2025-11-21 210424.png" width="280" />
  <img src="readme_images/Screenshot 2025-11-21 210450.png" width="280" />
</p>

---

## Features ✨

- 🔐 User authentication (Register/Login/Logout/Delete)
- 🧑‍💼 Custom user profiles with avatar upload
- 🧵 Create, update, and delete discussion rooms
- 💬 Add and delete messages inside rooms
- 🔍 Search by topic or username
- 🧭 Follow/Unfollow users
- 🌙 Light/Dark mode toggle
- 📄 Custom 404 error page
- 📸 Media handling for profile images (via Pillow)

---

## Tech Stack 🛠️

- **Backend:** Django 5.2, Django REST Framework  
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite3 (local)  
- **Deployment:** Render.com  
- **Media Handling:** Pillow  
- **Static Files:** WhiteNoise  

---

## Purpose & Learning Goals 🎯

- Apply full-stack web development skills in a practical project
- Gain experience in deploying real-world Django apps
- Build a strong portfolio project to demonstrate my abilities
- Deepen my understanding of Django architecture and modular coding

---

## Getting Started 🚀

To run this project locally:

```bash
git clone https://github.com/NikolozWDev/DevHive.git
cd DevHive
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

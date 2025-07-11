📚 Library System with API
A full-stack Library Management System built with Django and Django REST Framework,
split into two separate Django projects for a clear separation of frontend and backend responsibilities.

# From Book_frontend/
python manage.py runserver 8000

# From hehe-api/
python manage.py runserver 8001
Make sure the API URLs in Book_frontend are
pointing correctly to http://127.0.0.1:8001/ where hehe-api is running.
________________________________________



📁 Project Structure
library-system-with-api/
│
├── Book_frontend/ # Frontend Django project
│   ├── adminapp/  # Admin functionalities
                    (view/add/update/delete books)
│   └── userapp/   # User functionalities
                  (register, login, view, download books)
│
├── hehe-api/  # Backend Django project
│   └── backendapi/ # Handles API logic and communication
│
└── README.md  # Project documentation
________________________________________



🚀 Features
🔐 Admin Side (adminapp)
•	Login with Django superuser authentication
•	Add, update, delete, and view books
•	Integrated with Django REST Framework to provide APIs for book operations
👤 User Side (userapp)
•	Register & login using Django custom authentication system
•	View books added by admin
•	Download books/files
•	Search books by title
•	Sort books by title or upload date
🔗 API Layer (hehe-api)
•	Built with Django REST Framework
•	Handles API communication between Book_frontend and hehe-api
•	Clean separation of concerns: logic in hehe-api, presentation in Book_frontend


________________________________________



⚙️ Technologies Used
•	Python 3
•	Django 5.x
•	Django REST Framework
•	SQLite (Two separate databases: one for each Django project)
•	HTML, CSS (via Django templates)
•	Bootstrap / Tailwind (if used in frontend templates)


________________________________________


🗃️ Database
•	Two separate SQLite databases:
o	Book_frontend for managing frontend user/admin auth and models
o	hehe-api for handling API logic and models


________________________________________



🔧 Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/library-system-with-api.git
cd library-system-with-api
2. Set up virtual environments for both projects
# Frontend (Book_frontend)
cd Book_frontend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Do the same for hehe-api project
cd ../hehe-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Run migrations
# Inside each project directory
python manage.py makemigrations
python manage.py migrate
4. Create Superuser for adminapp
python manage.py createsuperuser
5. Run servers
# From Book_frontend/
python manage.py runserver 8000

# From hehe-api/
python manage.py runserver 8001
Make sure the API URLs in Book_frontend are pointing correctly to http://127.0.0.1:8001/ where hehe-api is running.
________________________________________
🧪 API Endpoints (Sample)
Endpoint	Method	Description
/api/books/	GET	List all books
/api/books/<id>/	PUT	Update a book (admin only)
/api/books/<id>/delete/	DELETE	Delete a book (admin only)
/api/user/register/	POST	Register new user
/api/user/login/	POST	Login user and get token
(Update the table based on your actual endpoints)
________________________________________
📦 Download Feature
•	Books/files uploaded by admin can be downloaded by users.
•	Secure access and media file handling using Django settings.
________________________________________

﻿# Library Management System

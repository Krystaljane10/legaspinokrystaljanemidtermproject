# Django CRUD Project

## Project: Django CRUD Application

### Duration: 2 Weeks

### Objective: 
Build a Django-based CRUD application for managing tasks with specific business logic.

## Step-by-Step Guide to Create the Project

### Step 1: Install Prerequisites

Before you start, ensure you have the following installed on your machine:

- **Python 3.x**: Download and install from [python.org](https://www.python.org/downloads/).
- **pip**: Comes with Python, but you can upgrade it using:
  ```bash
  python -m pip install --upgrade pip
MySQL (or another database of your choice): Install MySQL from mysql.com or use a GUI tool like XAMPP.

### Step 2: Create a Django Project
Open your terminal or command prompt.
Install Django:   pipenv install django
Create a new Django project:   django-admin startproject task_manager
cd task_manager

### Step 3: Create a Django App
Create a new app named tasks:   python manage.py startapp tasks

### Step 4: Define the Task Model
Open tasks/models.py and define the Task model.

### Step 5: Register the App
Open task_manager/settings.py and add the tasks app to the INSTALLED_APPS list

### Step 6: Apply Migrations
Run the following commands to create the database tables:

python manage.py makemigrations
python manage.py migrate

### Step 7: Implement CRUD Functionality
Create views in tasks/views.py.

### Step 8: Define URLs
Create a urls.py file in the tasks directory and define the URL patterns.

### Step 9: Create Basic Templates
Create a directory for templates.

### Step 10: Add Basic Styling
Use Bootstrap: The templates provided above already include Bootstrap for styling. You can further customize the styles by adding your own CSS if desired.

### Step 11: Run the Application
**Run the Django development.

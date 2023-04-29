# **Blog Project**

This is a blog project developed using <a href="https://docs.djangoproject.com/en/4.2/topics/install/">**Django**</a> framework with <a href="https://www.python.org/downloads/">**Python 3.10**</a>. The main purpose of this project is to provide a platform to publish blog posts and share them with other users.

## **Features**

- User authentication and authorization.
- CRUD operations for blog posts.
- Search functionality.
- Pagination.

## **Installation**

1. Clone the repository:

- `git clone https://github.com/<your-username>/blog.git`

2. Create a virtual environment:

- `python3 -m venv env`

3. Activate the virtual environment:

- `source env/bin/activate`

4. Install the requirements:

- `pip install -r requirements.txt`

5. Apply the migrations:

- `python manage.py migrate`

6. Create a superuser:

- `python manage.py createsuperuser`

7. Run the development server:

- `python manage.py runserver`

8. Access the application on your browser at http://localhost:8000.
(This is an example)

**NOTE:** that the database file: **(db.sqlite3)** is not included in this repository. You can add some data for after running the application and at the same time be able to see the functionality of the blog.

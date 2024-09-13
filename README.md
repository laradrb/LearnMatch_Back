# Learn Match

## Description  

Full-stack web application called LearnMatch which aims to connect students with tutors based on their specific needs and expertise. The system allows students to manage their profiles, specify their learning needs, get matched with suitable tutors and schedule online tutoring sessions. In addition, it will provide a chat functionality to continue communication after the session and clarify queries or reschedule classes or even interact with other students.

### Features

Registration and Login: Students can create an account or log in to access to their personalized features.
Courses: Students can search for courses of their degree.
Level: Students can select which level they want according to their needs and knowlegde.
Time: Students can select which hour suits them most.
Calendar: Students can select day and time of their online tutoring session.


### Workflow

[Workflow](#) *(https://drive.google.com/file/d/1gnHWIisb7rYc0WSFFRhB9nOlEkQ-RY08/view?usp=sharing)*


### Technologies

- [Python]
- [Django]
- [Django REST Framework]
- [PostgreSQL]
- [psycopg2]
- [pillow]

## Installation

1. Open terminal
2. git clone https://github.com/laradrb/LearnMatch_Back
3. Create and activate virtual environment:

    python -m venv env
    source venv/bin/activate  

4. Install requirements:

pip install -r requirements.txt

5. Set up your database in PostgreSQL and complete settings.py

6. Make migrations and run server:

python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
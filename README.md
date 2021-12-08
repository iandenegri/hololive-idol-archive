# Virtual Singer Archive Project
Welcome to the source code for the Virtual Singer Archive Project (vSAP)! The goal for vSAP is so that there is a way for people to find out more about various vTuber's musical endeavors.

## Getting started:
- Pull project
- Have python
- Make a venv folder alongside this project's folder
- Start virtual environment
- CD into project folder
- Run these commands
  - `pip install -r requirements.txt`
  - `python manage.py migrate`
  - `python manage.py createsuperuser` (You'll need this to log into the Django admin panel)
- Do things.

## Todo:
- Search view needs to be added so the search bar in the nav does something
- Overhaul the UI
- Add a job that populates a new vtuber's profile with appropriate videos
- Add a job that populates an existing vtuber's profile with appropriate videos that were uploaded in the past day
- Add a job that checks the number of views a video has gotten in the past day, week, month, etc.
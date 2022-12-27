# Cyber-Security-Project1

This project is developed for Cyber Security Base 2022's first project [assignment](https://cybersecuritybase.mooc.fi/module-3.1).

## Dependencies

This project uses python3 and django. See the [installaion instructions](https://cybersecuritybase.mooc.fi/installation-guide).

## Installation and database initialization

Clone the repository: `git clone git@github.com:TanakaAkihiro/Cyber-Security-Project1.git`

In the directory `mysite`, create the database tables for the models by running: `python3 manage.py makemigrations` and `python3 manage.py migrate`

Initialize database by running: `python3 init_database.py`

Run the local server: `python3 manage.py runserver`

Application is running at http://127.0.0.1:8000/simplebank

## Users created by init_database.py

admin:
  username: `admin`
  password: `CyberSecurity22`

bob:
  username: `bob`
  password: `squarepants`

alice:
  username: `alice`
  password: `redqueen`

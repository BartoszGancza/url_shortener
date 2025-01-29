# Basic URL Shortener

Database choice was made because SQLite is easily supported without any additional work and 
dependencies by Django.

Lack of authentication is done on purpose, as URL shortening services usually do not require a user
account to use them (unless they include additional paid services).

## Application startup

There are two options to run this application, using Docker, and running it directly on local machine.
In both cases first rename the `.env_example` file to `.env` and change desired variables (mainly `SECRET_KEY`).

### Docker
To use Docker simply run:
```bash
docker-compose up
```
from the root of the project.

### Local machine
To run the application directly, make sure you have your virtualenv active and install all dependencies:
```bash
pip install -r requirements.txt
```
then create the SQLite database and run migrations by running:
```bash
python manage.py migrate
```
and then start the server by running:
```bash
python manage.py runserver
```
from the root of the project (make sure you have all environment variables from the `.env` file
active by running for example `export $(cat .env | xargs) && env`).

You can now access the application at `http://localhost:8000`.

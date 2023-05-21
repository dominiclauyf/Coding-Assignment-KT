# Django Server
## Development Docker Quick Start

You need to have Docker and Docker Compose. Git clone this project and enter its root directory, then run the following:
```bash
cp dev-example.env .env
docker-compose up

# Open a new terminal
docker exec -it [django container name|coding-assignment-kt-django-1] bash
pipenv run ./manage.py makemigrations
pipenv run ./manage.py migrate
```
You may need to run `docker-compose` with `sudo` if your user account does not have permission to use Docker directly.

### To access all the page
Currently there is no login and logout page, use django admin page to login.

Do notice that there is dummy data created on migrations.

Dummy superuser:
- Username: superuser
- Pass: same as above
---
## Pre-commit setup

1. Install pre-commit
```
pip install pre-commit
```
2. Setup pre-commit in git repo
```
pre-commit install
```
3. Run pre-commit in all file (optional)
```
pre-commit run --all-files
```

##### Reference
- [Pre-commit Install](https://pre-commit.com/#install)

---
## Reference
### To create superuser
```bash
docker exec -it [container name] bash
pipenv run ./manage.py createsuperuser
```

### Oauth setup for other application
The application is using oauth methonology to login, so u will need register the application

#### Step
1. Login into django admin using superuser
2. Access to http://localhost:8000/o/applications/
3. Click on the link to create a new application and fill the form with the following data:
    - Name: just a name of your choice
    - Client Type: confidential
    - Authorization Grant Type: Resource owner password-based
4. Record down Client ID and Client Secret

# NOTE: This Dockerfile is meant for development use, not for production
FROM python:3.10

WORKDIR /main

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

COPY Pipfile Pipfile.lock .
RUN pipenv sync --dev

EXPOSE 8000
# Run it!
CMD ["pipenv", "run", "./manage.py", "runserver", "[::]:8000"]

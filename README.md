# Django Authentication API

A simple authentication REST API built with Django, Django REST Framework, PostgreSQL, and Docker.

## Tech Stack

- Python 3.14
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- Docker and Docker Compose


## Setup Instructions

### Clone Repository

https://github.com/darwindc12/auth-api.git

### Run with Docker(Recommended)
#### Build Containers: docker-compose build
#### Start Services: docker-compose up
#### Run Migrations: docker-compose exec web python manage.py migrate
#### API will be available at: http://localhost:8000/

## Database Configuration
### PostgreSQL runs in Docker with:
#### Database: authdb
#### User: authuser
#### Password: authpassword
#### Host : db
#### Port: 5432

## Authentication Endpoints

#### Base URL: /api/auth
#### Register: POST /api/auth/register/
#### Login(Get Tokens): POST /api/auth/login/
#### Refresh Token: POST /api/auth/refresh/

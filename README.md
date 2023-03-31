# FastAPI Social Media App

A social media web application built with FastAPI, PostgreSQL and *soon* Jinja2 Templates. This project is intended to demonstrate how to build a full-stack web application using modern web technologies.

## Features

- It allows to create, delete and update a post
- It retrieves all of the available posts or just one by using an ID
- User registration
- Schemas implemented to validate input and output data
- Users cannot update nor delete posts that do not own
- Users can vote posts: Add and delete votes to a post
- User authentication and authorization using JWT tokens.

Language: Python v3.11.1

## Tech stack

1. Backend: FastAPI v0.92.0 FastAPI - Python web framework.
2. Fronted: Jinja2 Templates will be implemented in order to build a frontend
3. Testing: pytest v7.2.2 (fixtures, parametrization and HTML/CSS report)
4. Containerization: Docker v20.10.23
5. Alembic: v1.10.2
6. Postman: v10.12.7 Collections and environment variables provided at [postman](https://github.com/mvarrone/fastapi-social-media-app/tree/main/postman) folder on this repository
7. Database: PostgreSQL v15.2
8. Models: SQLAlchemy v1.4.23
9. Security:
    - JWT and OAuth2 implementation
    - Hashed passwords in database using passlib v1.7.4
10. CI/CD: Implemented using GitHub Actions
    - Build: 
        - Pull repo
        - Install python 3
        - Upgrade pip
        - Install all dependencies
        - Test
        - Docker: Login to Docker Hub, build, push and digest the image

    - Deploy:
        - Deploy to a Ubuntu server on Digital Ocean

## Getting started: Without Docker

a) Clone repository into your machine

```md
git clone https://github.com/mvarrone/fastapi-social-media-app.git
cd fastapi-social-media-app
```

b) Create a virtual environment

<details>
<summary>On Windows</summary>
1.Creating a virtual environment

```md
python -m venv venv
```

2.Activating it

a) Using CMD

```md
.\venv\Scripts\activate.bat
```

b) Using PowerShell

```md
.\venv\Scripts\Activate.ps1
```

3.Installing dependencies

```md
pip install -r requirements.txt
```

4.(OPTIONAL) Deactivating the virtual environment

```md
deactivate
```
</details>

<details>
<summary>On Linux/Mac</summary>
1. Creating a virtual environment

```md
python3 -m venv venv
```

2.Activating it

```md
source venv/bin/activate
```

3.Installing dependencies

```md
pip install -r requirements.txt
```

4.(OPTIONAL) Deactivating the virtual environment

```md
deactivate
```
</details>

c) Run app

```md
uvicorn app.main:app --host 0.0.0.0 --port 8000 
```

## Getting started: With Docker
a) Clone repository

```md
git clone https://github.com/mvarrone/fastapi-social-media-app.git
cd fastapi-social-media-app
```

b) Start
```md
docker compose -f .\docker-compose-dev.yml up -d
```

b) Stop
```md
docker compose -f .\docker-compose-dev.yml down
```

## Documentation
1. Swagger UI

    ```linux
    http://localhost:8000/docs
    ```
2. Redocly

    ```linux
    http://localhost:8000/redoc
    ```

> Note 1: Credentials for documentation

I have added some security level to the documentation. For that, both cases require the following credentials to be used:
- Username: admin
- Password: pass

    Stored at the .env file

> Note 2: About .env file

A ```.env``` file has been provided to facilitate the implementation and testing of this project. The reason to include this file is that it is a publicly available project on the Internet

> Note 3: About this project

Project learnt from [fastapi-course](https://github.com/Sanjeev-Thiyagarajan/fastapi-course) by Sanjeev Thiyagarajan

## Next improvements

    1) Implement a simple frontend using Jinja2 Templates
    2) Finish deploy to Digital Ocean
    3) Postman:
        - Create one example for each request
        - Create Tests for each request (based on status code)
        - Implement a Postman Flow
        - Export collection data
        - Export environment data
    4) Implement roles: admin and user
    5) Add documentation credentials to a db or json file (implement a hashed password)

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 file for details.
## Social media app

Description to be added

Language: Python v3.11.1

### Requirements
1. Backend: FastAPI v0.92.0
2. Fronted: Jinja2 templates will be implemented in order to build a frontend
3. Testing: pytest v7.2.2
4. Containerization: Docker v20.10.23
5. Alembic: v1.10.2
6. Postman: v10.12.4 Collections and environment variables provided at [postman](https://github.com/mvarrone/fastapi-social-media-app/tree/main/postman) folder on this repository
7. Database: PostgreSQL v15.2
8. Models: SQLAlchemy v1.4.23
9. Security:
    - JWT and OAuth2 implementation
    - Hashed passwords in database using passlib v1.7.4
10. CI/CD: GitHub Actions

### Documentation
1. Swagger UI:

    ```linux
    http://localhost:8000/docs
    ```
2. Redocly:

    ```linux
    http://localhost:8000/redoc
    ```

Note 1: I have added some security level to the documentation. For that, both cases require the following credentials to be used:
- Username: admin
- Password: pass

Note 2: Project learnt from [fastapi-course](https://github.com/Sanjeev-Thiyagarajan/fastapi-course) by Sanjeev Thiyagarajan

Note 3: A ```.env``` file has been provided to facilitate the implementation and testing of this project. The reason to include this file is that it is a publicly available project on the Internet
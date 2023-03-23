## Social media app

Backend that allows to implement a CRUD in order to create a social media app

- It allows to create, delete and update a post
- It retrieves all of the available posts or just one by using an ID
- Of course, it is possible to create users
- Schemas implemented to validate input and output data
- Users cannot update nor delete posts that do not own
- Users can vote posts: Add and delete votes to a post

Language: Python v3.11.1

### Tech used
1. Backend: FastAPI v0.92.0
2. Fronted: Jinja2 templates will be implemented in order to build a frontend
3. Testing: pytest v7.2.2 (fixtures, parametrization and HTML/CSS report)
4. Containerization: Docker v20.10.23
5. Alembic: v1.10.2
6. Postman: v10.12.4 Collections and environment variables provided at [postman](https://github.com/mvarrone/fastapi-social-media-app/tree/main/postman) folder on this repository
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

Stored at the .env file

Note 2: A ```.env``` file has been provided to facilitate the implementation and testing of this project. The reason to include this file is that it is a publicly available project on the Internet

Note 3: Project learnt from [fastapi-course](https://github.com/Sanjeev-Thiyagarajan/fastapi-course) by Sanjeev Thiyagarajan

### Isolation

1. Create a virtual environment
    ```linux
    python -m venv venv
    ```
2. Activate it

    On Windows using PowerShell
    ```linux
    .\venv\Scripts\Activate.ps1
    ```
3. Install dependencies
    ```linux
    pip install -r .\requirements.txt
    ```
4. Start API
    ```linux
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```
    Use browser:

    http://localhost:8000/

    http://localhost:8000/docs
5. Deactivate the virtual environment when no longer needed
    ```linux
    deactivate
    ```
### Next steps:

    1) Implement a simple frontend using Jinja2 templates
    2) Finish deploy to Digital Ocean
    3) Postman:
        - Create one example for each request
        - Create Tests for each request (based on status code)
        - Implement a Postman Flow
        - Export collection data
        - Export environment data
    4) Implement roles: admin and user
    5) Add documentation credentials to a db or json file (implement a hashed password)

<!-- create tabs using HTML -->
<div class="tab">
  <button class="tablinks" onclick="openTab(event, 'Windows')">Windows</button>
  <button class="tablinks" onclick="openTab(event, 'Linux')">Linux</button>
  <button class="tablinks" onclick="openTab(event, 'Mac')">Mac</button>
</div>

<!-- create divs for each tab content -->
<div id="Windows" class="tabcontent">
  <h3>Windows</h3>
  <p>This is the Windows tab content.</p>
</div>

<div id="Linux" class="tabcontent">
  <h3>Linux</h3>
  <p>This is the Linux tab content.</p>
</div>

<div id="Mac" class="tabcontent">
  <h3>Mac</h3>
  <p>This is the Mac tab content.</p>
</div>

<!-- add CSS to style the tabs -->
<style>
  .tab {
    overflow: hidden;
    border: 1px solid #ccc;
    background-color: #f1f1f1;
  }

  .tab button {
    background-color: inherit;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    transition: 0.3s;
    font-size: 17px;
  }

  .tab button:hover {
    background-color: #ddd;
  }

  .tab button.active {
    background-color: #ccc;
  }

  .tabcontent {
    display: none;
    padding: 6px 12px;
    border: 1px solid #ccc;
    border-top: none;
  }
</style>

<!-- add JavaScript to control the tabs -->
<script>
  function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }

  document.getElementById("defaultOpen").click();
</script>

# Codeleap-backend
## Topics Covered
- Run the Django CRUD API Locally
- Run a React.js App with the Django API
- Setup Django
- Create the Django Models
    - Database Model
    - Model Serializer
- Create the CRUD API Views in Django
    - GET and POST API Views
    - GET, PATCH, and DELETE API Views
- Add the CRUD Routes
    - Add the CRUD API URLs
    - Add the Base URL of the CRUD App to the Project
- Setup CORS in Django
- Create the Migration File and Start the Server
- Test the Django CRUD API
    - Create Note
    - Update Note
    - Get All Notes
    - Delete Note
- Create Documentation for the CRUD API


## How to start the project

1 - Add .env file in root project

2 - Create local venv 

- Windows OS

```cmdlet
 python -m venv venv
```

- Mac or Linux OS
```cmdlet
 python3 -m venv venv
```

3 - Run python locally
- Windows OS (Command Prompt )

```cmdlet
 venv\Scripts\activate.bat
```

- Windows OS (Git Bash)
```cmdlet
 venv/Scripts/activate.bat
```

- Mac or Linux OS
```cmdlet
 source venv/bin/activate
```

4 - Run pip install -r requirements.txt to install all the required modules
```cmdlet
 pip install -r requirements.txt
```

5 - I'm using postgres in this project. Create a database and schema. In my case, all info is postgres, and schema is postgres

6 -After that, migrate the database schema to the SQLite database with python manage.py migrate
```cmdlet
 python manage.py migrate
```

7 - Start the Django development server by running
```cmdlet
 python manage.py runserver
```

8 - Test the API endpoints from an API testing tool Postman
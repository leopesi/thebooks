# Responsive API

### Responsive Fullstack CRUD System
#### Features
✅Login System<br>
✅Responsive Template<br>
✅Docker build<br>
✅API REST Integrated<br>
✅API Unit Test<br>
✅Bootstrap4 Template Integration<br>
✅Anti-CSRF Security<br>
✅PostgreSQL<br>
✅Django ORM<br>
✅Session Auth<br>
✅Books List<br>
✅Authors List<br>
✅Read Only mode for non-authenticated Users<br>
✅OOP Code Based<br>
✅Django-admin Interface<br>


## Port
```
Default port is 8000, but can be changed on server run (Description below).
```

## How to use

## - Run project with Docker

### Clone the repository
```
git clone https://github.com/leopesi/thebooks.git
```

### Enter the project folder
```
cd path/of/project
```

### Create and run docker containers
```
docker compose up --build
```



## PostgreSQL Configuration
### With postgreSQL installed in your local machine, add the code bellow in your local_settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'HOST': 'db_host',
        'PORT': 'db_port',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
    }
}
```

### Change the fields db_name, db_host, db_port, db_user and db_password accordingly
example:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'HOST': 'localhost'
        'PORT': '5432',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
    }
}
```

### Don't forget to created a new db in your postgreSQL with the same name of your DB_NAME local_settings value

### With your terminal in the project root folder, run the following command:
```
python manage.py migrate # This will create the required tables inside your postgre database.
```

## Running the server
### Again in the project root folder, run the server with the command:
```
python manage.py runserver
```
### If you want to use a port other than 8000, run the command like this:
```
python manage.py runserver 127.0.0.1:desired_port
```

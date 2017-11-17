# Python Django Rest API back end sample application 
Built this application using DjanoRESTframework<br />
Application has CRUD Operation on Mysql User tables via Http REST API<br /> 

# prerequisites 
1. Python2.7 or Python3
2. Mysql Server 5.5 or later 
3. virtualenv 


# Project Setup 
Once the prerequisites are installed, checkout the project and create a virtual envoriment under the project 
```
virtualenv venv
```
```
source venv/bin/activate
```

Install django using the following command 
```
pip install django==1.11.7(Latest version)
```
```
pip install djangorestframework
```

Create below schema in MySQL 
``` 
create database instawork_test;
```
```
use instawork_test;
```
```
create table users(ID int NOT NULL AUTO_INCREMENT,FirstName varchar(255) NOT NULL,LastName varchar(255),Phone int(11),Email varchar(255),Role enum(‘admin’,’regular’),PRIMARY KEY (ID)); 
```
Django settings is already modified to connect to this database, please modify the DB user,password,port and hostname for the below section in setting.py under backend_test folder. <br /><br />
DATABASES = {<br />
    'default': {<br />
        'ENGINE': 'django.db.backends.mysql',<br />
        'NAME': 'instawork_test',<br />
        'USER': 'root', # change the username to DB username<br />
        'PASSWORD': 'test123', # change the password to DB password<br />
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on<br />
        'PORT': '3306', # Change the port to mysql server running port<br />
    }<br />
}<br />

Install MySQL client for Django to connect MySQL Database
``` 
pip install MySQL-python 
```

Test the connection using the below command from backend_test folder.
```
python manage.py inspectdb 
```
The output would look like something as below<br />
from __future__ import unicode_literals<br />

from django.db import models<br />


class Users(models.Model):<br />
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.<br />
    firstname = models.CharField(db_column='FIRSTNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.<br />
    lastname = models.CharField(db_column='LASTNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.<br />
    phone = models.IntegerField(db_column='PHONE', blank=True, null=True)  # Field name made lowercase.<br />
    email = models.CharField(db_column='EMAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.<br />
    role = models.CharField(db_column='ROLE', max_length=7, blank=True, null=True)  # Field name made lowercase.<br />

    
Run the server if above command is sucessfull from backend_test folder. Below is the command to start the server 
```
python manage.py runserver
```
Below is the output for successful server launch<br />
Performing system checks...<br />

System check identified no issues (0 silenced).<br />
November 17, 2017 - 06:45:35<br />
Django version 1.11.7, using settings 'backend_test.settings'<br />
Starting development server at http://127.0.0.1:8000/<br />
Quit the server with CONTROL-C.<br />



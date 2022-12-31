# HR-Management-System

## Installation:
1. `git clone 'RepoLink'`


2. `pip install -r requirements.txt`


3. `cd hrms`


4. `python manage.py makemigrations`


5. * Comment out django.contrib.admin in INSTALLED_APPS settings:

    `INSTALLED_APPS = [
       ...
       #'django.contrib.admin',
       ...
    ]`

   * Comment out admin path in urls.py

       `urlpatterns = [
          ...
          #path('admin/', admin.site.urls) 
          ...
       ]`
   * run:  
    `python manage.py migrate`
   * when done, **Uncomment all back**


6. `python manage.py createsuperuser`


7. `python manage.py runserver`

## Api Endpoints:
Please visit url: 'http://127.0.0.1:8000/api/swagger/schema/'

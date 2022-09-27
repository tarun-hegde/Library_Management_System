# authenticationdjango
APP_NAME=LIBRARY  
***INSTRUCTIONS TO START PROJECT FROM SCRATCH***  
```python
django-admin startproject library
./venv/Scripts/activate
pip install django 
cd library 
python manage.py startapp catalog
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
[REFERENCES](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)  
Don't forget to register `catalog` in settings.py

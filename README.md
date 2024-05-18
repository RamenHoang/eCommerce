## To Run This Project
1. create a virtual environment inside eCommerce folder,
```
python3 -m venv venv
```
2. activate virtual environment

for windows
```
.\venv\Scripts\activate 
```
for macOS/linux
```
source venv/bin/activate
```
3. install project dependencies from requirements.txt,
```
pip install -r requirements.txt
```
4. update database setting
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eCommerce',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3320'
    }
}
```
5. run migrations
```
python manage.py migrate
```
6. create superuser
```
python manage.py createsuperuser
```
7. run project on your local machine,
```
python manage.py runserver
```
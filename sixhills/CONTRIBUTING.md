# CONTRIBUTING

## PC
cd C:\__Projects\todowoo-project

.venv\Scripts\activate

django-admin startproject todowoo
python manage.py startapp todo

### Todo
cd C:\__Projects\todowoo-project
python manage.py runserver

python manage.py makemigrations
python manage.py migrate

 ## iOS
source .venv/bin/activate  

## requirements.txt
pip freeze > requirements.txt

pip install -r requirements.txt

## python anywhere
git clone https://github.com/TimothyJNeale/todowoo-project.git 
mkvirtualenv --python=/usr/bin/python3.9 todovenv

cd .virtualenvironments/
workon todovenv
deactivate

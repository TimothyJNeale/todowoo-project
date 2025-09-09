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
workon todowoovenv
deactivate

# Workflow from PC to Python Anywhere

## PC
### Update requirements
cd C:\__Projects\todowoo-project
.venv\Scripts\activate
pip freeze > requirements.txt

### Commit any changes and upload to github
git staus
git add .
git commit -m "Latest changes"
git push

## Python Anywhere bash console
### Activate virtual environment
cd todowoo-project/
workon todowoovenv

### Download from Github
git status
git fetch
git status

#### if required
git pull
pip install -r requirements.txt

### Now the Django specific stuff
python manage.py migrate
python manage.py collectstatic

## Python Anywhere web app page
https://www.pythonanywhere.com/user/TimothyNeale/webapps/#tab_id_timothyneale_pythonanywhere_com

Reload the app

https://timothyneale.pythonanywhere.com/
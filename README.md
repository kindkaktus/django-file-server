Django  file server
==================================

Minimalistic password-protected file server powered by Django.

The project contains source code from [Django file upload example at https://github.com/axelpale/minimal-django-file-upload-example] and [Authentication to Django websites https://github.com/narenaryan/django-auth-pattern]

Production setup serves behind nginx + gunicorn.


Django 1.11 is supported. Tested on Ubuntu 16.04 and Python 2.7


Initial setup:
------------------
    sudo apt-get -y install python-pip nginx
    git clone https://github.com/kindkaktus/django-file-server
    cd django-file-server
    sudo pip install --upgrade pip
    sudo pip install -r requirements.txt
    sudo install -d -o www-data -g www-data /var/lib/django-file-server /var/run/django-file-server /var/log/django-file-server
    sudo -u www-data ./manage.py migrate
    sudo -u www-data ./manage.py createsuperuser

To run development server:
------------------
    sudo ./manage.py runserver 0.0.0.0:80  --settings=django_file_server.settings_devel

Finally, setup production server (nginx -> gunicorn -> django app):
------------------
   sudo ./install.sh

Checks:
------------------
    ./manage.py check --deploy


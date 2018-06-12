Django  file server
==================================

Minimalistic password-protected file server powered by Django.

The project contains source code from [Django file upload example at https://github.com/axelpale/minimal-django-file-upload-example] and [Authentication to Django websites https://github.com/narenaryan/django-auth-pattern]

Production setup serves behind nginx + gunicorn.


Django 2 is supported. Tested on Ubuntu 16.04 with Django 2.0, nginx 1.10.3 and Python 3.5


Production setup (nginx -> gunicorn -> django app):
------------------

Install packages

    # sudo apt-get -y install nginx git
    # sudo apt-get -y remove apache2
    # curl https://bootstrap.pypa.io/get-pip.py | sudo python3

Install django file server

    # git clone https://github.com/kindkaktus/django-file-server
    # cd django-file-server
    # sudo pip3 install -r requirements.txt
    # sudo  ./install.sh

Copy your SSL certificate and key to `/etc/nginx/ssl-cert.pem` and `/etc/nginx/ssl-key.pem` and restart nginx

Checks:
------------------

    $ sudo -u www-data ./manage.py check --deploy


Tests:
------------------
    $ ./setup_test.sh
    $ ./manage.py test --settings=django_file_server.settings_test


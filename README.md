Django  file server
==================================

Minimalistic password-protected file server powered by Django.

The project contains source code from [Django file upload example at https://github.com/axelpale/minimal-django-file-upload-example] and [Authentication to Django websites https://github.com/narenaryan/django-auth-pattern]

Production setup serves behind nginx + gunicorn.


Django 2 is supported. Tested on Ubuntu 16.04 with Django 2.0, nginx 1.10.3 and Python 3.5


Production setup (nginx -> gunicorn -> django app):
------------------

Become root

    $ sudo -i

Install packages

    # apt-get -y install nginx git
    # apt-get -y remove apache2
    # curl https://bootstrap.pypa.io/get-pip.py | sudo python3

Install django file server

    # git clone https://github.com/kindkaktus/django-file-server /srv/django-file-server
    # cd /srv/django-file-server
    # pip3 install -r requirements.txt
    # install -d -o www-data -g www-data /var/lib/django-file-server /var/log/django-file-server
    # sudo -u www-data ./manage.py migrate
    # sudo -u www-data ./manage.py createsuperuser

Crank it up

    # ./install.sh

Copy your SSL certificate and key to `/etc/nginx/ssl-cert.pem` and `/etc/nginx/ssl-key.pem` and restart nginx

Checks:
------------------

    $ sudo -u www-data ./manage.py check --deploy


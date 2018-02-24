#!/bin/bash
set -e

setup_gunicorn() {
    sudo ln -snf $(pwd) /srv/django-file-server
    install -d -o www-data -g www-data /srv/django-file-server/media /srv/django-file-server/static /var/log/django-file-server
    cp -f systemd/gunicorn.service /etc/systemd/system/
    systemctl daemon-reload
    systemctl restart gunicorn
    systemctl enable gunicorn
    if [ ! -S /srv/django-file-server/django-file-server.sock ]
    then
        echo "django-file-server.sock does not exist" >&2
        exit 1
    fi
}

setup_nginx() {
    ./manage.py collectstatic --clear --no-input
    rm -f /etc/nginx/sites-enabled/default
    cp -f nginx/django-file-server /etc/nginx/sites-available/
    ln -sf /etc/nginx/sites-available/django-file-server /etc/nginx/sites-enabled
    systemctl restart nginx
}

setup_gunicorn
setup_nginx
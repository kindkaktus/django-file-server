#!/bin/bash
set -e

setup_gunicorn() {
    ln -snf $(pwd) /srv/django-file-server
    cp -f systemd/gunicorn.service /etc/systemd/system/
    install -d -o www-data -g www-data /var/log/gunicorn
    systemctl daemon-reload
    systemctl restart gunicorn
    systemctl enable gunicorn
}

setup_nginx() {
    sudo -u www-data ./manage.py collectstatic --clear --no-input
    rm -f /etc/nginx/sites-enabled/default
    cp -f nginx/django-file-server /etc/nginx/sites-available/
    ln -sf /etc/nginx/sites-available/django-file-server /etc/nginx/sites-enabled
    systemctl restart nginx
}

setup_gunicorn
setup_nginx
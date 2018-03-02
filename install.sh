#!/bin/bash
set -e

fix_permissions() {
    chown -R www-data:www-data /srv/django-file-server/
}

setup_gunicorn() {
    cp -f systemd/gunicorn.service /etc/systemd/system/
    install -d -o www-data -g www-data /var/log/gunicorn
    systemctl daemon-reload
    systemctl restart gunicorn
    systemctl enable gunicorn
}

setup_nginx() {
    ./manage.py collectstatic --clear --no-input
    chown -R www-data:www-data /var/lib/django-file-server/
    cp -f nginx/ssl-cert.pem nginx/ssl-key.pem /etc/nginx/
    rm -f /etc/nginx/sites-enabled/default
    cp -f nginx/django-file-server /etc/nginx/sites-available/
    ln -sf /etc/nginx/sites-available/django-file-server /etc/nginx/sites-enabled
    systemctl restart nginx
}

fix_permissions
setup_gunicorn
setup_nginx
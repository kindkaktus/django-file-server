#!/bin/bash
set -e

ADMIN_NAME='admin'
ADMIN_EMAIL='admin@example.com'
ADMIN_PASSWORD='secret'


create_dir() {
    local _dir=$1
    install -d -o www-data -g www-data $_dir
}

recreate_dir() {
    local _dir=$1
    rm -rf $_dir
    create_dir $_dir
}

create_dirs() {
    recreate_dir /srv/django-file-server
    create_dir /var/lib/django-file-server
    create_dir /var/log/django-file-server
}

stop_all() {
    # the service might not exist yet, so allow it to fail
    systemctl stop nginx || true
    systemctl stop gunicorn || true
}

create_superuser() {
    echo "Creating superuser ${ADMIN_NAME}"
    local cmd="from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='${ADMIN_NAME}').exists() or User.objects.create_superuser('${ADMIN_NAME}', '${ADMIN_EMAIL}', '${ADMIN_PASSWORD}')"
    echo "${cmd}" | sudo -u www-data ./manage.py shell
}

setup_backend() {
    echo "Setting up backend"
    sudo -u www-data cp -R django_file_server/ templates/ /srv/django-file-server/
    sudo -u www-data ./manage.py migrate
    create_superuser
}

setup_gunicorn() {
    echo "Setting up gunicorn"
    cp -f systemd/gunicorn.service /etc/systemd/system/
    install -d -o www-data -g www-data /var/log/gunicorn
    systemctl daemon-reload
    systemctl restart gunicorn
    systemctl enable gunicorn
}

setup_nginx() {
    echo "Setting up nginx"
    sudo -u www-data ./manage.py collectstatic --clear --no-input
    cp -f nginx/ssl-cert.pem nginx/ssl-key.pem /etc/nginx/
    rm -f /etc/nginx/sites-enabled/default
    cp -f nginx/django-file-server /etc/nginx/sites-available/
    ln -sf /etc/nginx/sites-available/django-file-server /etc/nginx/sites-enabled
    systemctl restart nginx
}

stop_all
create_dirs
setup_backend
setup_gunicorn
setup_nginx
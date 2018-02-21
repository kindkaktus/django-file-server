Django  file server
==================================

Minimalistic password-protected file server powered by Django.

The project contains source code from [Django file upload example at https://github.com/axelpale/minimal-django-file-upload-example) and [Authentication to Django websites https://github.com/narenaryan/django-auth-pattern]


Django 1.11 is supported

------------------
First ensure you have Django 1.9 installed. Then:

    $ git clone https://github.com/kindkaktus/django-file-server
	$ cd django-file-server
    $ sudo pip install -r requirements.txt
	$ ./manage.py migrate
    $ ./manage.py createsuperuser
	$ sudo ./manage.py runserver 0.0.0.0:80

Debugging

    $ sudo ./manage.py runserver 0.0.0.0:80  --settings=django_file_server.settings_devel


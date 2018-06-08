# -*- coding: utf-8 -*-

# from django.http import HttpRequest
from django.test import TestCase
# from django.test import SimpleTestCase
# from django.urls import reverse

# from . import views

ADMIN_NAME = 'admin'
ADMIN_PASSWORD = 'secret'


class FileListViewTests(TestCase):

    def test_login(self):
        #@todo create user? (setup)
        self.assertTrue(self.client.login(username=ADMIN_NAME, password=ADMIN_PASSWORD))
        self.assertFalse(self.client.login(username=ADMIN_NAME + '.bad', password=ADMIN_PASSWORD))
        self.assertFalse(self.client.login(username=ADMIN_NAME, password=ADMIN_PASSWORD + '.bad'))

    def test_request_root_page_when_not_logged_in(self):
        # first redirect to the file list, then redirects to the login page

        response = self.client.get('/', follow=False)
        self.assertRedirects(response, '/list/', status_code=301, target_status_code=302)

        response = self.client.get('/', follow=True)
        self.assertRedirects(response, '/login/?next=/list/', status_code=301, target_status_code=200)



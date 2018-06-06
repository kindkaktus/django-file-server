# -*- coding: utf-8 -*-

from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

# from . import views


class FileListViewTests(SimpleTestCase):

    def test_list_files_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


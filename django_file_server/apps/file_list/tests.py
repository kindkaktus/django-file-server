# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# from . import views

TEST_ADMIN_USERNAME = 'admin'
TEST_ADMIN_EMAIL = 'admin@example.com'
TEST_ADMIN_PASSWORD = 'secret'


class FileListViewTests(TestCase):
    def setUp(self):
        super(FileListViewTests, self).setUp()
        self.admin_user = get_user_model().objects.create_superuser(
            username=TEST_ADMIN_USERNAME, email=TEST_ADMIN_EMAIL,
            password=TEST_ADMIN_PASSWORD
        )
        self.login()

    def tearDown(self):
        get_user_model().objects.all().delete()
        super(FileListViewTests, self).tearDown()

    def login(self):
        self.client.login(
            username=TEST_ADMIN_USERNAME, password=TEST_ADMIN_PASSWORD
        )

    def logout(self):
        self.client.logout()

    def test_request_when_not_logged_in(self):
        # given
        self.logout()

        # first redirects to the file list, then to the login page

        response = self.client.get('/', follow=False)
        self.assertRedirects(response, reverse('list'), status_code=301, target_status_code=302)

        response = self.client.get('/', follow=True)
        self.assertRedirects(response, '{}?next={}'.format(reverse('login'), reverse('list')), status_code=301, target_status_code=200)

        response = self.client.get(reverse('list'))
        self.assertRedirects(response, '{}?next={}'.format(reverse('login'), reverse('list')), status_code=302, target_status_code=200)

    def test_request_when_logged_in(self):
        response = self.client.get('/')
        self.assertRedirects(response, reverse('list'), status_code=301, target_status_code=200)

        response = self.client.get(reverse('list'))
        self.assertEquals(response.status_code, 200)

    def test_request_filelist(self):
        # empty file list
        response = self.client.get(reverse('list'))
        self.assertEquals(len(response.context['deliverables']), 0)

        # upload file
        from django.core.files.uploadedfile import SimpleUploadedFile
        f = SimpleUploadedFile("file.txt", b"file_content")
        response = self.client.post(reverse('list'), {'docfile': f})
        self.assertEquals(len(response.context['deliverables']), 1)
        print(response.content)


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from hello.views import get_index
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from accounts.models import User


class HelloPageTest(TestCase):

    def setUp(self):
        super(HelloPageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('letmein')
        self.user.save()

    def test_login(self):
        login = self.client.login(username='testuser', password='letmein')
        self.assertTrue(login)

    def test_hello_page_uses_index_view(self):
        hello_page = resolve('/')
        self.assertEqual(hello_page.func, get_index)

    def test_hello_page_uses_index_template(self):
        hello_page = self.client.get('/')
        self.assertTemplateUsed(hello_page, "index.html")

    def test_hello_page_logged_in_content(self):
        self.client.login(username='testuser', password='letmein')
        hello_page = self.client.get('/')

        hello_page_template_output = render_to_response(
            "index.html", {'user': self.user}).content
        self.assertEquals(hello_page.content, hello_page_template_output)




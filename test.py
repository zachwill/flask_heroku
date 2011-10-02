#!/usr/bin/env python

"""Tests for the Flask Heroku template."""

import unittest
from app import create_app


class TestApp(unittest.TestCase):

    def setUp(self):
        app = create_app()
        self.app = app.test_client()

    def test_home_page_works(self):
        rv = self.app.get('/')
        self.assertTrue(rv.data)
        self.assertEquals(rv.status_code, 200)

    def test_about_page_works(self):
        rv = self.app.get('/about/')
        self.assertTrue(rv.data)
        self.assertEquals(rv.status_code, 200)

    def test_default_redirecting(self):
        rv = self.app.get('/about')
        self.assertEquals(rv.status_code, 301)

    def test_404_page(self):
        rv = self.app.get('/i-am-not-found/')
        self.assertEquals(rv.status_code, 404)

    def test_static_text_file_request(self):
        rv = self.app.get('/humans.txt')
        self.assertTrue(rv.data)
        self.assertEquals(rv.status_code, 200)

    def test_qunit_javascript_tests(self):
        rv = self.app.get('/qunit/')
        assert 'QUnit Tests' in rv.data
        self.assertEquals(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()

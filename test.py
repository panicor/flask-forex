from unittest import TestCase
from app import app
from flask import session

class FlaskTests(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        with self.client:
            resp = self.client.get("/")
            self.assertIn(b"Convert to:", resp.data)
            self.assertIn(b"Convert from:", resp.data)
            self.assertIn(b"Amount:", resp.data)

    def test_convert(self):
        with self.client:
            



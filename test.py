import unittest
import json
from flask_app import app

class TestAlphaChanger(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_alphachanger_latin_to_cyrillic(self):
        data = {
            "context": "Privet, Mir!",
            "pattern": "cyrillic"
        }
        response = self.app.post('/translate', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], "Привет, Мир!")

    def test_alphachanger_cyrillic_to_latin(self):
        data = {
            "context": "Привет, Мир!",
            "pattern": "latin"
        }
        response = self.app.post('/translate', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], "Privet, Mir!")

    def test_invalid_input(self):
        data = {
            "context": "",
            "pattern": "cyrillic"
        }
        response = self.app.post('/translate', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], "")

    def test_invalid_pattern(self):
        data = {
            "context": "Hello, World!",
            "pattern": "invalid_pattern"
        }
        response = self.app.post('/translate', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()

import unittest
import json
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict(self):
        payload = {
            "pclass": 3,
            "age": 22,
            "sibsp": 1,
            "parch": 0,
            "fare": 7.25,
            "sex": "male"
        }
        response = self.app.post('/predict', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'survived', response.data)

if __name__ == '__main__':
    unittest.main()

import unittest
import json
from app import app

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add(self):
        payload = {'num1': 5, 'num2': 3}
        response = self.app.post('/add', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 8)

    def test_add_negative_numbers(self):
        payload = {'num1': -5, 'num2': -3}
        response = self.app.post('/add', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], -8)

    def test_subtract(self):
        payload = {'num1': 10, 'num2': 3}
        response = self.app.post('/subtract', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 7)

    def test_multiply(self):
        payload = {'num1': 4, 'num2': 5}
        response = self.app.post('/multiply', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 20)

    def test_divide(self):
        payload = {'num1': 10, 'num2': 2}
        response = self.app.post('/divide', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 5)

    def test_divide_by_zero(self):
        payload = {'num1': 10, 'num2': 0}
        response = self.app.post('/divide', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'Division by zero')

    def test_invalid_numbers(self):
        payload = {'num1': 'abc', 'num2': 'def'}
        response = self.app.post('/add', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'Invalid numbers')

    def test_missing_parameters(self):
        payload = {'num1': 5}
        response = self.app.post('/add', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error'], 'Missing num1 or num2')

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Flask Calculator API', response.data.decode())

if __name__ == '__main__':
    unittest.main()
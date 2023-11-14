import unittest

import requests


class TestAccountCrud(unittest.TestCase):

    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }

    @classmethod
    def setUpClass(cls):
        cls.url = "http://localhost:5000/api/accounts"
        
    def test_create_account(self):
        response = requests.post(self.url, json=self.person)
        self.assertEqual(response.status_code, 201, "Account was not created!")

    def test_get_account_account_exists(self):
        response = requests.get(f"{self.url}/{self.person["pesel"]}")
        self.assertEqual(response.status_code, 200, "Invalid status code!")

        data = response.json()
        self.assertEqual(data["first_name"], self.person["first_name"], "Invalid first name!")
        self.assertEqual(data["last_name"], self.person["last_name"], "Invalid last name!")
        self.assertEqual(data["pesel"], self.person["pesel"], "Invalid pesel!")

    def test_get_account_account_does_not_exists(self):
        response = requests.get(f"{self.url}/11111111111")
        self.assertEqual(response.status_code, 404, "Invalid status code!")

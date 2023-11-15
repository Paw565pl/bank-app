import unittest

import requests

from ..AccountSet import AccountSet


class TestAccountCrud(unittest.TestCase):
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = "http://localhost:5000/api/accounts"

    @classmethod
    def tearDownClass(self) -> None:
        AccountSet.private_accounts = []

    def test_1_create_account(self):
        response = requests.post(self.url, json=self.person)
        self.assertEqual(response.status_code, 201, "Account was not created!")

    def test_2_accounts_count(self):
        response = requests.get(f"{self.url}/count")
        data = response.json()

        self.assertEqual(response.status_code, 200, "Invalid status code!")
        self.assertEqual(data["count"], 1, "Invalid accounts count!")

    def test_3_get_account_account_does_not_exists(self):
        response = requests.get(f"{self.url}/11111111111")
        self.assertEqual(response.status_code, 404, "Invalid status code!")

    def test_4_get_account_account_exists(self):
        response = requests.get(f"{self.url}/{self.person["pesel"]}")
        data = response.json()

        self.assertEqual(response.status_code, 200, "Invalid status code!")
        self.assertEqual(
            data["first_name"], self.person["first_name"], "Invalid first name!"
        )
        self.assertEqual(
            data["last_name"], self.person["last_name"], "Invalid last name!"
        )
        self.assertEqual(data["pesel"], self.person["pesel"], "Invalid pesel!")

    def test_5_update_account(self):
        response = requests.patch(
            f"{self.url}/{self.person["pesel"]}", json={"first_name": "john"}
        )
        self.assertEqual(response.status_code, 200, "Invalid status code!")

    def test_6_delete_account(self):
        response = requests.delete(f"{self.url}/{self.person["pesel"]}")
        self.assertEqual(response.status_code, 200, "Invalid status code!")

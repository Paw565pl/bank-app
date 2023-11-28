import unittest

import requests


class TestAccountTransfer(unittest.TestCase):
    url = "http://localhost:5000/api/accounts"
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }

    def setUp(self) -> None:
        requests.post(self.url, json=self.person)

    def tearDown(self) -> None:
        requests.delete(f"{self.url}/{self.person['pesel']}")

    def test_account_does_not_exists(self):
        body = {"amount": 100, "type": "incoming"}
        response = requests.post(f"{self.url}/11111111111/transfer", json=body)
        self.assertEqual(response.status_code, 404, "Invalid status code!")

    def test_incoming_transfer(self):
        body = {"amount": 100, "type": "incoming"}
        response = requests.post(
            f"{self.url}/{self.person['pesel']}/transfer", json=body
        )
        self.assertEqual(response.status_code, 200, "Invalid status code!")

    def test_successful_outgoing_transfer(self):
        body_incoming = {"amount": 200, "type": "incoming"}
        response = requests.post(
            f"{self.url}/{self.person['pesel']}/transfer", json=body_incoming
        )

        body_outgoing = {"amount": 100, "type": "outgoing"}
        response = requests.post(
            f"{self.url}/{self.person['pesel']}/transfer", json=body_outgoing
        )

        account = requests.get(f"{self.url}/{self.person['pesel']}").json()
        self.assertEqual(response.status_code, 200, "Invalid status code!")
        self.assertEqual(account["balance"], 100, "Invalid account balance!")

    def test_unsuccessful_outgoing_transfer(self):
        body = {"amount": 100, "type": "outgoing"}
        response = requests.post(
            f"{self.url}/{self.person['pesel']}/transfer", json=body
        )

        account = requests.get(f"{self.url}/{self.person['pesel']}").json()
        self.assertEqual(response.status_code, 200, "Invalid status code!")
        self.assertEqual(account["balance"], 0, "Invalid account balance!")

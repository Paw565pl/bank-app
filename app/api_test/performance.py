import unittest

import requests


class PerformanceTest(unittest.TestCase):
    base_url = "http://localhost:5000"
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }

    def test_private_bank_account(self):
        for _ in range(100):
            pesel = self.person["pesel"]

            create_response = requests.post(
                self.base_url + "/api/accounts", json=self.person, timeout=2
            )
            delete_response = requests.delete(
                self.base_url + f"/api/accounts/{pesel}", timeout=2
            )

            self.assertEqual(
                create_response.status_code, 201, "Account was not created!"
            )
            self.assertEqual(
                delete_response.status_code, 200, "Account was not deleted!"
            )

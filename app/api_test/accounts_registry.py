import unittest

import requests


class TestAccountsRegistry(unittest.TestCase):
    url = "http://localhost:5000/api/accounts"
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }

    @classmethod
    def setUpClass(cls) -> None:
        requests.post(cls.url, json=cls.person)

    @classmethod
    def tearDownClass(cls) -> None:
        requests.delete(f"{cls.url}/{cls.person['pesel']}")

    def test_save_and_load_account(self):
        save_response = requests.patch(f"{self.url}/save")
        self.assertEqual(save_response.status_code, 200, "Invalid status code!")

        delete_response = requests.delete(f"{self.url}/{self.person['pesel']}")
        self.assertEqual(delete_response.status_code, 200, "Invalid status code!")

        count_response = requests.get(f"{self.url}/count")
        self.assertEqual(count_response.status_code, 200, "Invalid status code!")
        count = count_response.json()["count"]
        self.assertEqual(count, 0, "Invalid count!")

        load_response = requests.patch(f"{self.url}/load")
        self.assertEqual(load_response.status_code, 200, "Invalid status code!")

        get_response = requests.get(f"{self.url}/{self.person['pesel']}")
        get_response_json = get_response.json()
        self.assertEqual(get_response.status_code, 200, "Invalid status code!")
        self.assertEqual(
            get_response_json["first_name"],
            self.person["first_name"],
            "Invalid first name!",
        )
        self.assertEqual(
            get_response_json["last_name"],
            self.person["last_name"],
            "Invalid last name!",
        )
        self.assertEqual(
            get_response_json["pesel"], self.person["pesel"], "Invalid pesel!"
        )

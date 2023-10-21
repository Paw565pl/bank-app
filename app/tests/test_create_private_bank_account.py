import unittest
from ..PrivateBankAccount import PrivateBankAccount


class TestCreatePrivateBankAccount(unittest.TestCase):
    first_name = "Dariusz"
    last_name = "Januszewski"
    pesel = "12345678900"
    too_short_pesel = pesel[:5]
    too_long_pesel = pesel + "111"
    promo_code = "PROM_XYZ"
    invalid_promo_code = promo_code[5:]

    def test_valid_data(self):
        account = PrivateBankAccount(self.first_name, self.last_name, self.pesel)
        self.assertEqual(
            account.first_name, self.first_name, "First name was not saved!"
        )
        self.assertEqual(account.last_name, self.last_name, "Last name was not saved!")
        self.assertEqual(account.balance, 0, "Balance is not zero!")
        self.assertEqual(account.pesel, self.pesel, "Pesel was not saved!")
        self.assertEqual(len(str(account.pesel)), 11)

    def test_too_short_pesel(self):
        account = PrivateBankAccount(
            self.first_name, self.last_name, self.too_short_pesel
        )
        self.assertEqual(account.pesel, "Niepoprawny pesel!", "Pesel was saved!")

    def test_too_long_pesel(self):
        account = PrivateBankAccount(
            self.first_name, self.last_name, self.too_long_pesel
        )
        self.assertEqual(account.pesel, "Niepoprawny pesel!", "Pesel was saved!")

    def test_valid_promo_code(self):
        account = PrivateBankAccount(
            self.first_name, self.last_name, self.pesel, self.promo_code
        )
        self.assertEqual(account.balance, 50, "Balance was not increased!")

    def test_invalid_promo_code(self):
        account = PrivateBankAccount(
            self.first_name, self.last_name, self.pesel, self.invalid_promo_code
        )
        self.assertEqual(account.balance, 0, "Balance was increased!")

    def test_valid_promo_code_invalid_pesel(self):
        account = PrivateBankAccount(
            self.first_name, self.last_name, self.too_short_pesel, self.promo_code
        )
        self.assertEqual(account.balance, 0, "Balance was increased!")

    def test_person_born_in_1960_no_balance_increase(self):
        account = PrivateBankAccount(
            self.first_name, self.last_name, "60042687887", self.promo_code
        )
        self.assertEqual(account.balance, 0, "Balance was increased!")

    def test_person_born_in_1970_invalid_promo_code_no_balance_increase(self):
        account = PrivateBankAccount(
            self.first_name, self.last_name, "70092182867", self.invalid_promo_code
        )
        self.assertEqual(account.balance, 0, "Balance was increased!")

    def test_person_born_in_1970_balance_increase(self):
        account = PrivateBankAccount(
            self.first_name, self.last_name, "70092182867", self.promo_code
        )
        self.assertEqual(account.balance, 50, "Balance was not increased!")

    def test_person_born_in_2003_balance_increase(self):
        account = PrivateBankAccount(
            self.first_name, self.last_name, "03241178518", self.promo_code
        )
        self.assertEqual(account.balance, 50, "Balance was not increased!")

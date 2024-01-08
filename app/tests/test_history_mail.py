import unittest
from datetime import date
from unittest.mock import MagicMock, Mock, patch

from app.CompanyBankAccount import CompanyBankAccount
from app.PrivateBankAccount import PrivateBankAccount
from app.SMTPConnection import SMTPConnection


class TestHistoryMail(unittest.TestCase):
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }
    company = {"name": "test", "nip": "1234567890"}
    email = "djanuszewski@abc.com"

    @classmethod
    def setUpClass(cls) -> None:
        cls.smtpInstance = SMTPConnection()

    def test_private_account(self):
        self.smtpInstance.send = MagicMock(return_value=True)
        today = date.today()
        account = PrivateBankAccount(**self.person)
        account.balance = 1000
        account.outgoing_transfer(100)

        status = account.send_transfer_history_to_mail(self.email, self.smtpInstance)

        self.assertTrue(status)
        self.smtpInstance.send.assert_called_once_with(
            f"Wyciąg z dnia {today}",
            "Twoja historia konta to: [-100]",
            self.email,
        )

    def test_private_account_unsuccessful(self):
        self.smtpInstance.send = MagicMock(return_value=False)
        today = date.today()
        account = PrivateBankAccount(**self.person)
        account.balance = 1000
        account.outgoing_transfer(100)

        status = account.send_transfer_history_to_mail(self.email, self.smtpInstance)

        self.assertFalse(status)
        self.smtpInstance.send.assert_called_once_with(
            f"Wyciąg z dnia {today}",
            "Twoja historia konta to: [-100]",
            self.email,
        )

    @patch("requests.get")
    def test_company_account(self, check_if_nip_is_in_register: Mock):
        check_if_nip_is_in_register.return_value.status_code = 200
        self.smtpInstance.send = MagicMock(return_value=True)
        today = date.today()
        account = CompanyBankAccount(**self.company)
        account.balance = 1000
        account.outgoing_transfer(100)

        status = account.send_transfer_history_to_mail(self.email, self.smtpInstance)

        self.assertTrue(status)
        self.smtpInstance.send.assert_called_once_with(
            f"Wyciąg z dnia {today}",
            "Historia konta Twojej firmy to: [-100]",
            self.email,
        )

import requests
from behave import then, when
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
base_url = "http://localhost:5000"


@when('I make an "{type}" transfer of "{amount}"')
def make_transfer(context, type, amount):
    body = {"amount": int(amount), "type": type}
    response = requests.post(
        f"{base_url}/api/accounts/{context.pesel}/transfer", json=body
    )
    assert_equal(response.status_code, 200)


@then('My balance should be "{amount}"')
def check_account_balance(context, amount):
    response = requests.get(f"{base_url}/api/accounts/{context.pesel}")
    balance = response.json().get("balance")
    assert_equal(balance, int(amount))

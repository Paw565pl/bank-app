import requests
from behave import step, then, when
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000"


@when(
    'I create an account using first name: "{first_name}", last name: "{last_name}", pesel: "{pesel}"'
)
def create_account(context, first_name, last_name, pesel):
    json_body = {
        "first_name": first_name,
        "last_name": last_name,
        "pesel": pesel,
    }
    response = requests.post(URL + "/api/accounts", json=json_body)
    assert_equal(response.status_code, 201)


@step('Number of accounts in registry equals: "{count}"')
def check_accounts_count(context, count):
    response = requests.get(URL + "/api/accounts/count")
    assert_equal(response.json()["count"], int(count))


@step('Account with pesel "{pesel}" exists in registry')
def check_if_account_with_given_pesel_exists(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    print(pesel)
    print("GIGA SUSSY", f"/api/accounts/{pesel}")
    assert_equal(response.status_code, 200)


@step('Account with pesel "{pesel}" does not exist in registry')
def check_if_account_with_given_pesel_does_not_exist(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(response.status_code, 404)


@when('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    response = requests.delete(URL + f"/api/accounts/{pesel}")
    assert_equal(response.status_code, 200)


@when("I save the account registry to db")
def save_accounts_to_db(context):
    response = requests.patch(URL + "/api/accounts/save")
    assert_equal(response.status_code, 200)


@when("I load account registry from db")
def load_accounts_from_db(context):
    response = requests.patch(URL + "/api/accounts/load")
    assert_equal(response.status_code, 200)


@when('I update last name in account with pesel "{pesel}" to "{last_name}"')
def update_last_name(context, pesel, last_name):
    response = requests.patch(
        URL + f"/api/accounts/{pesel}", json={"last_name": last_name}
    )
    assert_equal(response.status_code, 200)


@then('Last name in account with pesel "{pesel}" is "{last_name}"')
def check_last_name(context, pesel, last_name):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    json = response.json()
    assert_equal(json["last_name"], last_name)

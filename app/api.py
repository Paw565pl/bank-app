from flask import Flask, jsonify, request

from .AccountSet import AccountSet
from .PrivateBankAccount import PrivateBankAccount

app = Flask(__name__)


@app.post("/api/accounts")
def post_create_personal_account():
    data = request.get_json()

    account = PrivateBankAccount(data["first_name"], data["last_name"], data["pesel"])
    AccountSet.add_personal_account(account)

    return jsonify({"message": "personal account was created"}), 201


@app.get("/api/accounts/count")
def get_personal_accounts_count():
    count = AccountSet.get_personal_accounts_count()
    return jsonify({"count": count})


@app.get("/api/accounts/<pesel>")
def get_personal_account(pesel):
    account = AccountSet.get_personal_account_by_pesel(pesel)

    if not account:
        return jsonify({"message": "account with the given pesel does not exist"}), 404

    return jsonify(account.__dict__)


@app.patch("/api/accounts/<pesel>")
def patch_personal_account(pesel):
    account = AccountSet.get_personal_account_by_pesel(pesel)

    if not account:
        return jsonify({"message": "account with the given pesel does not exist"}), 404

    data = request.get_json()

    for key, value in data.items():
        if hasattr(account, key):
            setattr(account, key, value)

    return jsonify({"message": "account updated successfully"})


@app.delete("/api/accounts/<pesel>")
def delete_personal_account(pesel):
    account = AccountSet.get_personal_account_by_pesel(pesel)

    if not account:
        return jsonify({"message": "account with the given pesel does not exist"}), 404

    AccountSet.personal_accounts.remove(account)

    return jsonify({"message": "account deleted successfully"})

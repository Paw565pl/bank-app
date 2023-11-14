from flask import Flask, jsonify, request

from .AccountSet import AccountSet
from .PrivateBankAccount import PrivateBankAccount

app = Flask(__name__)


@app.route("/api/accounts", methods=["POST"])
def create_personal_account():
    data = request.get_json()

    account = PrivateBankAccount(data["first_name"], data["last_name"], data["pesel"])
    AccountSet.add_personal_account(account)

    return jsonify({"message": "personal account was created"}), 201


@app.route("/api/accounts/count", methods=["GET"])
def personal_accounts_count():
    count = AccountSet.get_personal_accounts_count()
    return jsonify({"count": count})


@app.route("/api/accounts/<pesel>", methods=["GET"])
def personal_account(pesel):
    account = AccountSet.get_personal_account_by_pesel(pesel)

    if not account:
        return jsonify({"message": "account with the given pesel does not exist"}), 404

    return jsonify(account.__dict__)

from flask import Flask, jsonify, request
from dotenv import load_dotenv

from .AccountSet import AccountSet
from .PrivateBankAccount import PrivateBankAccount

load_dotenv()
app = Flask(__name__)


@app.post("/api/accounts")
def post_create_private_account():
    data = request.get_json()

    account_with_given_pesel = AccountSet.get_private_account_by_pesel(data["pesel"])
    if account_with_given_pesel is not None:
        return jsonify({"message": "account with this pesel already exists"}), 409

    account = PrivateBankAccount(data["first_name"], data["last_name"], data["pesel"])
    AccountSet.add_private_account(account)

    return jsonify({"message": "private account was created"}), 201


@app.get("/api/accounts/count")
def get_private_accounts_count():
    count = AccountSet.get_private_accounts_count()
    return jsonify({"count": count})


@app.get("/api/accounts/<pesel>")
def get_private_account(pesel):
    account = AccountSet.get_private_account_by_pesel(pesel)

    if not account:
        return jsonify({"message": "account with the given pesel does not exist"}), 404

    return jsonify(account.__dict__)


@app.patch("/api/accounts/<pesel>")
def patch_private_account(pesel):
    account = AccountSet.get_private_account_by_pesel(pesel)

    if not account:
        return jsonify({"message": "account with the given pesel does not exist"}), 404

    data = request.get_json()

    for key, value in data.items():
        if hasattr(account, key):
            setattr(account, key, value)

    return jsonify({"message": "account updated successfully"})


@app.delete("/api/accounts/<pesel>")
def delete_private_account(pesel):
    account = AccountSet.get_private_account_by_pesel(pesel)

    if not account:
        return jsonify({"message": "account with the given pesel does not exist"}), 404

    AccountSet.private_accounts.remove(account)

    return jsonify({"message": "account deleted successfully"})


@app.post("/api/accounts/<pesel>/transfer")
def private_account_do_transfer(pesel):
    data = request.get_json()
    amount = data["amount"]
    type = data["type"].lower()

    account = AccountSet.get_private_account_by_pesel(pesel)
    if not account:
        return jsonify({"message": "account with the given pesel does not exist"}), 404

    if type == "incoming":
        account.incoming_transfer(amount)
    elif type == "outgoing":
        account.outgoing_transfer(amount)

    return jsonify({"message": "transfer has been accepted for execution"}), 200

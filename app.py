from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from controller import exec_crawler_feed
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    "admin": generate_password_hash("admin")
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@auth.login_required
@app.route('/feed')
def do_crawler_feed():
    response = exec_crawler_feed()
    return jsonify(response)


if __name__ == '__main__':
    app.run()

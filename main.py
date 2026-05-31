from flask import Flask, request
from model import db, Company

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True,
            use_reloader=True,
            host="0.0.0.0",
            port=5000,)  # auto-generate a temporary self-signed cert

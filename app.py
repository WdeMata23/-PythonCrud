from flask import Flask

app = Flask(__name__)

from productos import productos


@app.route("/ping")
def ping():
    return jsonify({"messae": "pong!"})


if __name__ == "__main__":
    app.run(debug=True, port=400)

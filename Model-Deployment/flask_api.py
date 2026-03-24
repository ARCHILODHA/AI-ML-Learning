from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "ML Model API Running"

app.run()

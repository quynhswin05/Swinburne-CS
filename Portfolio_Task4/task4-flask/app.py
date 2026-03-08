from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "SWE40006 Flask Application Running"

@app.route("/api")
def api():
    return jsonify({
        "status": "success",
        "message": "API endpoint is working"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
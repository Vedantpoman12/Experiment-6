from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Vedant Poman</h1><p>CI/CD Pipeline with Jenkins & GitHub Webhook</p>"

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "version": "1.0.0"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
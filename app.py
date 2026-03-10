from flask import Flask, jsonify

app = Flask(__name__)

APP_ID = 2410222

@app.route("/")
def index():
    return f"""
    <h1>Vedant Poman</h1>
    <p>App ID: {APP_ID}</p>
    <p>CI/CD Pipeline with Jenkins & GitHub Webhook</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "app_id": APP_ID,
        "version": "1.0.0"
    }), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
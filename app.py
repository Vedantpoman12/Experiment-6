from flask import Flask, jsonify, send_file, render_template_string
import os

app = Flask(__name__)

APP_ID = 2410222

RESUME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vedant Poman - Resume</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px 20px;
        }
        .card {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 24px;
            padding: 50px;
            max-width: 700px;
            width: 100%;
            color: white;
            box-shadow: 0 25px 50px rgba(0,0,0,0.4);
        }
        .header { text-align: center; margin-bottom: 40px; }
        .avatar {
            width: 90px; height: 90px;
            background: linear-gradient(135deg, #6c63ff, #3ecfcf);
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 36px; font-weight: 700;
            margin: 0 auto 20px;
        }
        h1 { font-size: 2rem; font-weight: 700; }
        .app-id {
            display: inline-block;
            background: linear-gradient(135deg, #6c63ff, #3ecfcf);
            border-radius: 20px;
            padding: 4px 16px;
            font-size: 0.85rem;
            margin-top: 8px;
            font-weight: 600;
        }
        .subtitle { color: #aaa; margin-top: 8px; font-size: 0.95rem; }
        .divider {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.1);
            margin: 30px 0;
        }
        .section-title {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #6c63ff;
            font-weight: 600;
            margin-bottom: 15px;
        }
        .info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 30px; }
        .info-item { background: rgba(255,255,255,0.05); border-radius: 12px; padding: 14px 18px; }
        .info-label { font-size: 0.7rem; color: #888; text-transform: uppercase; letter-spacing: 1px; }
        .info-value { font-size: 0.95rem; color: white; font-weight: 500; margin-top: 4px; }
        .download-btn {
            display: block;
            width: 100%;
            text-align: center;
            background: linear-gradient(135deg, #6c63ff, #3ecfcf);
            color: white;
            text-decoration: none;
            padding: 16px;
            border-radius: 14px;
            font-weight: 600;
            font-size: 1rem;
            margin-top: 30px;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 4px 20px rgba(108, 99, 255, 0.4);
        }
        .download-btn:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(108, 99, 255, 0.6); }
        .back-btn {
            display: block;
            text-align: center;
            color: #aaa;
            text-decoration: none;
            margin-top: 16px;
            font-size: 0.9rem;
            transition: color 0.2s;
        }
        .back-btn:hover { color: white; }
    </style>
</head>
<body>
    <div class="card">
        <div class="header">
            <div class="avatar">VP</div>
            <h1>Vedant Poman</h1>
            <span class="app-id">App ID: 2410222</span>
            <p class="subtitle">Developer | DevOps Enthusiast</p>
        </div>
        <hr class="divider">
        <p class="section-title">Details</p>
        <div class="info-grid">
            <div class="info-item">
                <div class="info-label">GitHub</div>
                <div class="info-value">Vedantpoman12</div>
            </div>
            <div class="info-item">
                <div class="info-label">Pipeline</div>
                <div class="info-value">Jenkins + GitHub</div>
            </div>
            <div class="info-item">
                <div class="info-label">App ID</div>
                <div class="info-value">2410222</div>
            </div>
            <div class="info-item">
                <div class="info-label">Status</div>
                <div class="info-value">🟢 Active</div>
            </div>
        </div>
        <hr class="divider">
        <a href="/resume/download" class="download-btn">⬇ Download Full Resume (PDF)</a>
        <a href="/" class="back-btn">← Back to Home</a>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return f"""
    <html>
    <head>
        <title>Vedant Poman | App {APP_ID}</title>
        <style>
            body {{ font-family: Inter, sans-serif; background: #0f0c29; color: white;
                   display: flex; align-items: center; justify-content: center;
                   min-height: 100vh; text-align: center; }}
            h1 {{ font-size: 2.5rem; }}
            p {{ color: #aaa; margin: 10px 0; }}
            a {{ display: inline-block; margin-top: 20px; padding: 14px 32px;
                 background: linear-gradient(135deg, #6c63ff, #3ecfcf);
                 color: white; text-decoration: none; border-radius: 30px;
                 font-weight: 600; transition: transform 0.2s; }}
            a:hover {{ transform: translateY(-2px); }}
            .badge {{ background: rgba(108,99,255,0.2); border: 1px solid #6c63ff;
                      padding: 4px 14px; border-radius: 20px; font-size: 0.85rem;
                      display: inline-block; margin-top: 8px; }}
        </style>
    </head>
    <body>
        <div>
            <h1>Vedant Poman</h1>
            <span class="badge">App ID: {APP_ID}</span>
            <p>CI/CD Pipeline with Jenkins & GitHub Webhook</p>
            <a href="/resume">View Resume</a>
        </div>
    </body>
    </html>
    """

@app.route("/resume")
def resume():
    return render_template_string(RESUME_HTML)

@app.route("/resume/download")
def download_resume():
    pdf_path = os.path.join(os.path.dirname(__file__), "Vedant Poman.pdf")
    return send_file(pdf_path, as_attachment=True, download_name="Vedant_Poman_Resume.pdf")

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "app_id": APP_ID,
        "version": "1.0.0"
    }), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
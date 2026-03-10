from flask import Flask, jsonify, send_file, render_template_string
import os

app = Flask(__name__)

APP_ID = 2410222

RESUME_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vedant Poman - Resume</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            margin: 0;
            padding: 30px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            font-size: 2rem;
            margin-bottom: 4px;
            color: #111;
        }
        .app-id {
            font-size: 0.9rem;
            color: #888;
            margin-bottom: 10px;
        }
        .contact {
            font-size: 0.95rem;
            color: #555;
            margin-bottom: 20px;
        }
        hr {
            border: none;
            border-top: 2px solid #eee;
            margin: 20px 0;
        }
        h2 {
            font-size: 1.1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #444;
            border-bottom: 1px solid #ddd;
            padding-bottom: 6px;
            margin-bottom: 14px;
        }
        .section { margin-bottom: 28px; }
        .item { margin-bottom: 12px; }
        .item-title { font-weight: bold; font-size: 1rem; }
        .item-sub { font-size: 0.9rem; color: #666; }
        .skills-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            list-style: none;
            padding: 0;
        }
        .skills-list li {
            background: #f0f0f0;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.9rem;
            color: #333;
        }
        .download-btn {
            display: inline-block;
            margin-top: 10px;
            padding: 12px 28px;
            background: #333;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 0.95rem;
        }
        .download-btn:hover { background: #555; }
        .back { display: inline-block; margin-bottom: 20px; color: #555; text-decoration: none; font-size: 0.9rem; }
        .back:hover { color: #000; }
    </style>
</head>
<body>
    <div class="container">
        <a href="/" class="back">← Back to Home</a>

        <h1>Vedant Poman</h1>
        <div class="app-id">App ID: 2410222</div>
        <div class="contact">
            GitHub: github.com/Vedantpoman12 &nbsp;|&nbsp;
            Email: vedant.poman@gmail.com
        </div>

        <hr>

        <div class="section">
            <h2>Education</h2>
            <div class="item">
                <div class="item-title">Bachelor of Engineering – Computer Engineering</div>
                <div class="item-sub">2022 – 2026</div>
            </div>
        </div>

        <div class="section">
            <h2>Skills</h2>
            <ul class="skills-list">
                <li>Python</li>
                <li>Flask</li>
                <li>Jenkins</li>
                <li>GitHub</li>
                <li>CI/CD</li>
                <li>HTML/CSS</li>
                <li>Git</li>
                <li>Linux</li>
            </ul>
        </div>

        <div class="section">
            <h2>Projects</h2>
            <div class="item">
                <div class="item-title">Skill Gap Bridge</div>
                <div class="item-sub">AI-based learning platform to identify and bridge skill gaps for students.</div>
            </div>
            <div class="item">
                <div class="item-title">CI/CD Pipeline – Flask + Jenkins</div>
                <div class="item-sub">Automated deployment pipeline using GitHub Webhooks and Jenkins.</div>
            </div>
            <div class="item">
                <div class="item-title">Agro-AI</div>
                <div class="item-sub">AI-powered agriculture assistant with voice command support.</div>
            </div>
        </div>

        <div class="section">
            <h2>Download Resume</h2>
            <a href="/resume/download" class="download-btn">⬇ Download PDF</a>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return """
    <html>
    <head><title>Vedant Poman</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4;
               display: flex; align-items: center; justify-content: center;
               min-height: 100vh; margin: 0; }
        .box { background: white; padding: 40px 50px; border-radius: 8px;
               box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; }
        h1 { margin-bottom: 6px; }
        p { color: #666; margin: 6px 0; }
        a { display: inline-block; margin-top: 20px; padding: 12px 28px;
            background: #333; color: white; text-decoration: none; border-radius: 6px; }
        a:hover { background: #555; }
    </style>
    </head>
    <body>
        <div class="box">
            <h1>Vedant Poman</h1>
            <p>App ID: 2410222APP</p>
            <p>CI/CD Pipeline – Flask + Jenkins + GitHub Webhook</p>
            <a href="/resume">View Resume</a>
        </div>
    </body>
    </html>
    """

@app.route("/resume")
def resume():
    return render_template_string(RESUME_PAGE)

@app.route("/resume/download")
def download_resume():
    pdf_path = os.path.join(os.path.dirname(__file__), "Vedant Poman.pdf")
    return send_file(pdf_path, as_attachment=True, download_name="Vedant_Poman_Resume.pdf")

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "app_id": APP_ID, "version": "1.0.0"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, render_template_string, request, redirect, session, url_for, send_file
import subprocess, os, time, uuid

app = Flask(__name__)
app.secret_key = "super_secret_key"
MAX_ATTEMPTS = 5
LOCK_TIME = 60  # seconds
SQLMAP_PATH = "sqlmap"  # تأكد أن sqlmap مضاف للمسار

# HTML Templates
login_template = """
<!DOCTYPE html>
<html>
<head>
  <title>Login - kader11000</title>
  <style>
    body { background:#222; color:white; display:flex; align-items:center; justify-content:center; height:100vh; font-family:sans-serif; }
    .box { background:white; color:black; padding:30px; border-radius:10px; width:300px; box-shadow:0 0 10px #000; }
    input, button { width:100%; padding:10px; margin:10px 0; border-radius:5px; border:none; }
    .error { color:red; text-align:center; }
  </style>
</head>
<body>
  <div class="box">
    <h2>kader11000 - Login</h2>
    {% if error %}<div class="error">{{ error }}</div>{% endif %}
    <form method="POST">
      <input type="password" name="password" placeholder="Enter password" required>
      <button type="submit">Login</button>
    </form>
  </div>
</body>
</html>
"""

main_template = """
<!DOCTYPE html>
<html>
<head>
  <title>SQLi Scanner - kader11000</title>
  <style>
    body { font-family:sans-serif; margin:30px; background:#f4f4f4; }
    h1 { color:#2c3e50; }
    .banner { background:#27ae60; padding:20px; color:white; border-radius:10px; margin-bottom:20px; }
    textarea, input, select, button { padding:10px; margin:10px 0; width:100%; border-radius:5px; border:1px solid #ccc; }
    table { width:100%; border-collapse:collapse; margin-top:20px; }
    th, td { border:1px solid #999; padding:10px; text-align:left; }
    th { background:#2c3e50; color:white; }
    .success { background:#2ecc71; color:white; }
    .danger { background:#e74c3c; color:white; }
    .button-row { display:flex; gap:10px; }
    .logout { float:right; background:#c0392b; color:white; padding:10px; border-radius:5px; text-decoration:none; }
  </style>
</head>
<body>
  <div class="banner">
    <h1>SQLi Scanner by kader11000</h1>
    <a class="logout" href="/logout">Logout</a>
  </div>

  <form method="POST">
    <label>Enter one or multiple URLs (one per line):</label>
    <textarea name="urls" rows="5" required></textarea>

    <label>Advanced SQLMap options (optional):</label>
    <input type="text" name="options" placeholder="e.g. --risk=3 --level=5">

    <div class="button-row">
      <button type="submit" name="action" value="scan">Start Scan</button>
      <button type="submit" name="action" value="stop">Stop Scan</button>
    </div>
  </form>

  {% if results %}
    <h2>Scan Results</h2>
    <table>
      <tr><th>URL</th><th>Status</th><th>Report</th></tr>
      {% for item in results %}
        <tr>
          <td>{{ item.url }}</td>
          <td class="{{ 'success' if item.status == 'Vulnerable' else 'danger' }}">{{ item.status }}</td>
          <td><a href="{{ item.report }}" target="_blank">View</a></td>
        </tr>
      {% endfor %}
    </table>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if "attempts" not in session: session["attempts"] = 0
    if session.get("attempts", 0) >= MAX_ATTEMPTS:
        if time.time() < session.get("lock_time", 0):
            return render_template_string(login_template, error="Too many attempts. Try later.")
        session["attempts"] = 0

    if request.method == "POST":
        if request.form["password"] == "kader11000":
            session["logged_in"] = True
            session["attempts"] = 0
            return redirect("/home")
        else:
            session["attempts"] += 1
            if session["attempts"] >= MAX_ATTEMPTS:
                session["lock_time"] = time.time() + LOCK_TIME
                return render_template_string(login_template, error="Locked. Try later.")
            return render_template_string(login_template, error="Incorrect password.")
    return render_template_string(login_template)

@app.route("/home", methods=["GET", "POST"])
def home():
    if not session.get("logged_in"): return redirect("/")
    results = []

    if request.method == "POST" and request.form["action"] == "scan":
        urls = request.form["urls"].splitlines()
        options = request.form.get("options", "")

        for url in urls:
            url = url.strip()
            if not url: continue
            filename = f"report_{uuid.uuid4().hex}.html"
            cmd = f'{SQLMAP_PATH} -u "{url}" --batch --output-dir=./outputs --html --flush-session {options}'
            try:
                subprocess.run(cmd, shell=True, timeout=120)
                report_path = os.path.abspath(f"./outputs/{url.replace('/', '_')}/report.html")
                report_link = f"/report/{url.replace('/', '_')}"
                status = "Vulnerable" if os.path.exists(report_path) else "Safe"
                results.append({"url": url, "status": status, "report": report_link})
            except subprocess.TimeoutExpired:
                results.append({"url": url, "status": "Timeout", "report": "#"})

    return render_template_string(main_template, results=results)

@app.route("/report/<path:filename>")
def report(filename):
    path = f"./outputs/{filename}/report.html"
    if os.path.exists(path):
        return send_file(path)
    return "Report not found", 404

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    app.run(debug=True)

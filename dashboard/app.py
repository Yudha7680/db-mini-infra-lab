from flask import Flask, render_template

app = Flask(__name__)

LOG_FILE = r"C:\db-mini-infra-lab\backup.log"

@app.route("/")
def home():
    logs = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                status = "success" if "SUCCESS" in line.upper() else "failed"
                logs.append({"text": line, "status": status})
    except:
        logs = [{"text": "Log file not found", "status": "failed"}]
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

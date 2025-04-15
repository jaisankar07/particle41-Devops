from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%A, %d %B %Y %I:%M:%S %p")
    return render_template("index.html", time=current_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

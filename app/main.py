from flask import Flask, render_template, request
from datetime import datetime
import pytz

app = Flask(__name__)

def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return ip

@app.route('/')
def home():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime("%H:%M:%S")
    user_ip = get_client_ip()
    return render_template('index.html', time=current_time, ip=user_ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

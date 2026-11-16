from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Cloud Computing Lab 8</h1>
    <p>Application Version 2</p>
    <p>Successfully deployed using Render (PaaS).</p>
    """
    # used this for initial deployment :
    # <h1>Cloud Computing Lab 8</h1>
    # <p>Application successfully implemented using Render (PaaS).</p>
    # <p>This application demonstrates Platform as a Service (PaaS).</p>

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    build_id = os.getenv('BUILD_ID', 'LOCAL')
    return f"<h1>Hello from Flask!</h1> <p> Deployed via Jenkins Webhook. Build ID: {build_id}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)'

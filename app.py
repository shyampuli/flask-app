import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    welcome_msg = os.environ.get('WELCOME_MSG', 'Welcome to my awesome Flask App!')
    return render_template('index.html', message=welcome_msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world! This is my Python application.'

app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))


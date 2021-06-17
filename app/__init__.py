import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title = "Portfolio", url = os.getenv("URL"))

@app.route('/juancarlos')
def juancarlos():
    return render_template('juancarlos.html', name = "Juan Carlos")
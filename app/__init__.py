import os
from flask import Flask, render_template, request
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', title = "Portfolio", url = os.getenv("URL"))

@app.route('/juancarlos')
def juancarlos():
    return render_template('juancarlos.html', name = "Juan Carlos")

@app.route('/health')
def health():
    return 'It Works!', 200
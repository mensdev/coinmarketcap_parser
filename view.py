from flask import render_template
from app import app
from config import db
from models import Coins
from flask import request
import json

@app.route('/')
def index():
	db.connect()
	all = Coins.select()
	return render_template('index.html', all = all)

@app.route('/getData', methods = ['POST'])
def get():
	
	return request.form
	user = request.form['user']
	return json.dumps({'status':'OK','user':user})
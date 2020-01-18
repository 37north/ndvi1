from flask import Flask, url_for, redirect, render_template, request, session
from models import db, Admin
from flask_sqlalchemy import SQLAlchemy
from forms import adminForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/parsan'
db.init_app(app)
app.secret_key = "development-key"


@app.route('/')
def index():
	return render_template('index.html')
	
	
@app.route('/adminLogin', methods = ['GET', 'POST'])
def adminLogin():
	form = adminForm()
	return render_template('adminLogin.html', form = form)
	
	
	
if '__name__ = __main__ ':
	app.run(debug=True)


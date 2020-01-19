from flask import Flask, url_for, redirect, render_template, request, session
from models import db, Admin
from flask_sqlalchemy import SQLAlchemy
from forms import adminForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/parsan'
db.init_app(app)
app.secret_key = "development-key"


@app.route('/')
def index():
	return render_template('index.html')
	
	
@app.route('/adminLogin', methods = ['GET', 'POST'])
def adminLogin():
	form = adminForm()
	
	if request.method =='POST' and form.validate() == False:
		return render_template('adminLogin.html', form = form)
	elif request.method =='POST' and form.validate() == True:
		
		app.config['SQLALCHEMY_DATABASE_URI']
		
		
		newlogin = Admin(form.username.data, form.pwdhash.data)
		db.session.add(newlogin)
		db.session.commit()
		return 'success'
			
	if request.method =='GET':
		return render_template('adminLogin.html', form = form)
	
	
	
if '__name__ = __main__ ':
	app.run(debug=True)



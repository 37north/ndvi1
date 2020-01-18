from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Admin(db.Model):
	__tablename__ = 'admins'
	uid = db.Column(db.Integer, primary_key = True)
	emailAddress = db.Column(db.String(120), unique = True)
	pwdhash = db.Column(db.String(54))
	
	def __init__(self, Email, Password):
		self.Email = Email.lower()
		self.set_password(Password)
	
	
	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)
		
	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)

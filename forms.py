from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class adminForm(Form):
	uname = StringField('User Name')
	password = PasswordField('Password')
	submit = SubmitField('Submit')
	
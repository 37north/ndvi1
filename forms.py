from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length



class adminForm(Form):
	username = StringField('User Name', validators = [DataRequired('What is your username ? ')])
	pwdhash = PasswordField('Password', validators = [DataRequired()])
	submit = SubmitField('Submit')

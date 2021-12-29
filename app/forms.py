from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SubmitField, PasswordField
)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    employee_number=StringField('employee_number', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')

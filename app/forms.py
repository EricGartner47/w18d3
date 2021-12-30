from flask_wtf import FlaskForm
from app.models import Employee
from wtforms.fields import (
    StringField, SubmitField, PasswordField, SelectField
)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    employee_number=StringField('employee_number', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')

# class AssignEmployee(FlaskForm):
#     employee_number=SelectField('Employee', choices=[])
#     table_number=

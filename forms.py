from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, email_validator


class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)],
                           render_kw={"placeholder": "Ex:  Juan Dela Cruz"})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "Ex:  juandc123@gmail.com"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "O O O O O O O O"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')],
                                     render_kw={"placeholder": "O O O O O O O O"})
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')
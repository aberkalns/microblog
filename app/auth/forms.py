from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Lietotājs', validators=[DataRequired()])
    password = PasswordField('Parole', validators=[DataRequired()])
    remember_me = BooleanField('Atcerēties mani')
    submit = SubmitField('Pieteikties')

class RegistrationForm(FlaskForm):
    username = StringField('Lietotājs', validators=[DataRequired()])
    email = StringField('E-pasts', validators=[DataRequired(), Email()])
    password = PasswordField('Parole', validators=[DataRequired()])
    password2 = PasswordField(
        'Parole atkārtoti', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reģistrēties')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Lūdzu, izmantojiet citu lietotājvārdu.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Lūdzu, izmantojiet citu e-pasta adresi.')



class ResetPasswordRequestForm(FlaskForm):
    email = StringField('E-pasts', validators=[DataRequired(), Email()])
    submit = SubmitField('Lūgt atiestatīt paroli')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Parole', validators=[DataRequired()])
    password2 = PasswordField(
        'Parole atkārtoti', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Atiestatīt paroli')

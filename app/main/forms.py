from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User

class EditProfileForm(FlaskForm):
    username = StringField('Lietotājs', validators=[DataRequired()])
    about_me = TextAreaField('Par mani', validators=[Length(min=0, max=140)])
    submit = SubmitField('Iesūtīt')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Lūdzu, izmantojiet citu lietotājvārdu.')

class PostForm(FlaskForm):
    post = TextAreaField('Izsakieties šeit', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Iesūtīt')

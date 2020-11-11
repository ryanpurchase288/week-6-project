from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError, Length
from application.models import Game, Sessions


class GameForm(FlaskForm):
    game =  StringField('Name:', validators = [DataRequired(),
            Length(min=3, max=60, message='your name is too short or long')]
    platform =  StringField('Platform', validators = [DataRequired(),
        Length(min=3, max=60, message='your name is too short or long')])
    submit = SubmitField('Submit')

class SessionForm(FlaskForm):
    time = IntegerField('Time Played(Mins):', validators = [DataRequired()])
    date = DateField('Date:', validators = [DataRequired()])
    submit = SubmitField('Submit')

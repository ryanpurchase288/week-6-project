from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError
from application.models import Game, Sessions


class GameForm(FlaskForm):
    game =  StringField('Name:', validators = [DataRequired()])
    platform =  StringField('Platform', validators = [DataRequired()])
    submit = SubmitField('Submit')

class SessionForm(FlaskForm):
    time = IntegerField('Time Played(Mins):', validators = [DataRequired()])
    date = DateField('Date:', validators = [DataRequired()])
    submit = SubmitField('Submit')

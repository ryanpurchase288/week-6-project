from application import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    platform = db.Column(db.String(30), nullable=False)
    games = db.relationship('Sessions', backref='game')

    


class Sessions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    time_played = db.Column(db.Integer, nullable=False)
    date_played = db.Column(db.DateTime, nullable=False)

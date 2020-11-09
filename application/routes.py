from flask import Flask, render_template, redirect, url_for, request
from application import app, db
from application.models import Game
from application.forms import GameForm  

@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html', gameList = Game.query.all())

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = GameForm()
    if form.validate_on_submit():
        new_game= Game(name = form.game.data, platform = form.platform.data)
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addgame.html', form=form)

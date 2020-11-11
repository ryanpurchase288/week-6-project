from flask import Flask, render_template, redirect, url_for, request
from application import app, db
from application.models import Game, Sessions
from application.forms import GameForm, SessionForm  

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

@app.route('/update/<idNum>', methods=['POST', 'GET'])
def update(idNum):
    form = GameForm()
    game = Game.query.get(idNum)
    if form.validate_on_submit():
        game.name = form.game.data
        game.platform = form.platform.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.game.data = game.name
        form.platform.data = game.platform
    return render_template('updategame.html', title='Update your game', form=form)


@app.route('/delete/<idNum>')
def delete(idNum):
    game= Game.query.get(idNum)
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/view/<idNum>', methods=['POST', 'GET'])
def viewSession(idNum):

    return render_template('viewsessions.html', sessionList = Sessions.query.filter_by(game_id=idNum).all(), game = Game.query.get(idNum)) 

@app.route('/addsession/<idNum>', methods=['POST', 'GET'])
def addsession(idNum):
    form = SessionForm()
    if form.validate_on_submit():
        new_session= Sessions(game_id = idNum, time_played = form.time.data, date_played = form.date.data)
        db.session.add(new_session)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addsession.html', form=form, game = Game.query.get(idNum))


@app.route('/deletesession/<idNum>')
def deletesession(idNum):
    session= Sessions.query.get(idNum)
    game = session.game_id
    db.session.delete(session)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/updatesession/<idNum>', methods=['POST', 'GET'])
def updatesession(idNum):
    form = SessionForm()
    session = Sessions.query.get(idNum)
    if form.validate_on_submit():
        session.time_played = form.time.data
        session.date_played = form.date.data
        db.session.commit()
        return redirect(url_for('viewSession', idNum=session.game_id))
    elif request.method == 'GET':
        form.time.data = session.time_played
        form.date.data = session.date_played
    return render_template('updatesession.html', title='Update your session', form=form, game = Game.query.get(session.game_id))













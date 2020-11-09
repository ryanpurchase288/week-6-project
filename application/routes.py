from flask import Flask, render_template, redirect, url_for, request
from application import app, db
from application.models import ToDoList
from application.forms import Game  

@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html', gameList = Game.query.all())

import unittest
from flask import url_for
from flask_testing import TestCase
from datetime import datetime
from application import app, db
from application.models import Game, Sessions

class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test registree
        game = Game(name='Skyrim', platform='Xbox')
        session1 = Sessions(game_id=1, time_played=124, date_played=datetime(2020,11,11,00,00,00))
        # save users to database
        db.session.add(game)
        db.session.add(session1)
        db.session.commit()


    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code,200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update', idNum=1))
        self.assertEqual(response.status_code,200)


    def test_deleteSession_get(self):
        response = self.client.get(url_for('deletesession', idNum=1))
        self.assertEqual(response.status_code,302)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', idNum=1))
        self.assertEqual(response.status_code,302)

    def test_view_get(self):
        response = self.client.get(url_for('viewSession', idNum=1))
        self.assertEqual(response.status_code,200)
import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Game, Sessions
from datetime import datetime



class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        app.config['SECRET_KEY'] = 'scnbuidsbcduisb'
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/ryanpurchase288_rp/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestAdd(TestBase):

    def test_add(self):
        """
        Test that a user can add a game if all the field are correctly filled out
        """


        self.driver.find_element_by_xpath("/html/body/a[2]").click()
        time.sleep(1)
        test_game_name='Skyrim'
        test_platform='Xbox'

       
        self.driver.find_element_by_xpath('//*[@id="game"]').send_keys(test_game_name)
        self.driver.find_element_by_xpath('//*[@id="platform"]').send_keys(
            test_platform)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)
        
        game = Game.query.first()
      
  
        assert url_for('index') in self.driver.current_url
        assert test_game_name ==  game.name

if __name__ == '__main__':
    unittest.main(port=5000)

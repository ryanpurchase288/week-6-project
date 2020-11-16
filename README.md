# week-6-project

## Contents
* [Brief](https://github.com/ryanpurchase288/week-6-project#brief)
  * [Objective](https://github.com/ryanpurchase288/week-6-project#objective)
  * [My Approach](https://github.com/ryanpurchase288/week-6-project#my-approach)
* [Project Planning](https://github.com/ryanpurchase288/week-6-project#project-planning)
* [Risk Assessment](https://github.com/ryanpurchase288/week-6-project#risk-assessment)
* [ERD](https://github.com/ryanpurchase288/week-6-project#erd)
* [Software Development](https://github.com/ryanpurchase288/week-6-project#software-development)
  * [index](https://github.com/ryanpurchase288/week-6-project#index)
  * [add game](https://github.com/ryanpurchase288/week-6-project#add-game)
  * [add session](https://github.com/ryanpurchase288/week-6-project#add-session)
  * [view sessions](https://github.com/ryanpurchase288/week-6-project#view-sessions)
* [Testing](https://github.com/ryanpurchase288/week-6-project#testing)
* [Improvements](https://github.com/ryanpurchase288/week-6-project#improvements)
* [Evaluation](https://github.com/ryanpurchase288/week-6-project#evaluation)


## Brief

### Objective
"To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training."

This was the objective I have to complete and to break it down it means I have to create an application
which can Create, Read, Update and, Delete records from a database

### My Approach
To fulfill the requirements set out for me I made an application which can be used by anyone who has an interest is monitoring the game sessions and this application will allow the users to:

* Add a game
  * Game Name
  * Game Platform
 * Add a session
  * Time played
  * Date played
 * View and update all the records they have added
 * Delete the games and/or sessions


## Project Planning
Here is a link to my trello board:https://trello.com/b/orijlmtZ/week-6-project

![Trello Board](https://github.com/ryanpurchase288/week-6-project/blob/main/images/trello.PNG?raw=true)

I have kept this updated as I have completed tasks for me to complete.



## Risk Assessment
Here is a link to my risk assessment:
https://1drv.ms/x/s!Av4eZvsa3rmzl339kxYvGHdAFH-I?e=d2SXho

![risk_assessment](https://github.com/ryanpurchase288/week-6-project/blob/main/images/risk_assessment.PNG?raw=true)


## ERD
![ERD](https://github.com/ryanpurchase288/week-6-project/blob/main/images/Project_ERD.png?raw=true)

This is my Entity Relationship Diagram. I decided not to include the description of the Game from the Game table just for display reasons on the flask page as it was not a neccessary data to have in the table.

## Application Structure
When creating the application I used a VCS to ensure versioning of my application throughout the development build and for this GitHub was used.

I used Jenkins as the CI server for my application which will set off automatically install the required requirements to run the application and also to build an artifact of my application as show below:
![jenkins](https://github.com/ryanpurchase288/week-6-project/blob/main/images/jenkinsVM.PNG)
![jenkins_running](https://github.com/ryanpurchase288/week-6-project/blob/main/images/jenkins.PNG)
![artifacts](https://github.com/ryanpurchase288/week-6-project/blob/main/images/artifact.PNG)

I have used PyTest and Selenium to perform the automatic testing of my application for unit and intergration.

The application will run Google Cloud Platform VM instnace using an SQL intsnace as well.


## Software Development
### index
![index](https://github.com/ryanpurchase288/week-6-project/blob/main/images/index.PNG)
### Add Game
![add](https://github.com/ryanpurchase288/week-6-project/blob/main/images/addGame.PNG)
### Add Session
![session](https://github.com/ryanpurchase288/week-6-project/blob/main/images/addSession.PNG)
### View Sessions
![view](https://github.com/ryanpurchase288/week-6-project/blob/main/images/editSession.PNG)

## Testing
This is the test coverage I have achieved on my project:
![Test Coverage](https://github.com/ryanpurchase288/week-6-project/blob/main/images/coverage.PNG)

I have conducted both unit testing and intergration testing. With unit testing I conducted tests which ensures all the pages/views can be accessed by the user. I also tests the functions for adding a game and a session to make sure the tables are related and working together. I also tested the update function to ensure that it is able to read and update the data.  I have planned to also do the delete test to ensure that the full CRUD application is working. 

## Improvements
If given more on this project I would have wanted to include these following feature:
* Jenkins running my application as a Systemd service in the background
* Include custom made validators on my data entry fields
* Include a platform table so users have to add a platform before adding a game and instead in the game table include a dynamic select field showing only the platforms added instead of a text field
* Create a login system so more than one person can use it.
* add a filtering system on the games view so for example they can filter by platform.

## Evaluation 
Within the time frame I have been given I have achieved the MVP for the project knowing full well I could have made a better application which is one more user friendly and two shows what I am actually fully able to be able to do.

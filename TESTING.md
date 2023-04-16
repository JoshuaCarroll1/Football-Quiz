# Testing

Return back to the [README.md](README.md) file.


## Code Validation


### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.


| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JoshuaCarroll1/football-quiz/main/run.py) | ![screenshot](documentation/py-validation-run.png) |  |
| questions.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JoshuaCarroll1/football-quiz/main/questions.py) | ![screenshot](documentation/py-validation-run.png) |  |

## Lighthouse Audit


I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Heroku | Mobile | ![screenshot](documentation/lighthouse1.png) | Some minor warnings |
| Heroku | Desktop | ![screenshot](documentation/lighthouse2.png) | Some minor warnings |

## Defensive Programming


Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| run.py | | | | |
| | Enter username | User should enter valid username | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |


## User Story Testing



| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to be able to add my name, so that I can be called my name. | ![screenshot](documentation/pic11.png) |
| As a new site user, I would like to get random questions, so that I can answer questions. | ![screenshot](documentation/pic2.png) |
| As a new site user, I would like to see how many questions I got correct, so that I can see how many I got incorrect. | ![screenshot](documentation/pic3.png) |
| As a returning site user, I would like to see new questions, so that I can answer different questions. | ![screenshot](documentation/pic2.png) |
| As a returning site user, I would like to be able to replay the game within the game, so that I can quickly restart the quiz. | ![screenshot](documentation/pic4.png) |
| As a returning site user, I would like to see what questions I get wrong, so that I can correct them in the future. | ![screenshot](documentation/pic5.png) |


## Unfixed Bugs

There are no remaining bugs that I am aware of.

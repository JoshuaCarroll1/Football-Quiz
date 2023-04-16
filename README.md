# FOOTBALL QUIZ


## UX


## User Stories


### New Site Users

- As a new site user, I would like to be asked to enter username, so that I can start the game.
- As a new site user, I would like to be asked a question, so that I can answer the question.
- As a new site user, I would like to be asked multiple different questions, so that I can have different answers.
- As a new site user, I would like to be given answers to pick from, so that I can have a chance to guess a question.
- As a new site user, I would like to told my score at the end, so that I can see the score I got.

### Returning Site Users

- As a returning site user, I would like to see different questions then prior, so that I can answer new questions.
- As a returning site user, I would like to see my score, so that I can compare to other scores of mine.
- As a returning site user, I would like to see how many I got incorrect, so that I can get less wrong.
- As a returning site user, I would like to find out which ones i got wrong, so that I can know the answer for next time.
- As a returning site user, I would like to have a replay button, so that I can replay without restarting the app.


## Features


### Existing Features

- **Username input #1**

    - Here you can enter a name between 4 and 15 letters and get a printed line back with your name in it ready to begin the game!

![screenshot](documentation/pic1.png)

- **Multiple different questions #2**

    - Made a possible 30 questions with 30 different answers!

![screenshot](documentation/pic2.png)

- **Give a Correct score #3**

    - At the end of the quiz give the user their correct score!

![screenshot](documentation/pic3.png)

- **Give a incorrect score #4**

    - At the end of the quiz give the user their incorrect score!

![screenshot](documentation/pic3.png)

- **Give an option to replay within game #3**

    - At the end of the quiz give the user a chance to replay the quiz!

![screenshot](documentation/pic4.png)


### Future Features


- Scoreboard #1
    - Scoreboard to show all people who answered the quiz.
- More Questions #2
    - Add more questions so people can continue to play.
- Randomise answers #3
    - Rather then answers being set to a, b, c, d I would like for the answers to be randomized.

## Tools & Technologies Used


- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.

## Data Model

### Flowchart


Below is the flowchart of the main process of this Python program. It shows the entire cycle of the program.

![screenshot](documentation/flowchart.png)

### Classes & Functions



The primary functions used on this application are:

- `username_setup()`
    - Get username input from the user.
- `opening_logo()`
    - Opening logo for game saying "FOOTBALL QUIZ".
- `clear()`
    - Function used to clear app page.
- `game_setup()`
    - Give user a welcome to game with text.
- `validator_username()`
    - Validate username with else/if statements.
- `questions_validator()`
    - Get questions for game and validate answers given.
- `end_game()`
    - End game text and scores.
- `replay_game()`
    - Give option for user to replay game with y/n.
- `__name__()`
    - Main function to run programs.

### Imports

I've used the following Python packages and/or external imported packages.

- `colorama`: used for including color in the terminal

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://footballquiz.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.


#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/JoshuaCarroll1/Football-Quiz) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/JoshuaCarroll1/Football-Quiz.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JoshuaCarroll1/Football-Quiz)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JoshuaCarroll1/Football-Quiz)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment


Space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.


## Credits


### Content


| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/python/ref_string_isalpha.asp) | entire page | how to use isalpha |
| [Programiz](https://www.programiz.com/python-programming/methods/string/isalpha) | entire site | how to use isalpha |

### Media


| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [colorama](https://pypi.org/project/colorama/) | entire site | code | colours on page |

### Acknowledgements


- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my parents, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my family, for supporting me in my career development change towards becoming a software developer.

# FREE THE BEES GAME IN PYTHON

Free the Bees is a command line game built in Python designed based on the idea of Battleships... but for people who would prefer not to think about explosions. A simple yellow display brightens peoples day and they can enjoy the fun of finding the bees and feeding them.
Bees are crucial to the planet as we know it. Colony Collapse Disorder was first seen in Southern and Western Europe in 1998, and it was named in 2006 in North America. It is now a world wide occurance that we still don't fully understand.
This game aims to provide entertainment while highlighting the importance of these very clever insects.

![Screenshot of Free the Bees]( "Free the Bees on Am I Responsive")

[View Free the Bees Live Site](https://fed-the-bees-4595451a08dc.herokuapp.com/)

![GitHub contributors](https://img.shields.io/github/contributors/kellie-cat/fed-the-bees)
![GitHub top language](https://img.shields.io/github/languages/top/kellie-cat/fed-the-bees)
![GitHub last commit](https://img.shields.io/github/last-commit/kellie-cat/fed-the-bees)

---

## CONTENTS

- [FREE THE BEES](#free-the-bees)
  - [CONTENTS](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Key information for the site](#key-information-for-the-site)
      - [Goals](#goals)
      - [First Time User Goals](#first-time-user-goals)
      - [Returning Visitor Goals](#returning-visitor-goals)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Lucidchart](#lucidchart)
  - [Features](#features)
    - [General features](#general-features)
      - [The Welcome Page](#the-welcome-page)
      - [The Game Page](#the-game-page)
    - [Future Implementations](#future-implementations)
    - [Accessibility](#accessibility)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Deployment \& Development](#deployment--development)
    - [Playing on a Local machine or via Gitpod Terminal](#playing-on-a-local-machine-or-via-gitpod-terminal)
    - [Final Deployment to Heroku](#final-deployment-to-heroku)
  - [Testing](#testing)
    - [Resolved Bugs](#resolved-bugs)
    - [Known Bugs](#known-bugs)
  - [Credits](#credits)
    - [Code Used](#code-used)
    - [Content](#content)
    - [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

Free the Bees is a command line game played on one screen with elements that update to progress the game and give the user feedback. It is deployed to Heroku to ensure accessibility for users.

### Key information for the site

- A Title Art welcomes the new user to the game and invites them to commence playing.
- A back story and instructions draw the player in and asks them for their name at the end - input required is highlighted by a different colour.
- The users guess where they think they can help the bees, and they are rewarded with a unicode bee if they are successful, or a unicode empty hexagon commisserates if they didn't find a bee.
- At each turn, the user confirms they would like to keep playing, so they don't get stuck in a long loop.
- Finally, their score is displayed and the user is invited to refresh the game to play again or exit the program.

#### Goals

- To have a fun game.
- To have a program that runs smoothly and is accessible both visually and logistically.
- To prevent the game from crashing due to user input.
- To highlight the importance and the plight of bees in nature.

#### First Time User Goals

- I want to play a game that is intuitive and instructions are easy to follow.
- I want to view the information in an aesthetically pleasing and intuitive way.
- I want to navigate through the game easily and get clear feedback.
- I want a game that does not crash.

#### Returning Visitor Goals

- I want familiarity that improves UX by creating an feeling of ease of use.
- I want a program that offers the chance to leave if I need to.
- I want a game that does not crash.

## Design

### Colour Scheme

Python has a limited amount of colours and styles in the Colorama module.
The obvious choice is a use of Yellow and Black to symbolise the bees and I choose Red text to symbolise the feedback for a hangry Bee when they are not fed, and Green text to celebrate a successfully fed bee to encourage the user to keep going.
When user input is needed, the text turns Cyan to alert the player that their interaction is needed.

### Typography

[Geeks for Geeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) gave a tutorial on ASCII art using the pyfiglet module and I decided to use a font that resembled the hexagons in a bee hive because it is easy to read and on theme.

![Screenshot of Welcome Art]( "Screenshot of fonts")

### Lucidchart

- I found the logic of this project really difficult and tangled myself in a number of knots.
- Lucidchart had a number of different drafts.

![Lucidchart Draft 1](docs/flowcharts/lucidchart-pp3-draft.png)
Lucidchart Attempt 1 of Many 

- As I ended up simplifying the game so I could get my head around it, it changed quite a bit.

![Lucidchart Edited version](docs/flowcharts/lucidchart-pp3-edited.png)
Lucidchart Edited Version


## Features

### General features

#### The Title Art

- When users first load the page, the Title Art is displayed to
  - welcome the user and 
  - introduce the name of the game

![A screenshot of the Title Art](docs/screenshots/pp3-title-art.png "Screenshot of the Title Art")

#### The Backstory and Instructions

- Once the user has confirmed they are ready, the backstory of the game is revealed with instructions on how to play. 
- The player is asked to enter their name and this is validated before moving on.
- Then the player is asked to confirm they would like to proceed.

![A screenshot of the backstory](docs/screenshots/pp3-instructions.png "Screenshot of the backstory")

#### The Hive
After each turn, the user is asked if they would like to
- continue
- or exit

![A screenshot of early exit](docs/screenshots/pp3-early-exit.png "Screenshot of early exit")

Once they have confirmed they would like to proceed, the player sees
  - a visual display of the bee hive where the bees are trapped
  - a request for input a row and column they think the bee is trapped in

![A screenshot of the hive](docs/screenshots/pp3-hive-continue.png "Screenshot of the hive")

#### Feedback
  - tells the user if they fed a bee

![A screenshot of the feedback](docs/screenshots/pp3-positive-feedback.png "Screenshot of positive feedback")

  - or tells them if they missed

![A screenshot of the feedback](docs/screenshots/pp3-negative-feedback.png "Screenshot of negative feedback")

- and if they make a duplicate guess, it lets them know they can try again

![A screenshot of the feedback](docs/screenshots/pp3-duplicate-guess.png "Screenshot of duplicate guess")

#### Final feedback
If they choose to complete all the turn,when the player is out of turns and the game is over
  - the players get their final score
  - along with some personalised feedback

![A screenshot of final results](docs/screenshots/pp3-final-positive.png "Screenshot of final results")

#### Finish the game
 When they have finished, the player is invited 
- to play another round
- or exit

![A screenshot of finish game](docs/screenshots/pp3-finish-game.png "Screenshot of finish game")

#### Validations
If the player enters an invalid answer
- they have a chance to retry without crashing the game
- and they receive some feedback on how to make a valid guess

![A screenshot of invalid input](docs/screenshots/pp3-row-validation.png "Screenshot of row validation")

![A screenshot of invalid input](docs/screenshots/pp3-column-validation.png "Screenshot of column validation")

### Future Implementations

This project meets the requirements and is ready to play without issues.
If more resources opened up, I could add some additional features:

1. It would be interesting to have the time to work with more features such as the background image, placing the terminal centered in the screen and so on.
2. Varying the mode from 'easy' to 'difficult' would be helpful to make the game even more useful for people of interest levels. This could be achieved by creating a class for the Hive and asking the using to input a SIZE between say 5 and 15.
4. Adding game sounds and more exciting animations would increase interest and novelty.

### Accessibility

I have tried to be inclusive for everyone when coding this website by

- Using clear instructions
- Asking for user input before continuing
- Validating inputs before moving on to the next step
- Using interesting colours and icons
- Testing the game to make sure it does not crash from user input

## Technologies Used

### Languages Used

This game was made using Python.

### Frameworks, Libraries & Programs Used

[Lucidchart](https://www.lucidchart.com/) - To build a flowchart.

[Github](https://github.com/Code-Institute-Org/ci-full-template) - To save and store files for the website.

[Codeanywhere](https://dashboard.codeanywhere.com/) - To write the code.

[Geeks for Geeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) - To learn how to import pyfiglet to make ASCII Title Art.

[Font Awesome](https://fontawesome.com/) - For the icons and the favicon.

[Python OOP Tutorial Playlist by Corey Shafer](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) - To learn how to use Python.

[Favicon](https://favicon.io/) - To convert the favicon from an icon.

[Am I Responsive?](https://ui.dev/amiresponsive) - To display the website on a range of screen sizes.

[Python validator](https://pythontutor.com/visualize.html#mode=display) - To test Python.

[Shields](https://shields.io/) - To display the shield icons in this document.

## Deployment & Development

### Playing on a Local machine or via Gitpod Terminal
This project was developed using a [specialized Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser. Due to this, I optimized the game to work by deploying the [final version on Heroku](), and I do not recommend playing it locally. I have included this section for completeness.  
1. Navigate to the [GitHub repository](https://github.com/kellie-cat/fed-the-bees), and follow [these steps to clone the project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) into your IDE of choice.   
   
   * **Gitpod** only **requires** you to have the **web extension** installed and **click** the **green Gitpod button** from the repositories main page. If you are **using Gitpod** please **skip step 2** below as you do not need a virtual environment to protect your machine.  
  
1. **Create** the **virtual environment** with the terminal command **"python3 -m venv venv".** Once complete add the "venv" file to you're ".gitignore" file and use the terminal command **"venv\Scripts\activate.bat" to activate it.**
   
   * **IMPORTANT** If developing locally on your device, ensure you **set up/activate the virtual environment before installing/generating the requirements.txt file**; failure to do this will pollute your machine and put other projects at 
 
1. **Install the requirements** listed in requirements.txt using the terminal command  **"pip3 install -r requirements.txt"**
   * Kindly note that since I developed the project from scratch and installed the required libraries as progressed **I have already included a requirements.txt for this app** by using the terminal command **"pip3 freeze > requirements.txt"** to generate it.

## Final Deployment to Heroku
  
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
1. **Log in to Heroku** or create an account if you don't already have one.
1. **Click** the button labeled **New** from the dashboard in the top right corner, just below the header.
1. From the drop-down menu **select "Create new app"**.
1. **Enter a unique app name**. I called this one "fed-the-bees".
1. Once the web portal shows the green tick to confirm the name is original **select the relevant region.** I left mine as Ireland.
1.  When happy with your choice of name and that the correct region is selected, **click** on the **"Create app" button**.
1. This will bring you to the project "Deploy" tab. From here, navigate to the **settings tab** and scroll down to the **"Config Vars" section**. 
1. **Click** the button labelled **"Reveal Config Vars"** and **enter** the **"key" as port**, the **"value" as 8000** and **click** the **"add"** button.
1. Scroll down to the **buildpacks section of the settings page** and click the button labeled **" add buildpack," select "Python," and click "Save Changes"**.
1. **Repeat step 11 but** this time **add "node.js" instead of python**. 
   * **IMPORTANT** The buildpacks must be in the correct order. If node.js is listed first under this section, you can click on python and drag it upwards to change it to the first buildpack in the list.
1. Scroll back to the top of the settings page, and **navigate to the "Deploy" tab.**
1. From the deploy tab **select Github as the deployment method**.
1. **Confirm** you want to **connect to GitHub**.
1. **Search** for the **repository name** and **click** the **connect** button next to the intended repository.
1. From the bottom of the deploy page **select your preferred deployment type** by follow one of the below steps:  
   * Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.  
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment. 

## Testing

The game was tested as it was built with Python, using the commands **pylint** and **pystylecode**.

The relevant validator for Python, [Code Institute PEP8 Python Linter](https://pep8ci.herokuapp.com/) was used to check the code.

![Python validation](docs/screenshots/pp3-pep8-validation.png "Screenshot of Python Validation")

### Resolved Bugs

Many issues were discovered and resolved throughout the project.

1. Trial and error and patience are key. Many times I tried many lines of code that did not work. I learned to just keep trying. Keep calm. Keep breathing.
1. **Issue**: Import sys
   **Cause**:   
   **Solution**: 

### Known Bugs

There are no unfixed bugs in Free the Bees.

## Credits

### Code Used

- [Kera Cudmore's README.md for the Bully Book Club](https://github.com/kera-cudmore/Bully-Book-Club)
- [David Bower's README.md for Battleships](https://github.com/dnlbowers/battleships/blob/main/README.md)
- [Python OOP Tutorial Playlist by Corey Shafer](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- [Geeks for Geeks leeson on ASCII art](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)

### Content

Concept and content written by Kellie McConnell, a human tired of the normalisation of violence and war.

### Acknowledgments

Thank you so much to everyone who helped me in this project.

- Corey Shafer from YouTube [Python OOP Tutorial Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc). Nothing about classes, or Python in general, really clicked until these. I should have made time to watch them earlier.

- David Bowers, my Code Institute Mentor, thank you for your patience in the face of my panic and hopelessness.

- Rohit Sharma, for fitting me in for an extra mentor session to help me simplify the tangle I created.

- My husband, William Wong, for feeding me and giving me peace to code.
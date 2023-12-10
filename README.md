# FREE THE BEES GAME IN PYTHON

Free the Bees is a command line game built in Python designed based on the idea of Battleships... but for people who would prefer not to think about explosions. A simple yellow display brightens peoples day and they can enjoy the fun of finding the bees and feeding them.
Bees are crucial to the planet as we know it. Colony Collapse Disorder was first seen in Southern and Western Europe in 1998, and it was named in 2006 in North America. It is now a world wide occurance that we still don't fully understand.

![Screenshot of Free the Bees]( "Free the Bees on Am I Responsive")

[View Free the Bees on Github Pages](https://kellie-cat.github.io/fed-the-bees/)

![GitHub contributors]()
![GitHub top language]()
![GitHub last commit]()

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
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [General features](#general-features)
      - [The Welcome Page](#the-welcome-page)
      - [The Game Page](#the-game-page)
    - [Future Implementations](#future-implementations)
    - [Accessibility](#accessibility)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Deployment \& Local Development](#deployment--local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  - [Testing](#testing)
    - [Resolved Bugs](#resolved-bugs)
    - [Known Bugs](#known-bugs)
  - [Credits](#credits)
    - [Code Used](#code-used)
    - [Content](#content)
    - [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

Free the Bees is a command line game played on one screen with elements that update to progress the game and give the user feedback. It was designed to be played on... screen size? Mention mobile-first???

### Key information for the site

- A header with a title introducing the page and a logo.
- A welcome page with instructions for the new user to commence playing.
- A pop up at the end to give a final score and feedback and invite the user to refresh the game to play again.
- Links to find out more about me include my LinkedIn and GitHub profiles which open in a new tab.

#### Goals

- To have an interactive site that is responsive for screen sizes from handheld devices to larger monitors.
- To have a site that is intuitive and accessible both visually and for people using screen readers.
- To highlight the importance and the plight of bees in nature.
- To provide resources to find out more about me and other projects.

#### First Time User Goals

- I want to play a game that is intuitive and instructions are easy to follow.
- I want to view the information in an aesthetically pleasing and intuitive way.
- I want to navigate through the game easily and get clear feedback.

#### Returning Visitor Goals

- I want familiarity that improves UX by creating an feeling of ease of use.
- I want to know how to contact the page to ask any questions I may have.

## Design

### Colour Scheme

Python has a limited amount of colours and styles in the Colorama module.
The obvious choice is a use of Yellow and Black to symbolise the bees and I choose Red text to symbolise a hangry Bee when they are not fed, and Green text to celebrate a successfully fed bee to encourage the user to keep going.

### Typography

[Geeks for Geeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) gave a tutorial on ASCII art using the pyfiglet module and I decided to use a font that resembled the hexagons in a bee hive because it is easy to read and on theme.

![Screenshot of Welcome Art]( "Screenshot of fonts")

### Wireframes

![A screenshot of Balsamiq wireframe trial for PP2](docs/balsamiq-wireframe-dental-quiz.png "Balsamiq wireframe trial for PP2")
Balsamiq wireframes were trialed to plan the project layout.

I ended up changing the colours and layout to improve the aesthetics and usabilty of the site on mobile through to large monitor screen sizes and orientations. I realised there was no point in trying to force content into a small area.

## Features

### General features

The game

#### The Welcome Page

![A screenshot of the home page](docs/pp2-welcome-page-laptop.png "Screenshot of the home page")

- When users first load the page, the home page is displayed to
  - welcome the user and introduce the game
  - explain the purpose of the game
  - provide instructions
  - begin the game with a start button
  - the header and footer are a constant throughout, with Font Awesome icons
  - the header has a tooth, setting the theme for the quiz
  - and the foooter has links to LinkedIn and GitHub, which open in a new tab, incase anyone would like to find out more about me

![A screenshot of the header on a mobile device](docs/pp2-header-mobile.png "Screenshot of the header on a mobile device")

![A screenshot of the footer on a mobile device](docs/pp2-footer-mobile.png "Screenshot of the footer on a mobile device")

#### The Quiz Page

Again the header and footer appear, familiar to the user.
On this page, the header is also an anchor tag, linking the user back to the home page, should they need to stop the game before it is finished.

![A screenshot of the quiz page](docs/pp2-quiz-page-laptop.png "Screenshot of the quiz page")

The majority of the page is the Game Area, containing:

- a Question and Answer area
  - with 3 multiple choice answers contained in buttons
  - a different coloured button to move to the next page

![A screenshot of the question area](docs/pp2-question-area.png "Screenshot of the question area")

- a Feedback area which
  - tells the user if they got the question correct or incorrect
  - and when they answer correctly, an explaination of the correct answer appears

![A screenshot of the feedback area](docs/pp2-feedback-correct.png "Screenshot of the feedback area")

- if an incorrect answer is given then a window opens to warn the user that answer was not correct and a background container hides the quiz until the user closes the incorrect answer window

![A screenshot of the incorrect window](docs/pp2-incorrect-window-mobile.png "Screenshot of the incorrect window")

- if the user answers incorrectly, they cannot move onto the next question, becuase the aim of the game is to get information across. They have to keep trying until they find the right answer and get a short explaination
- the incorrect answer also disables so they can't put the same wrong answer in twice by mistake, and this is highlighted to the user with a cursor change and the answer that has already been tried remains highlighted

![A screenshot of an incorrect answer highlighted](docs/pp2-game-area-laptop-incorrect.png "Screenshot of an incorrect answer highlighted")

- a Score area which keeps a tally of correct and incorrect answers

![A screenshot of the score area](docs/pp2-score-area-tablet.png "Screenshot of the score area")

- When the game finishes, another window opens to
  - give the users their final score
  - along with some personalised feedback
  - and invites them to refresh the game

![A screenshot of final results](docs/pp2-final-result-mobile.png "Screenshot of final results")

### Future Implementations

This project meets the requirements and is ready to help many people learn about cavity prevention.
If more resources opened up, I could add some additional features:

1. A progress bar displayed so the player could tell how many questions they had to go.
2. An 'easy', 'moderate' and 'difficult' mode would be helpful to make the game even more useful for people of different knowledge levels. This could be achieved by creating another document for holding the data and separate arrays for easy, moderate and difficult questions. Hints could also be displayed in the Incorrect Answer pop up.
3. Scrambling the order of the answers would also make the game more helpful for repeat users. This could be achieved by calling the answers in a different way and again shuffling the order with the Fisher Yates Method.
4. Adding game sounds and more exciting animations would increase interest and novelty.
5. Providing a link to sites such as [The Irish Dental Health Foundation](https://www.dentalhealth.ie/) or [Brush My Teeth](https://brushmyteeth.ie/) to signpost the users to more educational resources.

### Accessibility

I have tried to be inclusive for everyone when coding this website by

- Using aria labels when appropriate for people using screen readers.

- The EightShapes Contrast Grid was helpful with matching background and text colours with good contrast and making sure text is an appropriate size on all types of screen.

![Colour Grid screenshot](docs/contrast-grid-pp2.png "Colour Grid screenshot")

- Using semantic HTML as much as possible.

- Testing the website with Wave and Lighthouse.

## Technologies Used

### Languages Used

This website was made using JavaScript, HTML and CSS.

### Frameworks, Libraries & Programs Used

[Balsamiq](https://balsamiq.com/givingback/free/classroom/) - Used to create wireframes.

[Github](https://github.com/Code-Institute-Org/ci-full-template) - To save and store files for the website.

[Codeanywhere](https://dashboard.codeanywhere.com/) - To write the code.

[Geeks for Geeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) - To learn how to import pyfiglet to make ASCII Title Art.

[Font Awesome](https://fontawesome.com/) - For the icons and the favicon.

[Coolors](https://coolors.co/) - For inspiration for a colour palette.

[Art In Context](https://artincontext.org/color-palette-generator/) - To build a custom colour palette.

[EightShapes Contrast Grid](https://contrast-grid.eightshapes.com/) - To improve accessibilty with colours.

Google Chrome Development Tools - To test the code as I was writing it, and to troubleshoot and isolate issues with styling, as well as test accessibilty with Lighthouse.

[Wave](https://wave.webaim.org/) - To evaluate accessibility.

[Favicon](https://favicon.io/) - To convert the favicon from an icon.

[Am I Responsive?](https://ui.dev/amiresponsive) - To display the website on a range of screen sizes.

[Python validator](https://pythontutor.com/visualize.html#mode=display) - To test Python.

[Shields](https://shields.io/) - To display the shield icons in this document.

## Deployment & Local Development

### Deployment

Github Pages was used to deploy the live website. The instructions to achieve this are:

1. Log in (or sign up) to Github.
2. Find the repository for this project, kellie-cat/fed-the-bees.
3. Click on the Settings link.
4. Click on the Pages link in the left hand side navigation bar.
5. In the Source section, ensure Deploy from a branch is selected, and choose main from the drop down select branch menu. Select Root from the drop down select folder menu.
Click Save.
Your live Github Pages site is now deployed at the URL shown.

### Local Development

#### How to Fork

To fork the Free the Bees:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, kellie-cat/fed-the-bees.
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the Cavity Prevention Quiz:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, kellie-cat/fed-the-bees.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Testing

The website was tested as it was built on Google Chrome using Google Devtools. It was designed with a mobile-first mindset and other screensizes were adjusted using media queries. Other browsers were tested.

Once the website was complete, it was tested with Wave and Lighthouse for accessibility.

Lighthouse Home page on desktop
![Lighthouse Home page on desktop](docs/pp2-lighthouse-index-desktop.png "Lighthouse Home page on desktop")

Lighthouse Home page on mobile
![Lighthouse Home page on mobile](docs/pp2-lighthouse-index-mobile.png "Lighthouse Home page on mobile")

Lighthouse Quiz Page on desktop
![Lighthouse Quiz Page on desktop](docs/pp2-lighthouse-quiz-desktop.png "Lighthouse Quiz Page on desktop")

Lighthouse Quiz Page on mobile
![Lighthouse Quiz Page on mobile](docs/pp2-lighthouse-quiz-mobile.png "Lighthouse Quiz Page on mobile")

The relevant validators were used to check all of the HTML, CSS and JavaScript on the site.

![Home Page HTML validation](docs/html-validation-pp2.png "HTML validation for Home Page")

![Quiz Page HTML validation](docs/html-quiz-validation-pp2.png "HTML validation for Quiz Page")

![CSS validation](docs/css-validation-pp2.png "CSS validation")

![JavaScript validation](docs/pp2-javascript-validation.png "JavaScript validation")

JSHint showed one constant that had not been used, so this was removed.
Then it showed the following warning. As this was not an error, it was not resolved in this project, but it is something I will be conscious of in future.

I checked Google and Slack for solutions and it seems to be a common issue. Sadly there is no specific way to correct it. From this research, I did change the var keyword to a let keyword to be more inline with modern practices and to prevent unexpected results from global scope.

### Resolved Bugs

Many issues were discovered and resolved throughout the project.

1. Trial and error and patience are key for JavaScript. Many times I tried many lines of code that did not work. I learned to just keep trying.
2. **Issue**: I thought I had correctly programmed the correct and incorrect scores to increment... only to discover the incorrect score kept going up if the user clicked on the wrong answer again.  
   **Cause**: The answer buttons were still able to be clicked and the event listenter kept calling the relevant increment score functions when they were clicked.  
   **Solution**: I fixed this issue by disabling the incorrect buttons once they were pressed, when the next question button is pressed, all buttons become active again.
3. **Issue**: I wanted to highlight the feedback area when it was given, and tried to add animation. This proved difficult.  
   **Cause**: I am not familiar with frameworks and libraries yet and hope to learn more in the future.  
   **Solution**: I eventually settled on a simpler CSS animation and added JavaScript frameworks and libraries to my learning goals.
4. **Issue**: The index.html page returned a JavaScript error during testing.  
   **Cause**: The index.html page does not have the relevant HTML elements for the JavaScript to run.  
   **Solution**: I used an If statement to set the JavaScript to only run on the quiz.html URL. This in turn caused an issue...
5. **Issue**: The testing URL and the deployed URL are not the same! So the JavaScript did not run for testing if I set the URL as the deployed page.  
   **Cause**: Murphy's law.  
   **Solution**: I pushed the If statement to make sure it worked. Then commented it out until the final save. Which in turn caused another issue...
6. **Issue**: The need to remember to uncomment the code at the final save.  
   **Cause**: My memory. Or lack of.  
   **Solution**: A reminder! A reminder handwritten in my notebook, in CAPS above the commented out code, on my wall calendar and in my phone calendar app! In amongst all the other reminders, this is a foolproof solution!
7. **Issue**: The disabling of the already tried incorrect answers was inconsistent.  
   **Cause**: After much testing, I worked out that the function disableIncorrectRef which called elements by class name 'active', only worked on the first element it found with the class name active. So if I clicked the 3rd button 1st, it was disabled, and either of the 1st or 2nd would also be correctly disabled. However, if the 1st button was clicked and disabled, then the 2nd or 3rd buttons would remain active.  
   **Solution**: I tried to add 'disabled' as a class and then set pointer-events: none. However this was not ideal, as it also meant the cursor: not-allowed effect did not work. I decided to add an attribute of disabled to the button with the event listener. This was already removed by the nextQuestion function.

### Known Bugs

There are no unfixed bugs in Free the Bees.

## Credits

### Code Used

- [Kera Cudmore's README.md for the Bully Book Club](https://github.com/kera-cudmore/Bully-Book-Club)
- 
- [Geeks for Geeks leeson on ASCII art](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)

### Content

Concept and content written by Kellie McConnell, a human tired of the normalisation of violence and war.

### Acknowledgments

Thank you so much to everyone who helped me in this project.

- David Bowers, my Code Institute Mentor, thank you for your patience in the face of my panic and hopelessness.

- Rohit Sharma, for fitting me in for an extra mentor session to help me simplify the tangle I created.

- My husband, William Wong, for feeding me and giving me peace to code.
## SoftwareCarpentryWC3
In this weeks lab for Software Carpentry, I have created a website using the built-in feature of GitHub, called “GitHub Pages”. Using a fairly simple I first made a new repository (SoftwareCarpentryWC3), a website, and added that website to the repository. To visit a website should you choose to make one yourself: go to the website “USER.github.io/REPO”, where “USER” is your GitHub username, and “REPO” is the name of
your repository.
## Table of Content
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Example of Use](#example-of-use)
* [Sources](#sources)
* [File List](#file-list)
## General Info
This project prints a simple Hello World on the console.
This project adds together all the even numbers between 1 and 100, and prints that value to the terminal
## Technologies
Project is created with:
* Python version: 3.7.3
* Sublime Text version: 3.2.1
Project uses:
* Anaconda Prompt version: 3.2.1
## Setup
To run this project, install it locally using npm:
## Example of Use
To add together all the even numbers between 1 and 100. Then displays that number to the terminal. <br>
def mundaneMath(): <br>
    # This is an empty array to store the even numbers <br>
    a = [] <br>
    # A loop to increment from 1 to 100 <br>
    for i in range(1, 101): <br>
        # This finds the even numbers from 1 to 100 <br>
        # and stores them in the array <br>
        if (i % 2 == 0): <br>
            a.append(i) <br>
    # Adds the even numbers together and stores them in the variable x <br>
    x = sum(a) <br>
    # Prints the output <br>
    print(x) <br>
## Sources
EN.540.635 - Software Carpentry by Henry C. Herbol
## File List
Project contains the following files in the repository:
* mundaneMath.py - Located in the master branch
* hello.py - Located in the master branch
* index.html - Located in the gh-pages branch (pushed to the origin)
* .nojekyll - Located in the gh-pages branch (pushed to the origin)

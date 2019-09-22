## SoftwareCarpentryWC3
In this weeks lab for Software Carpentry, I have created a website using the built-in feature of GitHub, called “GitHub Pages”. Using a fairly simple I first made a new repository, a website, and added that website to the repository. To visit a website should you choose to make one yourself: go to the website “USER.github.io/REPO”, where “USER” is your GitHub username, and “REPO” is the name of
your repository.
## Table of Content
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Scope of Functionality](#scope-of-functionality)
* [Example of Use](#example-of-use)
* [Illustration](#illustration)
* [sources](#sources)
## General Info
## Technologies
Project is created with:
* Python version: 3.7.3
* Sublime Text version: 3.2.1

## Setup
## Scope of Functionality 
## Example of Use
## File List
## Illustration
## Sources
mundaneMath.py - Located in the master branch
hello.py - Located in the master branch
index.html - Located in the gh-pages branch (pushed to the origin)
.nojekyll - Located in the gh-pages branch (pushed to the origin)
# Sample Code
This is the function to add together all the even numbers between 1 and 100. Then displays that number to the terminal. 
def mundaneMath():
    '''
    **Parameters**
        None
    **Returns**
        None
    '''
    # This is an empty array to store the even numbers
    a = []
    # A loop to increment from 1 to 100
    for i in range(1, 101):
        # This finds the even numbers from 1 to 100
        # and stores them in the array
        if (i % 2 == 0):
            a.append(i)
    # Adds the even numbers together and stores them in the variable x
    x = sum(a)
    # Prints the output
    print(x)

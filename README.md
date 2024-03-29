## SoftwareCarpentryWC3
In this weeks lab for Software Carpentry, I have created a website using the built-in feature of GitHub, called “GitHub Pages”. Using a fairly simple I first made a new repository (SoftwareCarpentryWC3), a website, and added that website to the repository. To visit a website should you choose to make one yourself: go to the website “USER.github.io/REPO”, where “USER” is your GitHub username, and “REPO” is the name of
your repository.
## Table of Content
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Sources](#sources)
* [File List](#file-list)
* [Sample Code](#sample-code)
## General Info
This project prints a simple Hello World on the console, and adds together 
all the even numbers between 1 and 100, and prints that value to the terminal.
## Technologies
Project is created with:
* Python version: 3.7.3
* Sublime Text version: 3.2.1
Project uses:
* Anaconda Prompt version: 3.2.1
## Setup
To run this project, use a Text Editor such as Sumblim Text to open the files:
* mundaneMath.py 
* hello.py <br>

Then use the Anaconda Prompt to run the files in Python 3.
## Sources
EN.540.635 - Software Carpentry by Henry C. Herbol
* https://www.thecomputationalist.com/Weekly_Challenges/WC3_GitHub_Online.pdf
## File List
Project contains the following files in the repository:
* mundaneMath.py - Located in the master branch
* hello.py - Located in the master branch
* index.html - Located in the gh-pages branch (pushed to the origin)
* .nojekyll - Located in the gh-pages branch (pushed to the origin)
## Sample Code
Sample of the code used to add all the even numbers between 1 and 100. 
Then displays that number to the terminal:

    def mundaneMath():           
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


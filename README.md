# Python VueJs Complete Example

## Project's aim :
This project aims to serve as a basic example for showing how **Python** as *back-end server* and **Vue js** as a *front js framework* might be glued together for a full-stack webapp

## What is about :
The project is a small web app that allow a user to buy stock options through the screen *Stock* and sell them
through the screen *Portfolio*.

You start with funds of 10000 units, the stock prices are displayed in the *Stock cards* when you hit the menu bar button *End the day* the price get update by a random 33%
(in/de)crease in order for you to decide hat to buy or sell

The project is largely inspired from Maximilian Schwarzmüller's [Udemy course](https://www.udemy.com/course/vuejs-2-the-complete-guide/) exercise section 18 although there are differences, like using python, using a relational database, real-time communication with back-end

## How the project is implemented :
The project contain 2 separated apps in 2 distinct folder, an app for the back-end server in the folder *api*, an app for the front in *ui* folder

### Back-end
The backend uses python, flask web framework, sqlAlchemy ORM and the integrated as a library database SQLite, the usage of SQLite has been choose to not have to use an external database, but since sqlite is not thread safe, is imposes us to not use multi-threading with flask in order to work properly

### Front-end
The front uses Vue js as the front web framework, we cover usage of some Vue's features like routers, filters, Vuex + store, for the css design we use   Bootstrap-Vue it's a mix between Bootstrap and Vue

## Project usage:

### Back-end
At first you need to install the dependencies, then populate the database, then start the server to listen request, here is how to do each step (pre-requisite : makefile program)

#### Install dependencies:

    # If you want to install the dependencies in a virtual env (recommended), create a virtual env
    python3 -m venv api/.env_webapp
    
    # Then activate virtual env
     source api/.env_webapp/bin/activate
    
    # Install dependencies
    pip install -r requirements.txt

#### Populate the database
Once the dependencies are installed initialize and populate the database by running the cmds :
    
    # create folder api/db/data if it does not exist
    mkdir api/db/data

    #populate the database
    make populate

you should see the the file db/data/database.db appearing this file contain the database's data, this is the file that is used by SQLite in this project for write/read operations

#### Run the back-end server
Once the database populated, start the single threaded flask server buy running the makefile cmd

    make run_back
Your server is listening to request on localhost, port:8080

### Front-end
Once again you need to start the dependencies and run the server

#### Install dependencies:

    # Enter the folder ui
    cd ui
   
    # Install dependencies with Yarn or npm
    yarn install
   
    # comeback to the root folder 
    cd ..

#### Run the front-end server
At the root of the project run the makefile cmd : 

    make run_front

You server should be running on http://localhost:8081/ just click on the link and then you are redirected through your default browser to the webapp.

Enjoy !

## Video : 

Checkout what is should looks like in the video [here](https://share.clickup.com/clip/p/t2195826/a0e128e5-95f4-4b29-92f7-ce4d597d73b6/screen-recording-2020-09-11-22%3A06.webm)

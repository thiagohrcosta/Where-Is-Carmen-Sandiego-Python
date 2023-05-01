# Carmen Sandiego Game (Python)
![enter image description here](https://res.cloudinary.com/dloadb2bx/image/upload/v1682968601/carmen1_fwioao.png)

## Technologies used
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

This project was created using Docker to studying the basic concepts of Python learned at day 06  in the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)**.  This project is not part of the course curriculum, but it was used to fix some knowledge learned during the sixth day, using small functions to control the flow of the application.

## Summary
**Day 06**: Functions

**Plus:** To better control the flow of the application and to apply more complex concepts from the beginning to simple projects, including SOLID, two files were created where hash arrays are stored, this makes calls to apply random functions to select locations easier, actions and countries that will be shown to the user.

## What user can do?
![enter image description here](https://res.cloudinary.com/dloadb2bx/image/upload/v1682969221/carmen2_guotog.png)

**User:** At the beginning of the application, the user must enter his agent name. After that random functions are called to determine which location, action and country Carmen Sandiego is. After that, information is generated asking which country has a certain flag. The user will have to choose between the 3 available options. If it hits, it will gain experience and remove life points from Carmen Sandiego, if it misses, the user will lose life points. The game ends when one of the two (user or Carmen Sandiego) reaches zero life points.

## How to run this project
This project was created with Docker, the Dockerfile is:

    FROM  python:3
    
    WORKDIR  /app
    
    COPY  .  .
    
    CMD  ["python",  "app/main.py"]

To run just download this project and run the follow commands:  `docker build -t where-is-carmen-sandiego .`  then run `docker run -it where-is-carmen-sandiego`. )

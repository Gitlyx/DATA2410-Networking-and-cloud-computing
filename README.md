## Results 
Course: DATA2410-Networking-and-cloud-computing
Title: Individual Portfolio Assignment 
Author: Charlie Vo, s188910.
Grade: 59/60 points (A).

## Summary
In this assignment, I have created a chat application where a server and a client are configured to act as a send and receive messaging service. The two main files are client.py and server.py. My choice of programming language is Python.

The application in itself is built on basic send and receive functions where the server accepts 5 connections. The 5 client connections should consist of 1 Lord (Which is you!) and 4 bots either named or randomly selected from a pool of names (From the Game of Thrones universe).


## How to use the Application
To launch the application in its entirety, you need to access the folder from a CLI and launch the server.py by writing `python3 server.py`. Once the server is running, you can proceed with connecting 1 Admin client with the command `python3 client Lord`. Lastly, you need to connect 4 bots by typing `python3 client` for each of the bots. You also have the alternative to name your bots by simply appending a username like this `python3 clients.py <username>`. 

Once the Server, Admin, and Bots are up and running you will see an announcement that 5/5 connections have been established and the main event is about to start. 

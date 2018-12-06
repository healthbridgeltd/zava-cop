# Hands-On Session: Hello Redis

This directory contains files to use for the first hands-on exercise, building the classic 
Hello World with a Redis twist.  In this session, you will create a Hello Redis program
which connects to Redis, writes a message to the database, reads that message back, then
displays the message to the end user.  After that you will modify the program to add a 
counter to track the number of times the program executes.

The files `hello.py` is a skeleton program to get you started.  It provides and explains
the boilerplate code needed to set up a connection to Redis. Feel free to study it or get help from the training staff.

Although this is a hands-on exercise, we want to encourage you to use this time to ask 
questions of the training staff as well.

## Part One: Hello

### Instructions
1. Prior to modifying `hello.py`, run the program and see what happens
2. Add code to the program to store a Hello World message in Redis
3. Modify the code that prints the message to read the message from Redis instead of a constant string

## Part Two: 

### Instructions
1. Add code to `hello.py` to track how often the program runs
2. Uncomment the code to print the run count message and modify to use the value from Redis

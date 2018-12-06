# Hands-On Session: PubSub

This exercise demonstrates the PubSub features of Redis by building a simulation of JSON messages
being sent from publishers to subscribers in response to events happening on a website.  For this
session, you will need to review the Redis PubSub commands, create a publisher that publishes JSON events
via Redis, then create a set of subscribers to receive and process the events.

This directory contains files to use for the exercise.  The `pubsub.py` program provides a skeleton to
help you get started.  We have added code to manage multiple publishers and subscribers running locally 
and to help create simulated messages.  If you get stuck, `pubsub_solution.py` implements our solution to 
the exercise.  Feel free to study it or ask questions of the training staff.

Although this is a hands-on exercise, we want to encourage you to use this time to ask 
questions of the training staff as well.

## Part One: Review PubSub Documentation on redis.io

### Instructions

Please review the following documentation on redis.io to get started:
* [PubSub Commands](https://redis.io/commands#pubsub)
* [Python client API](https://github.com/andymccurdy/redis-py)

## Part Two: Create a Publisher

1. Prior to modifying `publish.py`, run the program and see what happens
2. Update the file with your connection information
3. Add code to create a Redis connection object
4. Add code to the event simulation loop to publish the events via Redis
5. Add code to send the terminate event to the subscribers

## Part Three: Create a Subscriber

1. Prior to modifying `subscribe.py`, run the program and see what happens
2. Update the file with your connection information
3. Add code to create a Redis connection object
4. Add code to subscribe to the appropriate channels
5. Add code to get the JSON message from the Redis subscription




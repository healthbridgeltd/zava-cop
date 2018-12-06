#!/usr/bin/env python3

import json
import random
import redis
import time

from threading import Thread

# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""

def subscriber(name, channels):
    """Processes simulated event message from a Redis Channel"""
    
    # Add code to create a Redis connection

  
    # Add code to subscribe to the channels requested
  
    done = False
    while not done:
        
        # Add code to get message for Redis
        message = None
        
        if message is not None and message['type'] == 'message':
            print("Subscriber {} received a message: {} on channel {}".format(name, message['data'], message['channel']))
            
            event = json.loads(message['data'])
            if event['type'] == 'terminate':
                done = True  

        time.sleep(0.001)  
        
    
def run_subscribers():
    """Sets up a pubsub simulation environment with one publisher and 5 subscribers"""
    
    # create listeners on 
    c1 = Thread(target=subscriber, args=('A', ['user_event:view', 'process:terminate']))
    c2 = Thread(target=subscriber, args=('B', ['user_event:login', 'user_event:logout', 'process:terminate']))
    c3 = Thread(target=subscriber, args=('C', ['user_event:login', 'process:terminate']))
    c4 = Thread(target=subscriber, args=('D', ['user_event:logout', 'process:terminate']))
    c5 = Thread(target=subscriber, args=('E', ['user_event:login', 'user_event:logout', 'user_event:view', 'process:terminate']))
    
    c1.start()
    c2.start()
    c3.start()
    c4.start()
    c5.start()
            
if __name__ == '__main__':
        
    run_subscribers()    
        







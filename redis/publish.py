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

event_channels = {
    'login': 'user_event:login',
    'view': 'user_event:view',
    'logout': 'user_event:logout',
}

event_types = list(event_channels.keys())

def publisher():
    """Publishes simulated event messages to a Redis Channel"""
    
    # Create a Redis connection object

    for id in range(50):
        
        # create the event as an dict with fields type and id
        event = {}
        event['type'] = event_types[ random.randint(0, len(event_types) - 1) ]
        event['id'] = id

        # convert the event to json and log to the console
        event_message = json.dumps(event)
        channel = event_channels[event['type']]
        print("Sending message {} -> {}".format(event_message, channel))

        # add code here to publish message
        cnt = 0
        print("Delivered message to {} subscribers".format(cnt))
        
        time.sleep(0.001)
        
    # send a terminate message to all clients
    term = { 'type': 'terminate'}
    term_message = json.dumps(term)
    channel = 'process:terminate'
    
    print("Sending terminate message")

    # add code here to send the terminate meesage
    cnt = 0
    print("Delivered message to {} subscribers".format(cnt))
            
    
def run_publisher():
    """Sets up a pubsub simulation environment with one publisher and 5 subscribers"""
            
    p = Thread(target=publisher)
    p.start()
        
    
if __name__ == '__main__':
        
    run_publisher()    
        







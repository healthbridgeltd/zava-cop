#!/usr/bin/env python3

# step 1: import the redis-py client package
import redis

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "0.0.0.0"
redis_port = 6379
redis_password = ""


def hello_redis():
    """Example Hello Redis Program"""
    
    # step 3: create the Redis Connection object
    try:
    
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    
        # step 4: Set the hello message in Redis 
        # Add code here to set the hello message
        
        # step 5: Retrieve the hello message from Redis
        # Change this code to get the hello message from Redis
        msg = "Add code to get the message from Redis"
        print(msg)

        # step 6: increment our run counter
        # Add code to track the number of times the program has been run in 
        # cnt = 
        # print("Hello Redis has run {} times".format(cnt))
        
    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    hello_redis()
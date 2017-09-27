# Nginx example

1. try this:

    docker run -v ${PWD}:/usr/share/nginx/html:ro -p 8080:80 nginx:1.12.1-alpine 

    # point browser to localhost:8080

2. now this:

    docker run -v ${PWD}:/usr/share/nginx/html:ro -p 80 -d nginx:1.12.1-alpine

    # To find out the host and port:
    docker ps

    # or if you have jq
    docker inspect <container id> --format '{{json .NetworkSettings.Ports}}' | jq

    # then kill:
    docker kill <container id>


3. build our own

   docker build -t cop/nginx . 

   docker run --rm -p 8080:80 cop/nginx   

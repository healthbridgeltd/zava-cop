# Into compose

make sure that you add and entry to your `/etc/hosts` file for `docker.localhost`:
```
127.0.0.1       localhost localunixsocket.local localunixsocket docker.localhost
```

1. clean up from before:
```
   # check what's there
   docker ps -a 

   # remove old containers
   docker container prune

   # check again!
   docker ps
```

2. Build Arguments

```
    docker build -t cop2/nginx .
    docker build -t cop2/nginx-blue --build-arg COLOR=blue .
    docker run --rm -p 8080:80 cop2/nginx 

    # detour image clean up
    docker images
    docker image prune 
    docker images

    # docker compose!
    docker-compose build
    docker-compose up -d
    docker-compose ps
    # checkout the proxy page
    # http://docker.localhost:8080/dashboard/#/
    # and the service:
    # http://color.docker.localhost:8888/
    # refresh a couple of times to see the load balancing work
    # let's scale red
    docker-compose scale red=4
    docker-compose ps

    #clean up
    docker-compose stop
    docker-compose rm
    docker network prune
```


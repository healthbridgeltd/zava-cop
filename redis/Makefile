build:
	docker build --net=bridge -f Dockerfile -t redis-app .
redis:
	docker run --name redis-db -p 6379:6379 -d redis
run:
    docker run -v $(pwd):/app -it redis-app python hello_solution.py
	
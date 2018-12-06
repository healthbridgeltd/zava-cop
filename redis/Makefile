build:
	docker build -f Dockerfile -t redis-app .
redis:
	docker run --name redis-db -p 6379:6379 -d redis
run:
    docker run -v $(pwd):/app -it redis-app python hello.py
pub:
    docker run -v $(pwd):/app -it redis-app python publish.py
sub:
    docker run -v $(pwd):/app -it redis-app python subscribe.py
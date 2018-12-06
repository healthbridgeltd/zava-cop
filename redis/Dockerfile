FROM python:3.6

RUN mkdir -p /app

WORKDIR /app

COPY . .

RUN pip install -r /app/requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]
FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=root1234

COPY ./database/init.sql /init.sql

CMD ["mysqld", "--init-file=/init.sql", "--port=3307"]

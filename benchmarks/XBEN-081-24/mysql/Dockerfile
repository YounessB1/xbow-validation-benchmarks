FROM --platform=linux/amd64 mysql:5.7@sha256:4bc6bc963e6d8443453676cae56536f4b8156d78bae03c0145cbe47c2aad73bb

ENV MYSQL_ROOT_PASSWORD=password

ARG FLAG
ADD init.sql /docker-entrypoint-initdb.d
RUN sed -i s/FLAG_PLACEHOLDER/$FLAG/g /docker-entrypoint-initdb.d/init.sql

EXPOSE 3306
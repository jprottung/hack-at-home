FROM python:3.8.1-alpine3.11

MAINTAINER Antony Goetzschel <mail@ago.dev>

#RUN apt update
#RUN apt install python3-dev \
#                default-libmysqlclient-dev -y
RUN apk update
RUN apk add python3-dev \
            mariadb-dev \
            gcc \
            g++ \
            libffi-dev \
            make \
            openssl-dev \
            python3-dev
COPY requirement.txt /requirement.txt
RUN pip install --upgrade pip
RUN pip install -r /requirement.txt
RUN rm -rf /requirement.txt
WORKDIR /app
EXPOSE 8000
CMD ["/bin/sh"]
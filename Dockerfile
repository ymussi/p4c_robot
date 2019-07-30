FROM python:3.7
LABEL mantainer="ymussi@gmail.com"
LABEL fileversion=v0.1

ARG RUN_ENVIRONMENT
ENV DBENV=${RUN_ENVIRONMENT}
ENV PYTHONUNBUFFERED=TRUE

WORKDIR /app/first-robot

COPY . .

RUN apt update && \
    apt install -y openssh-client && \
    apt install -y git && \
    apt install -y python3-dev 

RUN pip install -r requirements.txt && python setup.py develop


ENTRYPOINT ["/bin/sh","/app/first-robot/entrypoint.sh"]

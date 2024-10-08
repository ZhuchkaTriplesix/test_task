FROM ubuntu:20.04

ENV LANG="en_US.UTF-8"
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y locales

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    /usr/sbin/update-locale LANG=en_US.UTF-8

ENV LC_ALL en_US.UTF-8

RUN \
  apt-get update && \
  apt-get install -y python3 python3-pip python3-dev

ADD requirements.txt /app/
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "./code/main.py"]
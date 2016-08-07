FROM gauravkaushik/ubuntu:latest

MAINTAINER "Gaurav Kaushik" <gaurav916@gmail.com>

COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN pip install -r app/requirements.txt

RUN chmod +x app/views.py
RUN export FLASK_APP=app/views.py
RUN PATH=$PATH:/app
RUN export PATH

CMD ["views.py"]

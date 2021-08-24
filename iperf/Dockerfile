FROM ubuntu:latest
MAINTAINER kunholee98 "dlrjsgh750@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["measure.py"]

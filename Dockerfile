# Dockerfile
# without an file extension

# Use an official Python runtime as a parent image
FROM python:3.7-slim

RUN mkdir -p /app

#ADD ./customScheduler.py .

# Set the working directory
#WORKDIR ~/k8s-scheduling-based-on-networking-latency-in-cloud-native-computing-platform
WORKDIR /app

# Copy the current directory contents into the container
#COPY . ~/k8s-scheduling-based-on-networking-latency-in-cloud-native-computing-platform
COPY customScheduler.py customScheduler.py
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
#RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
RUN pip install -r requirements.txt

# Make prot 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run custumScheduler.py when the container launches
ENTRYPOINT ["python", "customScheduler.py"]

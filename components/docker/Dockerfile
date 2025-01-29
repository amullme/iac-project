# Dockerhub base image
FROM python:3.12

# Working directory in the docker image
WORKDIR /usr/local/app

# Install the application dependencies from this machine to the image
COPY ../python/flask-hello/requirements.txt ./
RUN pip install -r requirements.txt

# Copy in the source code from this machine to the image
COPY ../python/flask-hello ./src

# Expose the default Flask port 5000
EXPOSE 5000

# Lauch the hello.py on the docker image
CMD ["python3", "./src/hello.py"]
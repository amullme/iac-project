FROM python:3.12
WORKDIR /usr/local/app

# Install the application dependencies
COPY ./flask-hello-world/requirements.txt ./
RUN pip install -r requirements.txt

# Copy in the source code
COPY ./flask-hello-world ./src
EXPOSE 5000

CMD ["python3", "./src/hello.py"]
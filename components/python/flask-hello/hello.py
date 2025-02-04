from flask import Flask
from faker import Faker
import socket

app = Flask(__name__)
fake = Faker()

@app.route('/')
def hello():
    return ( 'Hello fake person named ' + fake.name()
            + ' from container or host named ' + socket.gethostname())

if __name__ == '__main__':
    app.run(host='0.0.0.0')


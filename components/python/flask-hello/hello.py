from flask import Flask
from faker import Faker

app = Flask(__name__)
fake = Faker()

@app.route('/')
def hello():
    return 'Hello ' + fake.name() + '  '

if __name__ == '__main__':
    app.run(host='0.0.0.0')


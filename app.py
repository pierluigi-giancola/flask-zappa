from flask import Flask, request, jsonify, g
from utils.auth import protected
from routes import routes
from mongoengine import connect
import jwt

app = Flask(__name__)
app.config.from_object('config.{}'.format(app.config['ENV']))
config = app.config

connect(host=app.config['MONGODB_SETTINGS']['host'])

@app.route('/')
def rootcheck():
    return '<h1>{}-{}</h1>'.format(config['PROJECT_NAME'] ,config['ENV'])

for route in routes:
    route().register(app)

if __name__ == '__main__':
    app.run()

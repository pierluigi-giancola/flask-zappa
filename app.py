from flask import Flask, g, jsonify, request
from flask_cors import CORS

from routes import routes

app = Flask(__name__)
app.config.from_object('config.{}'.format(app.config['ENV']))
CORS(app=app)
config = app.config


@app.route('/')
def rootcheck():
    return '<h1>{}-{}</h1>'.format(config['PROJECT_NAME'], config['ENV'])


for route in routes:
    route().register(app)

if __name__ == '__main__':
    app.run()

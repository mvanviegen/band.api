from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identify
from resources.user import UserRegister
from resources.band import Band, Bands
import os
# SETUP DATABASE WITH SQLALCHEMY

# SETUP APP
app = Flask(__name__)
app.secret_key = 'jose' # LATER PLACED IN CONFIG
api = Api(app)

# JSON WEBTOKENS
jwt = JWT(app,authenticate,identify) #/auth

# CREATE TABLES IF NOT EXIST
@app.before_first_request
def create_tables():
    db.create_all()


# API RESOURCES
api.add_resource(Band, '/band/<string:name>')
api.add_resource(Bands, '/bands')
api.add_resource(UserRegister, '/register')

app.config.from_object(os.environ["APP_SETTINGS"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# print(os.environ['APP_SETTINGS'])

if __name__ == '__main__':
    from db import db
    db.init_app(app)
# START OUR APP
app.run(port=8000, debug=True)

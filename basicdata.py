import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' +os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.SQLAlchemy(app)

##########################################
class Puppy(db.model):
    #manual table name choice
    __tablename__= 'puppies'

    id = db.Column(db.integer,primary_key=True)
    name = db.Column(db.text)
    age = db.Column(db.integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"puppy {self.name} is {self.age} old"


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app=Flask(__name__)
app.config['SECRET_KEY']= 'efce622448d3b2f542f80b81715738ad'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
from app import routes

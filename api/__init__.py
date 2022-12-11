import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#db object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True

    #configure sqlite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gdsc.db'
    #initialize db
    db.init_app(app)

    #register posts blueprint
    from . import posts
    app.register_blueprint(posts.posts)

    return app
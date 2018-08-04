from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# creating an instance of the Flask app
app = Flask(__name__)

# setting the configuration of the application from a settings file
app.config.from_object('config')

# db holds the database
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# importing all of the views from the various modules
from MainModule import views

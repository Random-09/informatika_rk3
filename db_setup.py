from flask_sqlalchemy import SQLAlchemy
from app_setup import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///films.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .db import db, Question, User
from flask_cors import CORS
#from add_q import add_questions, get_all_questions

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db = SQLAlchemy(app)





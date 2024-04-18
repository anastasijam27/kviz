from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db = SQLAlchemy(app)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(300), nullable=False)
    option_1 = db.Column(db.String(300), nullable=False)
    option_2 = db.Column(db.String(300), nullable=False)
    option_3 = db.Column(db.String(300), nullable=False)
    option_4 = db.Column(db.String(300), nullable=False)
    correct_answer = db.Column(db.String(300), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(130), nullable=False)
    questions = db.relationship('Question', backref='author', lazy=True)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

with app.app_context():
    db.create_all()

def add_user(users):
    for user_details in users:
        users = User(
            username = user_details['username'],
            email = user_details['email'],
            password_hash = user_details['password_hash'],
        )
        db.session.add(users)
    db.session.commit()
def add_questions(questions):
    for question_details in questions:
        question = Question(
            question_text=question_details['question_text'],
            option_1=question_details['option_1'],
            option_2=question_details['option_2'],
            option_3=question_details['option_3'],
            option_4=question_details['option_4'],
            correct_answer=question_details['correct_answer'],
            author_id=question_details.get('author_id')
        )
        db.session.add(question)
    db.session.commit()

def get_all_questions():
    return Question.query.all()

if __name__ == "__main__":
    with app.app_context():
        questions = [
        {
            'question_text': 'Koji je glavni grad Srbije?',
            'option_1': 'Zagreb',
            'option_2': 'Novi Sad',
            'option_3': 'Budimpešta',
            'option_4': 'Beograd',
            'correct_answer': 'Beograd',
            'author_id': 1 
        },
        {
            'question_text': 'Koje godišnje doba je u Australiji tokom meseca januara?',
            'option_1': 'Zima',
            'option_2': 'Leto',
            'option_3': 'Proleće',
            'option_4': 'Jesen',
            'correct_answer': 'Leto',
            'author_id': 1
        },
    ]
        users = [
            {
                'username': 'anastasija',
                'email': 'anastasija@gmail.com',
                'password_hash': 'SAdojowWAR',
            }
        ]
        add_questions(questions)
        add_user(users)

    all_questions = get_all_questions()
    for question in all_questions:
        print(question.question_text)
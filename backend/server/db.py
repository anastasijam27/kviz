from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from datetime import datetime

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
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(130), nullable=False)
    questions = db.relationship('Question', backref='author', lazy=True)
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
class UserScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    user = db.relationship('User', backref='leaderboard_entries', lazy=True)

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
            'author_id': None
        },
        {
            'question_text': 'Koje godišnje doba je u Australiji tokom meseca januara?',
            'option_1': 'Zima',
            'option_2': 'Leto',
            'option_3': 'Proleće',
            'option_4': 'Jesen',
            'correct_answer': 'Leto',
            'author_id': None
        },
        {
            'question_text': 'Ko je pobedio na takmičenju Pesma Za Evroviziju 2022. godine?',
            'option_1': 'Breskvica',
            'option_2': 'Konstrakta',
            'option_3': 'Zorja',
            'option_4': 'Luke Black',
            'correct_answer': 'Konstrakta',
            'author_id': None
        },
        {
            'question_text': 'Koji je najveći organ u ljudskom telu?',
            'option_1': 'Srce',
            'option_2': 'Želudac',
            'option_3': 'Koža',
            'option_4': 'Pluća',
            'correct_answer': 'Koža',
            'author_id': None
        
        },
        {
            'question_text': 'Koji od sledećih filmova NE pripada Marvelovom univerzumu?',
            'option_1': 'Thor',
            'option_2': 'Doctor Strange',
            'option_3': 'Iron Man',
            'option_4': 'Wonder Woman',
            'correct_answer': 'Wonder Woman',
            'author_id': None
        },
        {
            'question_text': 'Koja planeta je najbliža Suncu?',
            'option_1': 'Mars',
            'option_2': 'Neptun',
            'option_3': 'Merkur',
            'option_4': 'Jupiter',
            'correct_answer': 'Merkur',
            'author_id': None
        },
        {
            'question_text': 'Ko je napisao delo "Zločin i kazna"?',
            'option_1': 'Vilijem Šekspir',
            'option_2': 'Alber Kami',
            'option_3': 'Fjodor Mihajlovič Dostojevski',
            'option_4': 'Aleksandar Puškin',
            'correct_answer': 'Fjodor Mihajlovič Dostojevski',
            'author_id': None
        },
        {
            'question_text': 'Koji je hemijski simbol ugljenika?',
            'option_1': 'H',
            'option_2': 'O',
            'option_3': 'C',
            'option_4': 'U',
            'correct_answer': 'C',
            'author_id': None
        },
        {
            'question_text': 'Koji je od sledećih filmova režirao Kventin Tarantino?',
            'option_1': 'Pulp Fiction',
            'option_2': 'The Dark Knight',
            'option_3': 'Barbie',
            'option_4': 'Oppenheimer',
            'correct_answer': 'Pulp Fiction',
            'author_id': None
        },
        {
            'question_text': 'Ko je grčka boginja ljubavi i lepote?',
            'option_1': 'Atina',
            'option_2': 'Afrodita',
            'option_3': 'Nika',
            'option_4': 'Hera',
            'correct_answer': 'Afrodita',
            'author_id': None
        },
        {
            'question_text': 'U kom gradu žive Simpsonovi?',
            'option_1': 'Njujork',
            'option_2': 'Los Anđeles',
            'option_3': 'Springfild',
            'option_4': 'Bruklin',
            'correct_answer': 'Springfild',
            'author_id': None
        },
        {
            'question_text': 'Ko je osvojio Svetsko prvenstvo u fudbalu 2014. godine?',
            'option_1': 'Francuska',
            'option_2': 'Argentina',
            'option_3': 'Brazil',
            'option_4': 'Nemačka',
            'correct_answer': 'Nemačka',
            'author_id': None
        },
        {
            'question_text': 'Koja je najgledanija Netflix serija 2019. godine?',
            'option_1': '13 Reasons Why',
            'option_2': 'Orange Is The New Black',
            'option_3': 'Stranger Things',
            'option_4': 'Lucifer',
            'correct_answer': 'Stranger Things',
            'author_id': None
        },
        {
            'question_text': 'Koja pesma ima najviše strimova na Spotify-u?',
            'option_1': 'Dance Monkey',
            'option_2': 'Blinding Lights',
            'option_3': 'Watermelon Sugar',
            'option_4': 'Cruel Summer',
            'correct_answer': 'Blinding Lights',
            'author_id': None
        },
        {
            'question_text': 'Gde će se održati Olimpijske igre 2024?',
            'option_1': 'London',
            'option_2': 'Pariz',
            'option_3': 'Los Anđeles',
            'option_4': 'Barselona',
            'correct_answer': 'Pariz',
            'author_id': None
        },
        {
            'question_text': 'Koja je najmanja država na svetu?',
            'option_1': 'San Marino',
            'option_2': 'Luksemburg',
            'option_3': 'Vatikan',
            'option_4': 'Crna Gora',
            'correct_answer': 'Vatikan',
            'author_id': None
        },
        {
            'question_text': 'Ko je bio prvi predsednik SAD?',
            'option_1': 'George Washington',
            'option_2': 'Thomas Jefferson',
            'option_3': 'Richard Nixon',
            'option_4': 'Abraham Lincoln',
            'correct_answer': 'George Washington',
            'author_id': None
        },
        {
            'question_text': 'Koji film je dobio oskara za najbolji film 2023. godine?',
            'option_1': 'Avatar: The Way Of Water',
            'option_2': 'Everything Everywhere All At Once',
            'option_3': 'Top Gun: Maverick',
            'option_4': 'All Quiet On The Western Front',
            'correct_answer': 'Everything Everywhere All At Once',
            'author_id': None
        },
    ]
        add_questions(questions)
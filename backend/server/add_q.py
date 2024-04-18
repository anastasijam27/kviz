from db import db, Question
from flask import Flask

app = Flask(__name__)

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
    ]
        add_questions(questions)

    all_questions = get_all_questions()
    for question in all_questions:
        print(question.question_text)
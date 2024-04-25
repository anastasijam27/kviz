from flask import Flask, request, render_template, redirect, session, jsonify
from db import db, User
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if not name or not email or not password:
        return jsonify({'error': 'Name, email, and password are required'}), 400
    existing_user = User.query.filter((User.email == email)).first()
    if existing_user:
        return jsonify(error='Email already exists!'), 400
    new_user = User(name=name,email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return jsonify(error='Invalid user')

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()  # Corrected
        if user:
            return render_template(user=user)
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
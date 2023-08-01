from website import app
from flask import render_template, url_for, request, redirect
from db import Users, Country
from flask import session as session
from db import session as ses
from datetime import datetime
from sqlalchemy import select
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os

app.config['UPLOAD_FOLDER'] = 'website/static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}


@app.route("/")
def main():
    requests = select(Users.id)
    user_profile = ses.scalars(requests)
    return render_template("main.html", user_profile=user_profile)


@app.route("/register", methods=['POST', 'GET'])
def register():
    requests = select(Country)
    countries = ses.scalars(requests)

    if request.method == "POST":
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        country_id = request.form.get('country')
        print(type(country_id))

        new_user = Users(first_name=request.form['first_name'],
                         second_name=request.form['second_name'],
                         email=request.form['email'],
                         password=hashed_password,
                         date=datetime.date(datetime.strptime(request.form["date"], '%Y-%m-%d')),
                         country_id=ses.get(Country, country_id)
                         )

        ses.add(
            new_user)

        ses.commit()
        return render_template('login.html')

    return render_template("register.html", countries=countries)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if 'email' in session:
        return redirect('profile')

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = ses.query(Users).filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['email'] = user.email
            return redirect(url_for('profile'))

        return 'Невірні дані для входу'

    return render_template("login.html")


@app.route("/country", methods=["POST", "GET"])
def country():
    if request.method == "POST":
        try:
            cuontry = Country(tittle=request.form['tittle'])
            ses.add(cuontry)

            ses.commit()
            return redirect('/')

        except Exception as e:
            ses.rollback()
            return f'{e}'

    else:
        return render_template("country.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


# @app.route('/profile', methods=['GET', 'POST'])
# def profile():
#         if request.method == 'POST':
#         file = request.files['file']
#
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('profile', filename=filename))
#
#     return render_template('profile.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('profile_2', filename=filename))

    return render_template('profile.html')


@app.route('/profile_2/<filename>')
def profile_2(filename):
    return render_template('profile2.html', filename=filename)

# @app.route('/profile2', methods=['GET', 'POST'])
# def profile2():
#     return render_template('profile2.html')

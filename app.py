from flask import Flask, render_template, request, sessions, redirect
import data
from data import read_users, add_user, get_patient, read_one
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/users")
def users():
    users_list = read_users()
    return render_template("users.html", result=users_list)


@app.route("/add-user", methods=['GET', 'POST'])
def add_users():
    print("Got It")
    if request.method == 'POST':
        print("its post")
        print(request.form['email'])
        data.add_user(request.form['email'], request.form['password'])
        return redirect('/users')


@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/signup_action", methods=['GET', 'POST'])
def signup_action():
    if request.method == 'POST':
        print(request.form['email'])
        add_user(request.form['email'], request.form['password'])
        print("SignUp Action completed")
    return redirect('/signin')


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/dashboard/<id>")
def dashboard(id):
    list_of_all = []
    result = read_one(id)
    for row in result:
        list_of_all.append(dict(row))
    print(list_of_all)
    return render_template('dashboard.html', all_data=list_of_all)


@app.route('/search', methods=['GET', 'POST'])
def search():
    result_list = []
    if request.method == "POST":
        print(request.form['user-name'])
        result = get_patient(request.form['user-name'])
        for i in result:
            result_list.append(dict(i))
        print(result_list)
        return render_template("list.html", data=result_list)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run()

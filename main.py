from flask import Flask, render_template

app=Flask(__name__)
holder = "Search"


@app.route('/')
def welcome():
    return render_template("welcome.html")


@app.route('/contact/')
def contact():
    return render_template("contact.html")


@app.route('/survey/')
def survey():
    return render_template("survey.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/login/')
def login():
    return render_template("login.html")


@app.route('/signup/')
def signup():
    return render_template("signup.html")


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
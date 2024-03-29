from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app=Flask(__name__)

holder = "Search"
app.config['SECRET_KEY'] = 'b2aca867f0c5bdd03fe53d12b4861c08'


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


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'meliodas123':
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('signup'))
    return render_template("login-flask.html", form=form)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
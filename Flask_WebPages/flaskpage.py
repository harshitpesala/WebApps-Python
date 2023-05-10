from flask import Flask, redirect, url_for, render_template, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b4cd0a4a1d2b0f60fab29cabe0ccff83'

posts = [
	{
		"author":"Harshit Pesala",
		"title":"Blog Post 1",
		"content":"First post content",
		"date_posted":"Sep 08, 2020"
	},
	{
		"author":"Pranav Pesala",
		"title":"Blog Post 2",
		"content":"Second post content",
		"date_posted":"Sep 09, 2020"
	}
]


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts = posts, title = "Home")


@app.route("/about")
def about():
	return render_template('about.html', title = "About Us")

@app.route("/register", methods = ['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f"Welcome {form.username.data}!",'success')
		return redirect(url_for('home'))
	return render_template('register.html', title = "Register", form = form)

@app.route("/login")
def login():
	form = RegistrationForm()
	return render_template('login.html', title = "Login", form = form)		

		
if __name__ == "__main__":
	app.run(debug = True)

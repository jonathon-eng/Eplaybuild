from flask import Flask, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

application = Flask(__name__)

application.config["TEMPLATES_AUTO_RELOAD"] = True
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registered.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configure session to use filesystem (instead of signed cookies)
application.config["SESSION_PERMANENT"] = False
application.config["SESSION_TYPE"] = "filesystem"

db = SQLAlchemy(application)

class Registered(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime)
    classes = db.Column(db.String(100), nullable=False)
    date_requested = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)


    def __repr__(self):
        return '<Name %r>' % self.id 







@application.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@application.route("/")
def home():
    return render_template("index.html")

@application.route("/about")
def about():
    return render_template("about.html")

@application.route("/class")
def name():
    return render_template("class.html")

@application.route("/events")
def events():
    return render_template("events.html")

@application.route("/register", methods=["GET", "POST"])
def register():
        if request.method == "POST":

#         # Ensure username was submitted
            if not request.form.getlist("classesChecked"): 
                # flash("Login successful")
                return redirect("/register")

            else:
                print(request.form.getlist("classesChecked"))  

                print(request.form.get("calendar"))

                print(request.form.get("email"))

                print(request.form.get("name"))


                return redirect("/class") 




#             return apology("must provide username", 400)

#         # Ensure password was submitted
#         elif not request.form.get("password"):
#             return apology("must provide password", 400)

#         elif not request.form.get("confirmation"):
#             return apology("must provide confirmation password", 400)

#         elif request.form.get("password") != request.form.get("confirmation"):
#             return apology("passwords must match", 400)

#         # Query database for username
#         rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

#         # if username exists
#         if len(rows) != 0:
#                 return apology("username already exists", 400)

#         # generate password hash
#         hash = generate_password_hash(request.form.get("password"))

#         # storing info into db
#         db.execute("INSERT INTO users (username, hash) VALUES(?,?)", request.form.get("username"), hash)


#          # Remember which user has logged in
#         username = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

#         session["user_id"] = username[0]["id"]

#         # Redirect user to home page
#         return redirect("/")


#     else:
        return render_template("register.html")

@application.route("/access")
def access():
    return render_template("access.html")



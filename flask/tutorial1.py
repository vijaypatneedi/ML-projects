from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route("/<name>") #this decorator is used give path to function
def home(name):
    return render_template("index.html", content=name)

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))    

@app.route("/about")
def about():
    name = "vijay"
    return render_template('about.html', name2= name)
app.run(debug=True)

if __name__ =="__main__":
    app.run()
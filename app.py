import csv
from flask import Flask, render_template, request, redirect


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# Home page
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/notes", methods=["GET", "POST"])
def notes():
    return render_template("notes.html")


@app.route("/eli5", methods=["GET", "POST"])
def eli5():
    return render_template("eli5.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")


@app.route("/import_csv", methods=["GET", "POST"])
def csv_import():
    return render_template("import_csv.html")


if __name__ == "__main__":
    app.run(debug=True)

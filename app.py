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


@app.route("/ai_ml_dl", methods=["GET", "POST"])
def ai_ml_dl():
    return render_template("ai_ml_dl.html")


@app.route("/data_types", methods=["GET", "POST"])
def data_types():
    return render_template("data_types.html")


@app.route("/perceptron_primer", methods=["GET", "POST"])
def perceptron_primer():
    return render_template("perceptron_primer.html")


@app.route("/perceptrons_and_logic_gates", methods=["GET", "POST"])
def perceptron_and_logic_gates():
    return render_template("perceptrons_and_logic_gates.html")


if __name__ == "__main__":
    app.run(debug=True)

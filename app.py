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

@app.route("/blog", methods=["GET", "POST"])
def blog():
    return render_template("blog.html")

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


@app.route("/error_functions", methods=["GET", "POST"])
def error_functions():
    return render_template("error_functions.html")


@app.route("/softmax", methods=["GET", "POST"])
def softmax():
    return render_template("softmax.html")


@app.route("/one_hot_encoding", methods=["GET", "POST"])
def one_hot_encoding():
    return render_template("one_hot_encoding.html")


@app.route("/backpropagation", methods=["GET", "POST"])
def backpropagation():
    return render_template("backpropagation.html")


@app.route("/q_learning", methods=["GET", "POST"])
def q_learning():
    return render_template("q_learning.html")


@app.route("/pandas_intro", methods=["GET", "POST"])
def pandas_intro():
    return render_template("pandas_intro.html")


@app.route("/numpy_intro", methods=["GET", "POST"])
def numpy_intro():
    return render_template("numpy_intro.html")


@app.route("/regex", methods=["GET", "POST"])
def regex():
    return render_template("regex.html")


@app.route("/cnn", methods=["GET", "POST"])
def cnn():
    return render_template("cnn.html")


@app.route("/asd_predictor", methods=["GET", "POST"])
def asd():
    return render_template("asd_predictor.html")


@app.route("/lstm", methods=["GET", "POST"])
def lstm():
    return render_template("lstm.html")

@app.route("/setup", methods=["GET", "POST"])
def setup():
    return render_template("setup.html")

@app.route("/datalake_vs_datawarehouse", methods=["GET", "POST"])
def dl_v_dw():
    return render_template("datalake_vs_datawarehouse.html")

@app.route("/pandas_polars_modin", methods=["GET", "POST"])
def pandas_polars_modin():
    return render_template("pandas_polars_modin.html")

if __name__ == "__main__":
    app.run(debug=True)

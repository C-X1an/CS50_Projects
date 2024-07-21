from flask import Flask, render_template, session, request

COLORS = ["red", "green", "blue"]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        color = request.form.get("color")
        if color in COLORS:
            return render_template("color.html", color=color)
        else:
            return render_template("index.html")

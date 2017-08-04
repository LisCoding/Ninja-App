from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/ninja")
def display_ninjas():
    return render_template("ninjas.html")

@app.route("/ninja/<color>")
def ninja(color):
    color2name = {"red": "raphael", "orange": "michelangelo", "purple":"donatello", "blue":"leonardo"}
    if not color2name.has_key(color):
        name = "notapril"
    else:
        name = color2name[color]
    return render_template("ninja.html", name = name)

app.run(debug=True)

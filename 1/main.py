from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "HARD STRING"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/white')
def white():
    return render_template("Тест 3 вопроса.html")


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
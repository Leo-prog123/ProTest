from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "HARD STRING"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/obroz')
def name():
    return render_template('obroz.html')


@app.route('/psiho')
def psiho():
    return render_template('psiho.html')


@app.route('/razvl')
def razvl():
    return render_template('razvl.html')


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')

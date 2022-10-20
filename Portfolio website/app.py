from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/intro.html")
def about():
    return render_template('intro.html')


@app.route("/services.html")
def skills():
    return render_template('services.html')


@app.route("/resume.html")
def resume():
    return render_template('resume.html')


@app.route("/contact.html")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)

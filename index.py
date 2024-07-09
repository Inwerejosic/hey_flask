from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello/<name>')
@app.route("/")
def hello_world(name="Inwerejosic"):
    return render_template('index.html', person=name)
@app.route('/about')
def about():
    return render_template('about.html')


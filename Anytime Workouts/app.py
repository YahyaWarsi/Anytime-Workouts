from os import times
from flask import Flask, render_template, url_for
import time
app = Flask(__name__)







@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/workout/')
def workout():
    return render_template('workout.html')

if __name__ == "__main__":
    app.run(debug=True)
 
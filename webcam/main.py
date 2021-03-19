from flask import render_template
from flask import Flask, url_for


app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
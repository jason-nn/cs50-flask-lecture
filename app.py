from flask import Flask, render_template, request

# __name__ is the name of the current file
app = Flask(__name__)


@app.route('/')
def index():
    name = request.args.get('name') or 'World'
    return render_template('index.html', name=name)

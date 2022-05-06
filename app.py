from flask import Flask, render_template, request

# __name__ is the name of the current file
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    # request.form is used for POST while request.get is used for GET
    name = request.form.get('name') or 'World'
    return render_template('greet.html', name=name)

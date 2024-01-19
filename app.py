from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the About Page'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/template')
def template_example():
    return render_template('index.html', message='Flask is fun!')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', path='Home')
@app.route('/about')
def about():
    return render_template('about.html', path='About')
if __name__ == '__main__':
    app.run(debug=True, port=4000)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ApostasVIP')
def home_page():
    return render_template('index.html')

@app.route('/ApostasVIP/register')

def register():
    return render_template('register.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ApostasVIP/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

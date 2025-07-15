from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/target1')
def target1():
    return render_template('target1.html')

@app.route('/target2')
def target2():
    return render_template('target2.html')

@app.route('/target3')
def target3():
    return render_template('target3.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

if __name__ == '__main__':
    app.run(debug=True)
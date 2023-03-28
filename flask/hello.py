#! /home/xs522872/miniconda3/envs/condapy310/bin/python3.10
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask 2.0!'
    
@app.route('/display', methods=['GET', 'POST'])
def display_text():
    if request.method == 'POST':
        text = request.form.get('text', '')
        return f'You entered: {text}'
    else:
        return render_template('display.html')


if __name__ == '__main__':
    app.run()

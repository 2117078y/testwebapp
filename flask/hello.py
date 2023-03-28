#! /home/xs522872/miniconda3/envs/condapy310/bin/python3.10
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
import openai

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Set your API key here
openai.api_key = "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"

@app.route('/')
def hello():
    return 'Hello, Flask 2.0!'
    
@app.route('/display', methods=['GET', 'POST'])
def display_text():
    if request.method == 'POST':
        text = request.form.get('text', '')
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "ChatGPTへの指示"},
            {"role": "user", "content": f"{text}"}
        ]   
        )
        chatgpt_output = response['choices'][0]['message']['content'].strip()
        return render_template('output.html', input_text=text, chatgpt_output=chatgpt_output)
    else:
        return render_template('display.html')


if __name__ == '__main__':
    app.run()

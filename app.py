import json
import requests
import os
from dotenv import load_dotenv
from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request

#Api Key Hiding
load_dotenv()
KEY = os.getenv('API_KEY')
language = 'en-us'

#Create App
app = Flask(__name__)


#Routes/ Views
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generated', methods=['POST', 'GET'])
def generated():
    language = request.form['language']
    content = request.form['sourcetts']
    tts = f'http://api.voicerss.org/?key={KEY}&hl={language}&src={content}'

    if content == '':
        tts = f'http://api.voicerss.org/?key={KEY}&hl={language}&src=No input detected. Please try again.'
        return render_template('generated.html', api=tts, content='No input detected. Please try again.')
    else:
        
        return render_template('generated.html', api=tts, content=content)

#Run App
if __name__ == '__main__':
    app.run(debug=True)
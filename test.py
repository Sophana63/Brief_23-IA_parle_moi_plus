from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
from dotenv import load_dotenv
import openai
import os

app = Flask(__name__)

# Configure OpenAI API key
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    r = sr.Recognizer()    

    with sr.Microphone() as source:
        audio = r.listen(source)
    try:        
        text = r.recognize_google(audio, language='fr-FR')
    except sr.UnknownValueError:
        text = "Désolé, je n'ai pas compris"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response_set = set(response.choices[0].text.split('\n'))
    response_text = '\n'.join(response_set)
    return jsonify({'text': text, 'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)

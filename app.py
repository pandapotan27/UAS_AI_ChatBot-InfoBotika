from flask import Flask, render_template, request, jsonify
import json
import re

app = Flask(__name__)

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

data = load_data('informatika.json')

def search_keywords(question):
    keywords = re.findall(r'\b\w+\b', question.lower())
    related_indexes = []
    for keyword in keywords:
        if keyword in data['kata_kunci']:
            related_indexes.extend(data['kata_kunci'][keyword])
    return list(set(related_indexes))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    question = request.form['question']
    related_indexes = search_keywords(question)
    if related_indexes:
        responses = [data['jawaban'][index] for index in related_indexes]
        response = '<br>'.join(responses)
    else:
        response = "Maaf, saya tidak mengerti pertanyaan Anda."
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

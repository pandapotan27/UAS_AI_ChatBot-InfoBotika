import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_response(question, data):
    if question in data['pertanyaan']:
        index = data['pertanyaan'].index(question)
        return data['jawaban'][index]
    else:
        return "Maaf, saya tidak mengerti pertanyaan Anda."

if __name__ == "__main__":
    data = load_data('informatika.json')
    while True:
        question = input("Anda: ")
        if question.lower() == "exit":
            break
        response = get_response(question, data)
        print("Bot: " + response)

import json

##################################################################

def json_to_string(data):
    output = ""

    try:
        json_data = json.loads(data)
        for item in json_data:
            word = item.get('text', '')
            output += word.upper()
            output += " "

    except json.JSONDecodeError as e:
        print(f"Fehler beim Handling von JSON: {e}")

    return output

def string_to_json(string):
    json_object = []

    try:
        words = string.split()

        for id, word in enumerate(words):
            json_word = {"id": id, "text": word}
            json_object.append(json_word)

    except:
        print("Couldn't reconvert string to json")

    return json_object
import language_tool_python
import requests

tool = language_tool_python.LanguageToolPublicAPI('de-DE')

def handle_request(data):
    # use python language tool to correct sentence
    corrected_data = tool.correct(data)

    print("Original:  ", data)
    print("Corrected: ", corrected_data)

    #close opened connection to tool
    tool.close()

    # return corrected sentence
    return corrected_data



def duden_api_request(text):
    # Generate POST request with settings to duden API
    url = 'https://api.duden.de/v1/spellcheck'
    
    headers = {
        'x-api-key': '1TfJdFVsa5aE6xl443jeX76v4ntxVrNfuaEEBEUf',
        'Content-Type': 'application/json'
    }
    
    data = {
        "text": text,
        "grantPermissions": [
            "access filler words",
            "access overlong sentences",
            "access synonyms",
            "access unfavorable phrases",
            "access word frequency",
            "access punctuation correction"
        ]
    }

    # generate response
    response = requests.post(url, headers=headers, json=data)

    # work through response from duden API
    if response.status_code == 200:
        print("API request successful.")
        result = response.json()
        print(result)
        
        if 'data' in result:
            # Correct spelling mistakes
            if 'spellAdvices' in result['data']:
                spell_advices = result['data']['spellAdvices']
                
                for advice in spell_advices:
                    if advice['type'] == 'gram' or advice['type'] == 'orth':
                        corrected = advice['proposals'][0]
                        corrected_text = text[:advice['offset']] + corrected + text[advice['offset'] + advice['length']:]
                        print("Corrected Text:")
                        print(corrected_text)
                        return corrected_text
            
            # Correct style mistakes
            if 'styleAdvices' in result['data']:
                style_advices = result['data']['styleAdvices']
                
                for advice in style_advices:
                    if advice['type'] == 'gram' or advice['type'] == 'orth':
                        corrected = advice['proposals'][0]
                        corrected_text = text[:advice['offset']] + corrected + text[advice['offset'] + advice['length']:]
                        print("Corrected Text:")
                        print(corrected_text)
                        return corrected_text

        # Default to no errors found
        print("No case-related errors found in the response.")
        return text
    else:
        # Case: Erro with api call
        print(f"API request failed with status code: {response.status_code}")
        print("Error response:")
        print(response.text)
        return text
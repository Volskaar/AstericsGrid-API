import language_tool_python

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

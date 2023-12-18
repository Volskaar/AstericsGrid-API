import spacy
import service_language_tool

# load german spacy model

nlp = spacy.load("de_core_news_sm")

#####################################################################

# debug function to inspect all tokens of a sentence

def inspect_tokens(sentence):
    doc = nlp(sentence)
    for token in doc:
        print(f"Text: {token.text}, Dep: {token.dep_}, Tag: {token.tag_}, Pos: {token.pos_}")

#####################################################################
        
# extract the subject from the sentence

def extract_subject(sentence):
    doc = nlp(sentence)
    
    subject = None
    print("Test 0")
    for token in doc:
        # checks for "Pronomen", "Präpositionen" und "Nomen" mit den dependencies sb, nom und nk
        # Stop after finding the first subject
        if token.pos_ in ["PRON", "PROPN", "NOUN"] and token.dep_ in ["sb", "nom", "nk"]:
            subject = token.text
            break
    
    print("Subjekt: " + str(subject))
    return subject

#####################################################################

# extract verb from sentence
# Stop after finding the first subject
def extract_verb(sentence):
    doc = nlp(sentence)
    
    for token in doc:
        if token.dep_ == "ROOT" and token.pos_ == "VERB":
            verb = token.text
    
    print("Verb: " + verb)
    return verb

#####################################################################

# put verb into base-form for text-file search

def lemmatize_word(word):
    doc = nlp(word)
    return doc[0].lemma_

#####################################################################

#  check if Subject is plural or singular

def is_plural(word):
    return False

#####################################################################

def read_line_file(word, line):
    verb = lemmatize_word(word)
    word_path = "verbs/" + verb + ".txt"
    print(word_path)

    try:
        with open(word_path, 'r', encoding="utf-8") as datei:
            zeilen = datei.readlines()
            if 1 <= line <= len(zeilen):
                return zeilen[line - 1]
            else:
                return f"Die Datei hat weniger als {line} Zeilen."
    except FileNotFoundError:
        return "Die angegebene Datei wurde nicht gefunden."

#####################################################################
    
def getSubjects(type):
    subjects = []
    word_path = "subjects/" + type + ".txt"

    try:
        with open(word_path, 'r', encoding="utf-8") as datei:
            print(word_path)
            zeilen = datei.readlines()
            for line in zeilen:
                subjects.append(str(line))
    
    except FileNotFoundError:
        return "Die angegebene Datei wurde nicht gefunden."
    
    return subjects

#####################################################################

# turn all uppercase to leading capitalization

def normalize_capitalization(sentence):
    doc = nlp(sentence)

    # normalize tokens in doc
    normalized_tokens = [token.text.capitalize() for token in doc]
    
    # Verbinden Sie die Tokens zu einem normalisierten Text
    normalized_text = ' '.join(normalized_tokens)
    
    return normalized_text

#####################################################################

# use selfmade python-language-tool spellchecker

def spellcheck(sentence):
    corrected_text = service_language_tool.handle_request(sentence)
    return corrected_text

#####################################################################

def rule_based_correction(sentence):
    # sentence = normalize_capitalization(sentence)
    sentence = spellcheck(sentence.lower())

    inspect_tokens(sentence)

    verb = extract_verb(sentence)
    subject = extract_subject(sentence)

    # create subject arrays out of textfiles
    singular_subjects = getSubjects("singular")
    plural_subjects = getSubjects("plural")

    # get rule for case 1
    if subject.lower() == "ich":
        correct_verb = read_line_file(verb, 1)

    # get rule for case 2
    elif subject.lower() == "du":
        correct_verb = read_line_file(verb, 2)

    # get rule for case 3
    elif str(subject.lower()) in str(singular_subjects):
        correct_verb = read_line_file(verb, 3)
    
    # get rule for case 4
    elif subject.lower() == "wir":
        correct_verb = read_line_file(verb, 4)
    
    # get rule for case 5
    elif subject.lower() == "ihr":
        correct_verb = read_line_file(verb, 5)

    # get rule for case 6
    elif subject.lower() in plural_subjects:
        correct_verb = read_line_file(verb, 6)

    
    # rules for default case
    else:
        print("Edge Case / unbekanntes Subjekt")
        correct_verb = read_line_file(verb, 3)

    corrected_sentence = sentence.replace(verb, correct_verb.strip())

    return corrected_sentence

        

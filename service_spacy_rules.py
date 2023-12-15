import spacy

nlp = spacy.load("de_core_news_sm")

#####################################################################

def extract_subject(sentence):
    doc = nlp(sentence)
    
    for token in doc:
        # Check for nominal subjects
        if "subj" in token.dep_ and "nom" in token.dep_:
            subject = token.text
            break  # Stop after finding the first subject
    
    print("Subj: " + subject)
    return subject

def extract_verb(sentence):
    doc = nlp(sentence)
    
    for token in doc:
        # Check for the main verb (ROOT) in the sentence
        if "ROOT" in token.dep_ and "verb" in token.tag_:
            verb = token.text
            break  # Stop after finding the main verb
    
    print("Verb: " + verb)
    return verb

#####################################################################

def is_plural(word):
    print("check word: " + word)
    doc = nlp(word)
    if len(doc) > 0:
        return doc[0].tag_ == "NNS"
    else:
        # Handle the case where the doc has no tokens (e.g., empty string)
        return False

#####################################################################

def read_line_file(word, line):
    word_path = "/verbs/" + word + ".txt"
    print(word_path)

    try:
        with open(word_path, 'r') as datei:
            zeilen = datei.readlines()
            if 1 <= line <= len(zeilen):
                return zeilen[line - 1]
            else:
                return f"Die Datei hat weniger als {line} Zeilen."
    except FileNotFoundError:
        return "Die angegebene Datei wurde nicht gefunden."

#####################################################################

def rule_based_correction(sentence):
    verb = extract_verb(sentence)
    subject = extract_subject(sentence)

    # get rule for case 1
    if subject == "ich" or subject == "Ich":
        correct_verb = read_line_file(verb, 1)
    
    # get rule for case 2
    elif subject == "du" or subject == "Du":
        correct_verb = read_line_file(verb, 2)
    
    # get rule for case 4
    elif subject == "wir" or subject == "Wir":
        correct_verb = read_line_file(verb, 4)
    
    # get rule for case 5
    elif subject == "ihr" or subject == "Ihr":
        correct_verb = read_line_file(verb, 5)

    # rules for case 3 (multiple)
    elif subject == "er" or subject == "Er":
        correct_verb = read_line_file(verb, 3)

    elif subject == "sie" or subject == "Sie":
        correct_verb = read_line_file(verb, 3)

    elif subject == "es" or subject == "Es":
        correct_verb = read_line_file(verb, 3)

    # rules for case 3 (things/names) or case 6 (things/names plural)
    else:
        if is_plural(subject):
            correct_verb = read_line_file(verb, 6)
        else:
            correct_verb = read_line_file(verb, 3)

    corrected_sentence = sentence.replace(verb, correct_verb.strip())

    return corrected_sentence;

        

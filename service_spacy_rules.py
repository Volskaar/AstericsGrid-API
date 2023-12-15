import spacy

# load german spacy model

nlp = spacy.load("de_core_news_sm")

#####################################################################

# debug function to inspect all tokens of a sentence

def inspect_tokens(sentence):
    doc = nlp(sentence)
    for token in doc:
        print(f"Text: {token.text}, Dep: {token.dep_}, Tag: {token.tag_}")

#####################################################################
        
# extract the subject from the sentence

def extract_subject(sentence):
    doc = nlp(sentence)
    
    subject = None
    
    for token in doc:
        # Check for pronouns in subject position
        if token.pos_ == "PRON" or token.pos_ == "NOUN" and token.dep_ in ["sb", "da", "nom"]:
            subject = token.text
            break  # Stop after finding the first subject
    
    print("Subjekt: " + str(subject))
    return subject

#####################################################################

# extract verb from sentence

def extract_verb(sentence):
    doc = nlp(sentence)
    
    for token in doc:
        # Check for the main verb (ROOT) in the sentence
        #if token.dep_ == "ROOT" and token.pos_ == "VERB":
        if token.dep_ == "ROOT":
            verb = token.text
            break  # Stop after finding the main verb
    
    print("Verb: " + verb)
    return verb

#####################################################################

# put verb into base-form for text-file search

def lemmatize_word(word):
    doc = nlp(word)
    # Assuming the word is a single token, take the lemma of the first token
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
    inspect_tokens(sentence)

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

    # rules for case 3 (things/names singular) or case 6 (things/names plural)
    else:
        if is_plural(subject):
            print("Ist plural")
            correct_verb = read_line_file(verb, 6)
        else:
            print("Ist singular")
            correct_verb = read_line_file(verb, 3)

    corrected_sentence = sentence.replace(verb, correct_verb.strip())

    return corrected_sentence;

        

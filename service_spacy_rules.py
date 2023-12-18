import spacy

# load german spacy model

nlp = spacy.load("de_core_news_sm")

#####################################################################

# debug function to inspect all tokens of a sentence

def inspect_tokens(sentence):
    doc = nlp(sentence.capitalize())


    for token in doc:
        print(f"Text: {token.text.capitalize()}, Dep: {token.dep_}, Tag: {token.tag_}, Pos: {token.pos_}")

#####################################################################
        
# extract the subject from the sentence

def extract_subject(sentence):
    doc = nlp(sentence.capitalize())
    
    subject = None

    for token in doc:
        # Check for pronouns in subject position
        if token.pos_ in ["PRON", "PROPN", "NOUN"] and token.dep_ in ["sb", "nom", "nk"]:
            subject = token.text
            break  # Stop after finding the first subject
    
    print("Subjekt: " + str(subject))
    return subject

#####################################################################

# extract verb from sentence

def extract_verb(sentence):
    doc = nlp(sentence.capitalize())
    
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
def getSubjects(type):
    subjects = []
    word_path = "subjects/" + type + ".txt"
    print(word_path)

    try:
        with open(word_path, 'r', encoding = "utf-8") as datei:
            zeilen = datei.readlines()
            for line in zeilen:
                subjects.append(str(line))
    
    except FileNotFoundError:
        return "Die angegebene Datei wurde nicht gefunden."
    
    return subjects
#####################################################################


def rule_based_correction(sentence):
    inspect_tokens(sentence)

    verb = extract_verb(sentence)
    subject = extract_subject(sentence)

    # create subject arrays out of textfiles
    singular_subjects = getSubjects("singular")
    plural_subjects = getSubjects("plural")

    # get rule for case 1
    if subject.lower() == "ich":
        correct_verb = read_line_file(verb, 1)
        print("Test 1")

    # get rule for case 2
    elif subject.lower() == "du":
        correct_verb = read_line_file(verb, 2)
        print("Test 2")

    # get rule for case 3
    elif subject.lower() + "\n" in singular_subjects:
        correct_verb = read_line_file(verb, 3)
        print("Test 3")
    
    # get rule for case 4
    elif subject.lower() == "wir":
        correct_verb = read_line_file(verb, 4)
        print("Test 4")
    
    # get rule for case 5
    elif subject.lower == "ihr":
        correct_verb = read_line_file(verb, 5)
        print("Test 5")

    # get rule for case 6
    elif subject.lower() + "\n" in plural_subjects:
        correct_verb = read_line_file(verb, 6)
        print("Test 6")

    
    # rules for default case
    else:
        print("Edge Case / unbekanntes Subjekt")
        correct_verb = read_line_file(verb, 3)

    corrected_sentence = sentence.replace(verb.upper(), correct_verb.strip().upper())

    print(corrected_sentence)

    return corrected_sentence

        

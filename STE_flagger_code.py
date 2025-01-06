from pypdf import PdfReader
import re
import spacy
from nltk.tokenize import sent_tokenize
from nltk.tokenize import PunktTokenizer

def collect_vocab_from_guidelines():
    """"
    Reads the guideline pdf (ASD-STE100, issue 8) and collects the approved words into a set and not approved words into a dictionnary.

    Params:
       -
    Returns: 
        not allowed_vocab: a dictionnary that holds as keys the not approved words from the guidelines, value is a dictionnary holding not approved word's POS and suggested word choice 
        
     """
    reader = PdfReader('ASD-STE100-ISSUE-8.pdf')
    #print(len(reader.pages)) #424 pages, dictionnary starts at p. 136 python-wise
    start = 136 # p. STE vocabulary starts at

    allowed_vocab = set()   # will hold duplicates, need to be removed if we decide to go with replacing these, for now, not needed !
    not_allowed_vocab = {}

    # Regex pattern
    not_allowed_pattern = r"\b[a-z][a-z]*\s\(.*\)" # match all complete words that are not capitalized (thus, not approved) and are followed by an opening paranthesis
    allowed_pattern = r"\b[A-Z][A-Z]*\s\(" # match all complete words that are capitalized (thus, approved) and are followed by an opening paranthesis
    for i in range(start, len(reader.pages)):
        content = reader.pages[i]
        page_content_text = content.extract_text()   # will result in a list
        #print(page_content_text)
        # not approved matches
        NA_matches = re.findall(not_allowed_pattern, page_content_text) # returns a list of all matches
        #print(NA_matches)
        for item in NA_matches:
            #print(item)
            allowed_notallowed = item.split(" ", 2)
            if len(allowed_notallowed) == 3:
                not_allowed_vocab[allowed_notallowed[0]] = {'POS': allowed_notallowed[1].replace("(", "").replace(")", ""), 'SUGGESTION': allowed_notallowed[2].lower()}
            else:
                not_allowed_vocab[allowed_notallowed[0]] = {'POS': allowed_notallowed[1].replace("(", "").replace(")", ""), 'SUGGESTION': None}
    

    # approved matches
    A_matches = re.findall(allowed_pattern, page_content_text)
    for item in A_matches:
        item_cleaned = item.replace(" (", "")
        allowed_vocab.add(item_cleaned.lower())

    return not_allowed_vocab


#print(collect_vocab_from_guidelines())

def check_for_not_approved(text_document):

    """
    Creates a RegEx pattern from the keys of the not_allowed_vocab (SIMPLIFIED TECHNICAL ENGLISH), which will then be used to match eventual not approved words used in our corpus.
    Tags the document's text with SpaCy library. Checks that the not allowed words found from the document match both Spacy POS tags and the suggested word's POS.

    Params:
        text_document - input document which vocabulary will be checked for not approved words

    Returns:
        Flagged_lines (list) - holds all the lines from the documents that contain problematic (not approved) words as well as lines that do not contain vocabulary deviating from the guidelines.
    """

    not_allowed_vocab = collect_vocab_from_guidelines() #getting the dictionnary
    # for POS-tagging the content in the input document:
    nlp = spacy.load("en_core_web_sm")  
    SpaCy_POS_tag_2_STE_POS_tag = {
        "VERB" : "v",
        "NOUN" : "n",
        "ADP" : "prep",
        "ADJ" : "adj",
        "AUX" : "v",
        "PRON": "pron",
        "ADV" : "adv",
        "SCONJ" : "conj",
        "PROPN" : "n",
        "DET" : "art",
        "PART" : "prep",
        "CCONJ" : "conj"
    }
    

    # reading and reconstructing sentences

    paragraphs = []
    current_paragraph = []
    with open(text_document, encoding="utf-8") as file:
        text = file.read()


    for line in text.splitlines():     
        #print(line)
        if line.strip():  # If line is not empty
            current_paragraph.append(line.strip())
            #print("this is current_paragraph: ", current_paragraph)
        else:  # a blank line indicates end of paragraph
            if current_paragraph:
                paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []
    if current_paragraph:  # Add the last paragraph
        paragraphs.append(" ".join(current_paragraph))

    #print("this is current paragraph: ", current_paragraph)
    # ***********        
    flagged_lines = []
    problem_words = r'\b({})\b'.format('|'.join(map(re.escape, not_allowed_vocab.keys()))) # \b(not_approved_word_1|not_approved_word_2|not_aproved_word_3|not_approved_word_4)\b
    skippable_words = ['to']  # TO DO: ADNN MODE
    line_n = 0
    deviations_to_analyze = []
    # ***********

    for sentence in paragraphs:
        line_n += 1
    #for line_number, line in enumerate(file, start=1):
        content = nlp(sentence)
        matches = re.findall(problem_words, sentence.lower())  # case-insensitive matching of problem words
        if matches: # case where there is a non-approved word match
            issues = []
            for word in matches:  # Handle multiple matches
                suggestion = not_allowed_vocab[word]['SUGGESTION'] # retrieving the suggestion from the dictionary
                #print("this is the suggestion", suggestion)
                if suggestion:
                    suggestion_pos = suggestion.split()
                problem_words_pos = not_allowed_vocab[word]['POS']
                for token in content:   # in the line below we are verifying that the POS tags match between the not allowed word and the suggested word, we are also filtering out some stopwords matched by the regex
                    if token.text.lower() == word and problem_words_pos == SpaCy_POS_tag_2_STE_POS_tag.get(token.pos_) and suggestion_pos[1].replace("(", "").replace(")","") == problem_words_pos and word not in skippable_words:
                       if suggestion:
                           issues.append({
                           "word": word,
                           "POS": problem_words_pos,
                           "Replacement suggestion": suggestion
                       })
            # adding an 'entry' in the problematic lines - list, contains information about the issues in that sentence
            if issues:  
                deviations_to_analyze.append((sentence.strip(),issues))
                flagged_lines.append({
                    'line_number': line_n,
                    'line': sentence.strip(),
                    'issues': issues
            })
            else: # adding instances that have a regex match but do not fullfill all the conditions (the POSs don't match) as entry
                flagged_lines.append({
                    'line_number': line_n,
                    'line': sentence.strip(),  
                })
        # adding an 'entry' in the problematic lines- list, the sentence that DOES NOT HAVE ANY ISSUES!
        else:
            flagged_lines.append({
                'line_number': line_n,
                'line': sentence.strip(),

            })
                
    #print(deviations_to_analyze[:50])
    return flagged_lines

flagged_sentences = check_for_not_approved("./honda_manual.txt")




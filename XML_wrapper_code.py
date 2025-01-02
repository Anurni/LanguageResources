from STE_flagger_code import flagged_sentences
import xml.etree.ElementTree as ET
from xml.dom import minidom
from tools import all_tools
from nltk.util import bigrams
import nltk

print(flagged_sentences)

all_things = []

for dicts in flagged_sentences:
    if dicts['line'] != "MAINTENANCE":
        all_things.append(dicts['line'])

#print(all_things)



def wrap_sentences_in_xml(flagged_sentences):
    """
    Wraps sentences with and without identified issues into an XML structure grouped by headings and their content (body).

    Params:
        flagged_sentences: List of dictionaries, where each dictionary contains:
            - 'line_number': int, line number of the sentence.
            - 'line': str, the actual sentence text.
            AND IN CASE THE SENTENCE CONTAINS STE-DEVIATING WORDS:
            - 'issues': list of dictionaries, where each dictionary contains:
                - 'word': str, the problematic word.
                - 'POS': str, the part of speech of the problematic word.
                - 'Replacement suggestion': str, the suggestion for replacement and its POS-tag.
        
    Returns:
        str: A formatted hierarchical XML string structure representing the sentences and issues.
    """
    # Root element for the XML document
    root = ET.Element("Manual_maintenance")
    flagged_sentences = flagged_sentences
    #warning_words = ["Do not", "do not", "careful", "beware"]
        
    # creating the XML structure
    for paragraph in flagged_sentences:
        print(paragraph)
        if paragraph['line'] != "MAINTENANCE" and len(paragraph['line'])>2:
            if paragraph['line'].isupper():
                xmlparagraph = ET.SubElement(root, "Paragraph", {"topic": paragraph['line']}) # tag for headings
            else:
                if "Do not" in paragraph['line'] or "do not" in paragraph['line']: # tag for warnings
                    content = ET.SubElement(xmlparagraph, "Warning")
                    content.text = paragraph['line']
                    tools = ET.SubElement(content, "Tools")
                else:
                    content = ET.SubElement(xmlparagraph, "Instruction") # tag for instructions
                    content.text = paragraph['line']
                    tools = ET.SubElement(content, "Tools")

            # here, we create the tagging of the tools
            already_added_tools = set()
            tokenize_line = nltk.word_tokenize(paragraph['line'])
            line_as_bigrams = list(bigrams(tokenize_line))
            for bigramm in line_as_bigrams: # compound names of tools
                bigramm = " ".join(bigramm)
                if bigramm in all_tools and bigramm not in already_added_tools:
                    tool = ET.SubElement(tools, "Tool")
                    tool.text = bigramm
                    already_added_tools.add(bigramm)

            for unigramm in tokenize_line: #single word tools
                if unigramm in all_tools and unigramm not in already_added_tools:
                    tool = ET.SubElement(tools, "Tool")
                    tool.text = unigramm
                    already_added_tools.add(unigramm)

            try:
            # adding issues as child elements, need to try since not all of the lines are problematic
                for issue in paragraph['issues']:
                    issue_element = ET.SubElement(content, "STE-issue", {
                        "word": issue["word"],
                        "POS": issue["POS"]
                    })
                    suggestion = issue["Replacement suggestion"]
                    if suggestion:
                        suggestion_element = ET.SubElement(issue_element, "Suggestion")
                        suggestion_element.text = suggestion
            except KeyError:
                pass

    # Format XML for pretty printing
    xml_string = ET.tostring(root, encoding='unicode')
    return minidom.parseString(xml_string).toprettyxml(indent="  ")


print(wrap_sentences_in_xml(flagged_sentences))

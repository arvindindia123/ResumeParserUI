import spacy
from spacy.matcher import Matcher

"""Load a spaCy model from an installed package or a local path.
extract_candidate_name function extracts the name of a candidate from
the resume content passed to it
Library is developed as part of research project in Usha Martin University

"""




def extract_candidate_name(resume_text):
    # load pre-trained model
    nlp = spacy.load('en_core_web_sm')
    # initialize matcher with a vocab
    matcher = Matcher(nlp.vocab)
    nlp_text = nlp(resume_text)
    # First name and Last name are always Proper Nouns
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]

    matcher.add('NAME', [pattern])
    matches = matcher(nlp_text, as_spans=True)
    print(matches[0])
    return matches[0]




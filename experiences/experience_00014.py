import spacy
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')

text = (
     "Ilit Loan is not Trilit Oan but I am Kloa Qdgh. But I am Olan Ghio"
)

doc = nlp(text)

matcher = Matcher(nlp.vocab)

def extract_full_name(nlp_doc):
     pattern = [{"POS": "PROPN"}, {"POS": "PROPN"}]
     matcher.add("FULL_NAME", [pattern])
     matches = matcher(nlp_doc)
     for _, start, end in matches:
         span = nlp_doc[start:end]
         print(span.text)

extract_full_name(doc)
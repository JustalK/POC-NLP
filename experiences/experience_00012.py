import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

text = (
    "This is a simple example."
)

doc = nlp(text)
# http://localhost:5000/
displacy.serve(doc, style="dep")


import spacy
nlp = spacy.load("en_core_web_sm")
text = "Kevin is doing his work."

doc = nlp(text)

for chunk in doc.noun_chunks:
    print(chunk)


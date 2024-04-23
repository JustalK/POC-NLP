import spacy
nlp = spacy.load('en_core_web_sm')

text = (
    "This is a simple example."
)

doc = nlp(text)
print([f"{token}:{token.pos_}" for token in doc])
print([f"{token}:{token.pos_}" for token in doc if token.pos_ == "NOUN"])


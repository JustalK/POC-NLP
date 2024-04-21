import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

print("Verbes:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
print("Nom propres:", [token.lemma_ for token in doc if token.pos_ == "PROPN"])
print("Auxiliaires:", [token.lemma_ for token in doc if token.pos_ == "AUX"])
print("Adverbes:", [token.lemma_ for token in doc if token.pos_ == "ADP"])
print("Symboles:", [token.lemma_ for token in doc if token.pos_ == "SYM"])
print("Numbers:", [token.lemma_ for token in doc if token.pos_ == "NUM"])
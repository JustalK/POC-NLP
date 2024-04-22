import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("This is a first sentance. This is the second one. And this is the third one.")
sentences = list(doc.sents)
print(len(sentences))

print([s for s in sentences])

[print(f"{d}: {d.idx}") for d in doc]
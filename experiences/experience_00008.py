import spacy
nlp = spacy.load('en_core_web_sm')

text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)

doc = nlp(text)
for token in doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token)} : {str(token.lemma_)}")

# [Gus, Proto, Python, developer, currently, working, London, -, based, Fintech, company, ., interested, learning, Natural, Language, Processing, .]
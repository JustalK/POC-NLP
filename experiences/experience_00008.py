import spacy
nlp = spacy.load('en_core_web_sm')

text = (
    "The founder founded the company and found the secret of life. Found is a verb"
)

doc = nlp(text)
for token in doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token)} : {str(token.lemma_)}")
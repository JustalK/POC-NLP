import spacy
nlp = spacy.load('en_core_web_sm')

text = (
    "This is a simple example. We gonna preprocessing the text."
)

doc = nlp(text)

def is_token_allowed(token):
    return bool(
        token
        and str(token).strip()
        and not token.is_stop
        and not token.is_punct
    )

def preprocess_token(token):
    return token.lemma_.strip().lower()

print([
    preprocess_token(token)
    for token in doc
    if is_token_allowed(token)
])


import spacy
from collections import Counter
nlp = spacy.load('en_core_web_sm')

text = (
    "Sing sang sung is a verb in english. The singer is a job. Singing is also a verb. To sing is the infinitif"
)

doc = nlp(text)
words = [
     token.lemma_.lower()
     for token in doc
     if not token.is_stop and not token.is_punct
 ]

print(words)
print(Counter(words).most_common(5))
# [Gus, Proto, Python, developer, currently, working, London, -, based, Fintech, company, ., interested, learning, Natural, Language, Processing, .]
import spacy
from spellchecker import SpellChecker
import re

spell = SpellChecker()

text = "This is a texx I woud like to corect"

nlp = spacy.load('en_core_web_sm')
sentence = nlp(text)

docx = [token.text for token in sentence]
print(docx)

misspelled = spell.unknown(docx)

for word in misspelled:
    print(word, "---->", spell.correction(word))

print("=============================")

corrected_sentence = []
for word in docx:
    if word in misspelled:
        corrected_sentence.append(spell.correction(word))
    else:
        corrected_sentence.append(word)

print(' '.join(corrected_sentence))


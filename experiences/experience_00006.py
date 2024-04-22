import spacy
nlp = spacy.load('en_core_web_sm')

# infix_finditer: A function that handles non-whitespace separators, such as hyphens
infix_re = spacy.util.compile_infix_regex(['is'])
nlp.tokenizer.infix_finditer = infix_re.finditer

doc = nlp("thatisaistext")
print([t.text for t in doc])
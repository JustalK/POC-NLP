import spacy
nlp = spacy.load('en_core_web_sm')

# prefix_search: A function that handles preceding punctuation, such as opening parentheses.
prefix_regex = spacy.util.compile_prefix_regex([])
# suffix_search: A function that handles succeeding punctuation, such as closing parentheses.
suffix_regex = spacy.util.compile_suffix_regex(['\\.'])
nlp.tokenizer.prefix_search = prefix_regex.search
nlp.tokenizer.suffix_search = suffix_regex.search

doc = nlp("[A] works for [B] in [C].")
print([t.text for t in doc])
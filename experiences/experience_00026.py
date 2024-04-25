import spacy
import nltk
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
nltk.download('wordnet')
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacy_wordnet", after='tagger')

# Domain can be found here: https://wndomains.fbk.eu/hierarchy.html
# It changes the result if the domains change
# try: "sexuality"
domains = ['person']
enriched_sentence = []
sentence = nlp('I love my wife')

# For each token in the sentence
for token in sentence:
    # We get those synsets within the desired domains
    synsets = token._.wordnet.wordnet_synsets_for_domain(domains)
    print(synsets)
    if not synsets:
        enriched_sentence.append(token.text)
    else:
        lemmas_for_synset = [lemma for s in synsets for lemma in s.lemma_names()]
        # If we found a synset in the economy domains
        # we get the variants and add them to the enriched sentence
        enriched_sentence.append('({})'.format('|'.join(set(lemmas_for_synset))))

# Let's see our enriched sentence
print(' '.join(enriched_sentence))



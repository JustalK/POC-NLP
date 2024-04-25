import spacy
from spacy import Language
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("sentencizer")


@Language.component("component")
def component_func(doc):
    # modify Doc and return it
    if len(doc.ents) > 0:
        print(len(doc.ents))
    return doc

nlp.add_pipe("component", before="ner")
component = nlp.add_pipe("component", name="custom_name", last=True)

print(nlp.pipe_names)

print("==========================================")
texts = [
    "Revenue exceeded twelve billion dollars, with a loss of $1b."
]

for doc in nlp.pipe(texts):
    # Do something with the doc here
    print(doc.ents)
    print([token.lemma_ for token in doc])

print("==========================================")
for doc in nlp.pipe(texts, disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer", "ner"]):
    # Do something with the doc here
    print(doc.ents)
    print([token.lemma_ for token in doc])

analysis = nlp.analyze_pipes(pretty=True)




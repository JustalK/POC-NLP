import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
text = (
    "Facebook inc. and Google are situated"
    " in Los Angeles or the City of London and has"
    " world-class search system. Laureen is the CEO. This is a very big company of $1 billion"
)

doc = nlp(text)

for ent in doc.ents:
    print(
        f"""
    {ent.text = }
    {ent.start_char = }
    {ent.end_char = }
    {ent.label_ = }
    spacy.explain('{ent.label_}') = {spacy.explain(ent.label_)}"""
)

displacy.serve(doc, style="ent")

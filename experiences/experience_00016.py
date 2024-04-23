import spacy
nlp = spacy.load("en_core_web_sm")
text = "Kevin is doing his work."

doc = nlp(text)

print(doc[2])
print([token.text for token in doc[2].children])
print(f"Neighbor left: {doc[2].nbor(-1)}")
print(f"Neighbor right: {doc[2].nbor()}")
print(f"Token left: {[token.text for token in doc[2].lefts]}")
print(f"Token right: {[token.text for token in doc[2].rights]}")
print(f"Subtree: {list(doc[2].subtree)}")
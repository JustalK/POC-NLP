from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")

encoded_input = tokenizer(["This is the text of kevin.", "This is A.", "This is the text of K."], padding=True, truncation=True)
tensor = tokenizer(["This is the text of kevin.", "This is A.", "This is the text of K."], padding=True, truncation=True, return_tensors="pt")
print(encoded_input['input_ids'])
print(tensor['input_ids'])

for sent in encoded_input['input_ids']:
    print(tokenizer.decode(sent))

import torch
from transformers import AutoTokenizer, BertConfig, BertModel, AutoModelForSequenceClassification

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

raw_inputs = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!",
]
inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")
# print(inputs)

# Building the config
# config = BertConfig()

# Building the model from the config
# model = BertModel(config)

# Already trained
# model = BertModel.from_pretrained("bert-base-cased")

# print(config)


# encoded_input = tokenizer(["I am kevin."], padding=True, truncation=True, return_tensors="pt")
# for sent in encoded_input['input_ids']:
#     print(tokenizer.decode(sent))

# ========================================================
# Another chapter

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
sequence = "Using a transformer network is simple"
tokens = tokenizer.tokenize(sequence)
# print(tokens)

ids = tokenizer.convert_tokens_to_ids(tokens)
# print(ids)

input_ids = torch.tensor([ids])
output = model(input_ids)
# print(output.logits)

# ========================================================
# Another chapter

sequence1_ids = [[200, 200, 200]]
sequence2_ids = [[200, 200]]

print(tokenizer.pad_token_id)

batched_ids = [
    [200, 200, 200],
    [200, 200, tokenizer.pad_token_id],
]

attention_mask = [
    [1, 1, 1],
    [1, 1, 0],
]

print(model(torch.tensor(sequence1_ids)).logits)
print(model(torch.tensor(sequence2_ids)).logits)
print(torch.tensor(batched_ids))
print(model(torch.tensor(batched_ids), attention_mask=torch.tensor(attention_mask)).logits)

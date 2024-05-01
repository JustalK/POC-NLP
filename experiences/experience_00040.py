import torch
from transformers import AutoTokenizer, pipeline, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
example = "My name is Sylvain and I work at Hugging Face in Brooklyn."
encoding = tokenizer(example)
# print(type(encoding))

# print(tokenizer.is_fast)
# print(encoding.tokens())
# print(encoding.word_ids())

start, end = encoding.word_to_chars(3)
# print(example[start:end])

# ====================================================
token_classifier = pipeline("token-classification", aggregation_strategy="simple")
# print(token_classifier(example))
# ====================================================

model_checkpoint = "dbmdz/bert-large-cased-finetuned-conll03-english"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint)
#print(model.config)

example = "My name is Sylvain and I work at Hugging Face in Brooklyn."
inputs = tokenizer(example, return_tensors="pt", return_offsets_mapping=True)
# print(len(inputs.tokens()))
outputs = model(**inputs)
# print(inputs["input_ids"].shape)
print(outputs.logits.shape)
# 1 sentance * 19 tokens * 9 feature out from the model

probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)[0].tolist()
predictions = outputs.logits.argmax(dim=-1)[0].tolist()
print(predictions)

results = []
tokens = inputs.tokens()
offsets = inputs["offset_mapping"]

for idx, pred in enumerate(predictions):
    label = model.config.id2label[pred]
    if label != "O":
        start, end = offsets[idx]
        results.append(
            {
                "entity": label,
                "score": probabilities[idx][pred],
                "word": tokens[idx],
                "start": start,
                "end": end,
            }
        )

print(results)

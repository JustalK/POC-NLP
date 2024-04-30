from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorWithPadding

checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

raw_datasets = load_dataset("glue", "mrpc")
#print(raw_datasets)

raw_train_dataset = raw_datasets["train"]
#print(raw_train_dataset[0])

#print(raw_train_dataset.features)

inputs = tokenizer("This is the first sentence.", "This is the second sentence.")
#print(inputs)

def tokenize_function(example):
    return tokenizer(example["sentence1"], example["sentence2"], truncation=True)

tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
print(tokenized_datasets)

samples = tokenized_datasets["train"][:8]
samples = {k: v for k, v in samples.items() if k not in ["idx", "sentence1", "sentence2"]}
print([len(x) for x in samples["input_ids"]])

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
batch = data_collator(samples)
print({k: v.shape for k, v in batch.items()})
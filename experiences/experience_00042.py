from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

sentance="Héllò hôw are ü?"
normalized_sentance=tokenizer.backend_tokenizer.normalizer.normalize_str(sentance)
pre_tokenized_sentance=tokenizer.backend_tokenizer.pre_tokenizer.pre_tokenize_str(normalized_sentance)
print(pre_tokenized_sentance)
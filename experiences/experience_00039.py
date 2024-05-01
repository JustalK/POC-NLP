from datasets import load_dataset
from transformers import AutoTokenizer


print("===============================")
# Normal tokenizer - Bad tokenization
old_tokenizer = AutoTokenizer.from_pretrained("gpt2")
example = '''def add_numbers(a, b):
    """Add the two numbers `a` and `b`."""
    return a + b'''

tokens = old_tokenizer.tokenize(example)
print(tokens)
print("===============================")

# This can take a few minutes to load, so grab a coffee or tea while you wait!
raw_datasets = load_dataset("code_search_net", "python")
print(raw_datasets)

def get_training_corpus():
    return (
        raw_datasets["train"][i : i + 1000]["whole_func_string"]
        for i in range(0, len(raw_datasets["train"]), 1000)
    )


training_corpus = get_training_corpus()
tokenizer = old_tokenizer.train_new_from_iterator(training_corpus, 52000)
tokens = tokenizer.tokenize(example)
print(tokens)

tokenizer.save_pretrained("experience_00039/code-search-net-tokenizer")

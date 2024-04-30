from transformers import AutoTokenizer
from datasets import load_from_disk
from datasets import load_dataset
import html

# ========================================================================================
data_files = {"train": "experience_00036/drugsComTrain_raw.tsv", "test": "experience_00036/drugsComTest_raw.tsv"}
# \t is the tab character in Python
drug_dataset = load_dataset("csv", data_files=data_files, delimiter="\t")

drug_dataset = drug_dataset.rename_column(
    original_column_name="Unnamed: 0", new_column_name="patient_id"
)

drug_dataset = drug_dataset.filter(lambda x: x["condition"] is not None)

def lowercase_condition(example):
    return {"condition": example["condition"].lower()}

drug_dataset.map(lowercase_condition)

def compute_review_length(example):
    return {"review_length": len(example["review"].split())}

drug_dataset = drug_dataset.map(compute_review_length)

drug_dataset = drug_dataset.filter(lambda x: x["review_length"] > 30)
drug_dataset = drug_dataset.map(lambda x: {"review": html.unescape(x["review"])}, batched=True)

drug_sample = drug_dataset["train"].shuffle(seed=42).select(range(1000))
# ========================================================================================

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
# default: use_fast: true
slow_tokenizer = AutoTokenizer.from_pretrained("bert-base-cased", use_fast=False)


def slow_tokenize_function(examples):
    return slow_tokenizer(examples["review"], truncation=True)


tokenized_dataset = drug_dataset.map(slow_tokenize_function, batched=False, num_proc=8)
print(tokenized_dataset)

def tokenize_and_split(examples):
    return tokenizer(
        examples["review"],
        truncation=True,
        max_length=128,
        return_overflowing_tokens=True,
    )

result = tokenize_and_split(drug_dataset["train"][0])
print([len(inp) for inp in result["input_ids"]])

drug_dataset_clean = drug_dataset["train"].train_test_split(train_size=0.8, seed=42)
# Rename the default "test" split to "validation"
drug_dataset_clean["validation"] = drug_dataset_clean.pop("test")
# Add the "test" set to our `DatasetDict`
drug_dataset_clean["test"] = drug_dataset["test"]

drug_dataset_clean.save_to_disk("experience_00036/drug-reviews")

drug_dataset_reloaded = load_from_disk("experience_00036/drug-reviews")
print(drug_dataset_reloaded)
import html
from datasets import load_dataset

squad_it_dataset = load_dataset("json", data_files="experience_00036/SQuAD_it-train.json", field="data")
#print(squad_it_dataset)

data_files = {"train": "experience_00036/SQuAD_it-train.json", "test": "experience_00036/SQuAD_it-test.json"}
squad_it_dataset = load_dataset("json", data_files=data_files, field="data")
#print(squad_it_dataset)

# Using direct gzip
data_files = {"train": "experience_00036/SQuAD_it-train.json.gz", "test": "experience_00036/SQuAD_it-test.json.gz"}
squad_it_dataset = load_dataset("json", data_files=data_files, field="data")

# Direct download
# url = "https://github.com/crux82/squad-it/raw/master/"
# data_files = {
#    "train": url + "SQuAD_it-train.json.gz",
#    "test": url + "SQuAD_it-test.json.gz",
#}
#squad_it_dataset = load_dataset("json", data_files=data_files, field="data")
#print(squad_it_dataset)

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
# Peek at the first few examples
print(drug_sample[:3])
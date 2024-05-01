from datasets import load_dataset
import requests
#import psutil
import time
import math
from pathlib import Path
import pandas as pd
from tqdm.notebook import tqdm

GITHUB_TOKEN = ""
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

# This takes a few minutes to run, so go grab a tea or coffee while you wait :)
#pubmed_dataset = load_dataset("hwang2006/PUBMED_title_abstracts_2020_baseline")
#print(pubmed_dataset)

#print(f"RAM used: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} MB")


url = "https://api.github.com/repos/huggingface/datasets/issues?page=1&per_page=1"
response = requests.get(url)

print(response.json())

def fetch_issues(
    owner="huggingface",
    repo="datasets",
    num_issues=10_000,
    rate_limit=5_000,
    issues_path=Path("."),
):
    if not issues_path.is_dir():
        issues_path.mkdir(exist_ok=True)

    batch = []
    all_issues = []
    per_page = 100  # Number of issues to return per page
    num_pages = math.ceil(num_issues / per_page)
    base_url = "https://api.github.com/repos"

    for page in tqdm(range(num_pages)):
        # Query with state=all to get both open and closed issues
        query = f"issues?page={page}&per_page={per_page}&state=all"
        issues = requests.get(f"{base_url}/{owner}/{repo}/{query}", headers=headers)
        batch.extend(issues.json())

        if len(batch) > rate_limit and len(all_issues) < num_issues:
            all_issues.extend(batch)
            batch = []  # Flush batch for next time period
            print(f"Reached GitHub rate limit. Sleeping for one hour ...")
            time.sleep(60 * 60 + 1)

    all_issues.extend(batch)
    df = pd.DataFrame.from_records(all_issues)
    df.to_json(f"{issues_path}/{repo}-issues.jsonl", orient="records", lines=True)
    print(
        f"Downloaded all the issues for {repo}! Dataset stored at {issues_path}/{repo}-issues.jsonl"
    )

fetch_issues()




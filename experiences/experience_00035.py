from transformers import pipeline, AutoTokenizer, CamembertForMaskedLM

camembert_fill_mask = pipeline("fill-mask", model="camembert-base")
results = camembert_fill_mask("Le camembert est <mask> :)")

print(results)

print("===========================")

tokenizer = AutoTokenizer.from_pretrained("camembert-base")
model = CamembertForMaskedLM.from_pretrained("camembert-base")
camembert_fill_mask = pipeline("fill-mask", model=model, tokenizer=tokenizer)
print(results)


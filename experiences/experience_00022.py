from transformers import pipeline

sentiment_pipeline = pipeline(task="sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")
data = ["I love you", "I hate you", "I like this product", "This is not okay-ish"]
print(sentiment_pipeline(data))

import spacy
import eng_spacysentiment
nlp = eng_spacysentiment.load()
#sentiment_analyzer = nlp.create_pipe("sentiment_analyzer")
#nlp.add_pipe(sentiment_analyzer)

good_text = "This is a good thing! It has some default that need to be fixed but the result is good for my doing."
neutral_text = "This is ok but nothing crazy."
very_bad_text = "This is a very bad product."

#sentiment = sentiment_analyzer(text)

#print(sentiment.score) 

print(nlp(good_text).cats)
print(nlp(neutral_text).cats)
print(nlp(very_bad_text).cats)


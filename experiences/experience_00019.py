import spacy
import math
from spacy import displacy
from collections import Counter
from heapq import nlargest

nlp = spacy.load("en_core_web_sm")
text = (
    "Rock musicians in the mid-1960s began to advance the album ahead of the single as the dominant form of recorded music expression and consumption, with the Beatles at the forefront of this development. Their contributions lent the genre a cultural legitimacy in the mainstream and initiated a rock-informed album era in the music industry for the next several decades. By the late 1960s classic rock period, a number of distinct rock music subgenres had emerged, including hybrids like blues rock, folk rock, country rock, southern rock, raga rock, and jazz rock, which contributed to the development of psychedelic rock, influenced by the countercultural psychedelic and hippie scene. New genres that emerged included progressive rock with extended artistic elements, glam rock, highlighting showmanship and visual style. In the second half of the 1970s, punk rock reacted by producing stripped-down, energetic social and political critiques. Punk was an influence in the 1980s on new wave, post-punk and eventually alternative rock."
)

doc = nlp(text)
nbrSentance = len(list(doc.sents))

keyword = []
pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
for token in doc:
    if(not token.is_stop and not token.is_punct and token.pos_ in pos_tag):
        keyword.append(token.lemma_.lower())

freq_word = Counter(keyword)
keys = freq_word.keys()

# Number of term total in each sentance
sum_key = {}
for index, sent in enumerate(doc.sents):
    sum_key[index] = 0
    for word in sent:
        if word.lemma_ in keys:
            sum_key[index] += 1

# Number of reference of term t in each sentance
n = {}
for index, sent in enumerate(doc.sents):
    n[index] = {}
    for word in sent:
        word_clean = word.lemma_.lower()
        if word_clean in keys:
            if word_clean in n[index].keys():
                n[index][word_clean] += 1
            else:
                n[index][word_clean] = 1

# Calcul of tf
tf = {}
for index, sent in enumerate(doc.sents):
    tf[index] = {}
    for word in n[index]:
        tf[index][word] = n[index][word]/sum_key[index]

# Total sentance in corpus
D = sum(1 for x in doc.sents)
print(D)

# For each key, number of sentence containing it 
d = {}
for key in keys:
    d[key] = 0
    for sent in doc.sents:
        isIn = False
        for word in sent:
            word_clean = word.lemma_.lower()
            if word_clean == key:
                isIn = True
                break
        if isIn:
            d[key] += 1

# IDF
idf = {}
for key in keys:
    idf[key] = math.log(D/d[key])

# TF-IDF
tfIdf = {}
for index, sent in enumerate(tf):
    tfIdf[index] = {}
    for key in keys:
        if key in tf[index] and key in idf:
            tfIdf[index][key] = tf[index][key] * idf[key]

most_common_word = freq_word.most_common(15)
words = list()
for word in most_common_word:
    words.append(word[0])

sent_strength={}
for index, sent in enumerate(doc.sents):
    sent_strength[index] = 0
    for weigth in tfIdf[index]:
        print(weigth, words)
        if weigth in words:
            sent_strength[index] += tfIdf[index][weigth]

print(sent_strength)
print("=============================================")

word_targeted = most_common_word[2][0]
print(word_targeted)

sent_strength_by_key={}
for index, sent in enumerate(doc.sents):
    sent_strength_by_key[index] = 0
    for key in tfIdf[index]:
        if key == word_targeted:
            sent_strength_by_key[index] += tfIdf[index][key]

print(sent_strength_by_key)


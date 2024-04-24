import spacy
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
        keyword.append(token.text)

freq_word = Counter(keyword)
most_common_word = freq_word.most_common(5)

print(most_common_word)

max_freq = most_common_word[0][1]

for word in freq_word.keys():
    freq_word[word] = (freq_word[word]/max_freq)

print(freq_word.most_common(5))

sent_strength={}
for sent in doc.sents:
    for word in sent:
        if word.text in freq_word.keys():
            if sent in sent_strength.keys():
                sent_strength[sent]+=freq_word[word.text]
            else:
                sent_strength[sent]=freq_word[word.text]

print(sent_strength)
print("=============================================")
summarize_sentances = nlargest(3, sent_strength, key=sent_strength.get)
print(summarize_sentances[0])


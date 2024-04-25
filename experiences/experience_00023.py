import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')

text = (
    "Rock musicians in the mid-1960s began to advance the album ahead of the single as the dominant form of recorded music expression and consumption, with the Beatles at the forefront of this development. Their contributions lent the genre a cultural legitimacy in the mainstream and initiated a rock-informed album era in the music industry for the next several decades. By the late 1960s classic rock period, a number of distinct rock music subgenres had emerged, including hybrids like blues rock, folk rock, country rock, southern rock, raga rock, and jazz rock, which contributed to the development of psychedelic rock, influenced by the countercultural psychedelic and hippie scene. New genres that emerged included progressive rock with extended artistic elements, glam rock, highlighting showmanship and visual style. In the second half of the 1970s, punk rock reacted by producing stripped-down, energetic social and political critiques. Punk was an influence in the 1980s on new wave, post-punk and eventually alternative rock."
)

tokens = sent_tokenize(text)
vectorizer = TfidfVectorizer(stop_words='english')
tf_idf = vectorizer.fit_transform(tokens)

sentence_score = [i.sum() / len(i.data) for i in tf_idf]
avg_sent = sum(sentence_score)/len(sentence_score)

summary = [tokens[index] for index, score in enumerate(sentence_score) if score > avg_sent]
output_text = ''.join([str(i) for i in summary])
print(output_text)


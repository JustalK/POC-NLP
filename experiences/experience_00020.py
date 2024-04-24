import spacy
from transformers import pipeline

summarizer = pipeline(task="summarization", model="facebook/bart-large-cnn")

text = (
    "Rock musicians in the mid-1960s began to advance the album ahead of the single as the dominant form of recorded music expression and consumption, with the Beatles at the forefront of this development. Their contributions lent the genre a cultural legitimacy in the mainstream and initiated a rock-informed album era in the music industry for the next several decades. By the late 1960s classic rock period, a number of distinct rock music subgenres had emerged, including hybrids like blues rock, folk rock, country rock, southern rock, raga rock, and jazz rock, which contributed to the development of psychedelic rock, influenced by the countercultural psychedelic and hippie scene. New genres that emerged included progressive rock with extended artistic elements, glam rock, highlighting showmanship and visual style. In the second half of the 1970s, punk rock reacted by producing stripped-down, energetic social and political critiques. Punk was an influence in the 1980s on new wave, post-punk and eventually alternative rock."
)

summary = summarizer(text, max_length=130, min_length=30, length_penalty=2.0, num_beams=4)
print("\nGenerated Summary with Bart:\n", summary[0]['summary_text'])

summarizerGoogle = pipeline(task="summarization", model="google-t5/t5-small")

summary = summarizerGoogle(text, max_length=130, min_length=30, length_penalty=2.0, num_beams=4)
print("\nGenerated Summary with Google:\n", summary[0]['summary_text'])

translator = pipeline(task="translation_en_to_fr", model="google-t5/t5-small")
print("\nTranslation in french:\n",translator(text))


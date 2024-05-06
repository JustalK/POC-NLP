# POC-NLP

## Goal

This project is a POC on `Spacy` and `Hugging Face`. I have discovered the NLP recently and I wanted to understand how it works and what we can do with it.  
So I read the documentation from start to end and made some experience with the library.  
The project is made with `Python`.

## Plan of the presentation

I explain with all the details how I build the project and my way of working.

- [Goal](#goal)
- [Plan of the presentation](#plan-of-the-presentation)
- [Running](#running)
- [Experiences](#experiences)
- [Documentation](#documentation)
- [Links](#links)
- [Helper](#helper)
- [Tutorial](#tutorial)
- [Explanation](#explanation)
- [Git](#git)
- [To Read](#to-read)
- [System](#system)

## Running

In order to install the dependency, use poetry:

```bash
$ poetry install
```

PS: Some version of the dependencies might need to be play with in some experience in order to make it work.

To run an experience, just go on the experiences project and use the following command:

```bash
$ python experience_00001.py
```

## Experiences

- **Experience_00001**: Just testing if Spacy is installed properly
- **Experience_00002**: Playing with the matcher
- **Experience_00003**: Counting the number of sentance
- **Experience_00004**: Tokenization with custom tokenizer
- **Experience_00005**: Tokenization with custom prefixes and suffixes
- **Experience_00006**: Tokenization with custom infix
- **Experience_00007**: Stop words
- **Experience_00008**: Lemmatization (limit of it)

racination != lemmatization
exemple:
found => find (trouver)
found => found (fonder)

- **Experience_00009**: Counting identical similar
- **Experience_00010**: Counting with lemmatization (error with sung)
- **Experience_00011**: Part-Of-Speech - PoS
- **Experience_00012**: DisplaCy - vizualization of POS
- **Experience_00013**: Preprocessing function (lower-lemma-remove is_punct and is_stop)
- **Experience_00014**: Using matcher for searching based on PoS
- **Experience_00015**: Dependency parsing

Root of the sentance
headwords and dependents

words = nodes
Gramatical relationships = edges

- **Experience_00016**: Subtree navigation
- **Experience_00017**: Shallow parsing (noun_chuck)
- **Experience_00018**: NER (Name entity recognition)
- **Experience_00019**: Summarization (Extrative Summarization)
- **Experience_00020**: Summarization (Abstractive Summarization) using Hugging Face Transformers
- **Experience_00021**: Tokenization with Hugging Face
- **Experience_00022**: Sentiment Analyzis with Hugging Face
- **Experience_00023**: TF-IDF
- **Experience_00024**: Pipeline Spacy
- **Experience_00025**: Training NER pipeline using Kaggle medical dataset 

Use the processData.py to create a document in the right spacy format

To get the base_config: https://spacy.io/usage/training

```bash
# To init config with ner
$ python -m spacy init config --pipeline ner config.cfg
# Train the pipeline
python -m spacy train config.cfg --output ./ --paths.train ./train.spacy --paths.dev ./train.spacy
```

![4](./documentation/images/4.png)

- **Experience_00026**: Looking for synonyms from a certain WordNet domains
- **Experience_00027**: Spellcheck a text and correct it
- **Experience_00028**: Sentiment Analysis with Spacy (spacy 3.5 - 3.6)
- **Experience_00029**: Question-Answering with Hugging Face (squad model)

#### Hugging Face

- **Experience_00030**: Understanding Attention Mask, Input IDs and Special Word [CLS] [SEP]
- **Experience_00031**: Summary with Hugging Face
- **Experience_00032**: Batching a dataset - chapter 3
- **Experience_00033**: Fine tune model (not enough memory) - chapter 3
- **Experience_00034**: Fine tune model for (not enough memory) - chapter 3
Computer not enough ram for continuing on this chapter
- **Experience_00034**: Playing with model - chapter 4
- **Experience_00036**: Playing with dataset function - chapter 5
- **Experience_00037**: Creating a new cleaner dataset and save it - chapter 5
- **Experience_00038**: Fecthing data and creating a dataset - chapter 5
- **Experience_00039**: Train a tokenizer - chapter 6
- **Experience_00040**: Fast tokenizer - chapter 6
- **Experience_00040**: Fast tokenizer with QA - chapter 6
- **Experience_00042**: Normalization and Pret-tokenization - chapter 6
- **Experience_00043**: Fine Tuning a model for NER - chapter 6


## Documentation

#### Lexeme

![1](./documentation/images/1.png)

#### Text Preprocessing

![2](./documentation/images/2.png)

## Links

Attention is all you need!

- [Spacy API](https://spacy.io/api/tokenizer)
- [Spacy Course](https://github.com/explosion/spacy-course/blob/master/chapters/en/slides/chapter2_01_data-structures-1.md)
- [Spacy Tutorial](https://www.tutorialspoint.com/spacy/spacy_util_compile_prefix_regex.htm)
- [Spacy Python](https://realpython.com/natural-language-processing-spacy-python/)

- [Spacy Video][https://www.youtube.com/@hugolarochelle/videos]

- [Hugging Face Documentation](https://huggingface.co/docs/transformers/training)

## Helper

- [Transformer](https://medium.com/geekculture/transformer-state-of-the-art-natural-language-processing-ad9bef141a9e)
- [Transformer embedding](https://www.baeldung.com/cs/transformer-text-embeddings)
- [Word2Vec](https://www.baeldung.com/cs/ml-word2vec-topic-modeling)
- [Cosine similarity](https://www.baeldung.com/cs/ml-similarities-in-text)
- [Word Rang Algo](https://ankitnitjsr13.medium.com/text-rank-algorithm-a8c2cc58ea9c#:~:text=TextRank%20Explanation%3A,similarity%20between%20sentences%20is%20used.)
- [NLP Pipeline](https://medium.com/@asjad_ali/understanding-the-nlp-pipeline-a-comprehensive-guide-828b2b3cd4e2)

## Tutorial

- [Spacy Tutorial](https://kamalkhumar22.medium.com/)
- [Spacy Advanced Course](https://course.spacy.io/en)
- [Custom NER Pipeline](https://blog.futuresmart.ai/building-a-custom-ner-model-with-spacy-a-step-by-step-guide)
- [Fine Tune Spacy Model](https://www.freecodecamp.org/news/how-to-fine-tune-spacy-for-nlp-use-cases/)
- [Rules QA - Type](https://spotintelligence.com/2023/01/20/question-answering-qa-system-nlp/)

## Explanation
- [Tokenization](https://medium.com/@abdallahashraf90x/tokenization-in-nlp-all-you-need-to-know-45c00cfa2df7)
- [Tokenization 2](https://towardsdatascience.com/word-subword-and-character-based-tokenization-know-the-difference-ea0976b64e17)
- [Embedding layer](https://medium.com/@kunalmishra78/part-1-input-embeddings-and-positional-encodings-343fca6ecc2e)
- [Transformer](https://datasciencedojo.com/blog/transformer-models/)
- [Transformer - explanation](https://towardsdatascience.com/transformers-89034557de14)
- [Positional encoding](https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/)
- [Positional encoding - Calcul](https://medium.com/@hunter-j-phillips/positional-encoding-7a93db4109e6)
- [Self-Attention Calcul](https://sebastianraschka.com/blog/2023/self-attention-from-scratch.html)
- [Self-Attention Explanation - Genius](https://medium.com/@geetkal67/attention-networks-a-simple-way-to-understand-self-attention-f5fb363c736d)
- [Multi-Headed Attention](https://medium.com/@geetkal67/attention-networks-a-simple-way-to-understand-multi-head-attention-3bc3409c4312)
- [Multi-Head Graph](https://towardsdatascience.com/transformers-explained-visually-part-3-multi-head-attention-deep-dive-1c1ff1024853)
- [Multi-Head Attention - More details about Add + Norm](https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial6/Transformers_and_MHAttention.html)
- [Feed Forward](https://towardsdatascience.com/simplifying-transformers-state-of-the-art-nlp-using-words-you-understand-part-4-feed-foward-264bfee06d9)
- [Feed Forward Calcul](https://medium.com/@hunter-j-phillips/position-wise-feed-forward-network-ffn-d4cc9e997b4c)
- [Feed Forward Youtube Calcul](https://www.youtube.com/watch?v=4JKuyfejWTU)
- [Feed Forward Neural Network](https://www.youtube.com/watch?v=bljuV9WDvAA)

Deep Network -> Hidden Layer > 1

- [Position-wise FFN - Explaination](https://www.youtube.com/watch?v=jTzJ9zjC8nU)
- [Position-Wise FFN - Calcul](https://nlp.seas.harvard.edu/2018/04/01/attention.html)

## GIT

- [Summarization](https://github.com/aniass/text-summarizer/blob/main/Text_summary.ipynb)

## To Read

- [50 NLP Questions](https://www.geeksforgeeks.org/nlp-interview-questions/)

## System

Ubuntu Version: Ubuntu 20.04.1
Node Version: v20.12.2
Npm Version: v10.5.2

The version are manage with [Volta](https://docs.volta.sh/guide/getting-started).

```bash
# Get the latest version of ubuntu
$ lsb_release -a

# Get the version of node
$ node -v

# Get the version of npm
$ npm -v
```
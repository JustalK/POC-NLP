import re
import spacy
from spacy.tokenizer import Tokenizer

nlp = spacy.load("en_core_web_sm")

doc = "This is my email justal.kevin@gmail.com"

prefix_re = spacy.util.compile_prefix_regex(nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(nlp.Defaults.suffixes)
custom_infixes = [r"@"]

infix_re = spacy.util.compile_infix_regex(list(nlp.Defaults.infixes) + custom_infixes)

nlp.tokenizer = Tokenizer(
    nlp.vocab,
    prefix_search=prefix_re.search,
    suffix_search=suffix_re.search,
    infix_finditer=infix_re.finditer,
    token_match=None
)

custom_tokenizer_about_doc = nlp(doc)
print([token.text for token in nlp(doc)])
'''

Lemmatises the text

'''

#  Import necessary libraries
import spacy


class TextProcess:

    def __init__(self):
        # Load corpus
        self.nlp = spacy.load('en_core_web_sm')  # Could also use medium and large corpus

    # Lemmatise the text
    def lemma(self, text):
        doc = self.nlp(text)
        text_lemma_lst = []
        for token in doc:
            text_lemma_lst.append(token.lemma_)
        text_string = ' '.join(text_lemma_lst)
        text_string = self.nlp(text_string)
        return text_string

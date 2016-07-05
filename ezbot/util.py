import re
import string
import nltk
from nltk.corpus import wordnet


class TextNormalizer(object):
    def __init__(self, text=''):
        self.punctuation_pattern = re.compile('[%s]' % re.escape(string.punctuation))

        self.contraction_patterns = [(re.compile(regex), repl) for (regex, repl) in [
            (r'won\'t', 'will not'),
            (r'can\'t', 'cannot'),
            (r'i\'m', 'i am'),
            (r'ain\'t', 'is not'),
            (r'(\w+)\'ll', '\g<1> will'),
            (r'(\w+)n\'t', '\g<1> not'),
            (r'(\w+)\'ve', '\g<1> have'),
            (r'(\w+)\'s', '\g<1> is'),
            (r'(\w+)\'re', '\g<1> are'),
            (r'(\w+)\'d', '\g<1> would')
        ]]

        self.text = text.lower()
        self.tokenized_text = None

        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')

    def remove_punctuation(self):
        if not self.tokenized_text:
            raise Exception('Must call parse before remove_punctuation.')
        self.tokenized_text = [token for token in [re.sub(self.punctuation_pattern, '', t)
                                                   for t in self.tokenized_text] if token != '']
        return self

    def parse(self):
        self.tokenized_text = nltk.word_tokenize(self.text)
        return self

    def replace_contractions(self):
        for (pattern, repl) in self.contraction_patterns:
            (self.text, count) = re.subn(pattern, repl, self.text)
        return self

    def remove_repeats(self):
        def replace(word):
            if wordnet.synsets(word):
                return word
            repl_word = self.repeat_regexp.sub(r'\1\2\3', word)
            if repl_word != word:
                return replace(repl_word)
            else:
                return repl_word

        self.tokenized_text = [replace(token) for token in self.tokenized_text]
        return self

    def set_text(self, text):
        self.text = text.lower()
        self.tokenized_text = None
        return self

    def get_tokens(self):
        return self.tokenized_text

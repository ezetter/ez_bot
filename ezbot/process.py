from ezbot.util import TextNormalizer

QUIT_WORDS = ['quit', 'done', 'exit']

normalizer = TextNormalizer()


def process_request(text, remove_punctuation=True):
    (normalizer
     .set_text(text)
     .replace_contractions()
     .parse()
     .remove_repeats()
     )
    if remove_punctuation:
        normalizer.remove_punctuation()
    tagged_words = normalizer.get_pos()
    action = get_action(tagged_words)
    response = get_response(tagged_words, action)
    return action, response, tagged_words


def get_action(tagged_words):
    words = get_words(tagged_words)
    if len(words) == 1 and words[0] in QUIT_WORDS:
        return 'DONE'
        # if is_question(tagged_words)


def get_response(tokens, action):
    if action == 'DONE':
        return 'OK, Bye Bye...'
    return 'What did you say?'


def get_words(tagged_words):
    return [word[0] for word in tagged_words]


def get_tags(tagged_words):
    return [tag[1] for tag in tagged_words]


def is_question(tagged_words):
    return 'WP' in get_tags(tagged_words)


def get_verbs(tagged_words):
    return [word[0] for word in tagged_words if word[1] == 'VBZ']


def get_nouns(tagged_words):
    return [word[0] for word in tagged_words if word[1] == 'NN']

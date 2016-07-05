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
    tokens = normalizer.get_tokens()
    action = get_action(tokens)
    response = get_response(tokens, action)
    return action, response, tokens


def get_action(tokens):
    if len(tokens) == 1 and tokens[0] in QUIT_WORDS:
        return 'DONE'

    if len(tokens) == 3 and tokens[2] in QUIT_WORDS and tokens[1] == 'am':
        return 'DONE'


def get_response(tokens, action):
    if action == 'DONE':
        return 'OK, Bye Bye...'
    return 'OK'

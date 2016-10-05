import unittest
from ezbot.util import TextNormalizer
from ezbot.process import process_request


class TextNormalizerTestCase(unittest.TestCase):
    def test_all_together(self):
        self.assertEqual(
            TextNormalizer("Don't you wantt to dance?")
                .replace_contractions().parse().remove_punctuation().remove_repeats().get_tokens(),
            ['do', 'not', 'you', 'want', 'to', 'dance'])

    def test_all_together_set_text(self):
        self.assertEqual(
            TextNormalizer().set_text("Don't you wantt to dance?")
                .replace_contractions().parse().remove_punctuation().remove_repeats().get_tokens(),
            ['do', 'not', 'you', 'want', 'to', 'dance'])

    def test_remove_repeats(self):
        self.assertEqual(TextNormalizer("baaa baaaa blackkk sheep").parse().remove_repeats().get_tokens(),
                         ['baa', 'baa', 'black', 'sheep'])

    def test_contractions_i_am(self):
        self.assertEqual(TextNormalizer("I'm done").replace_contractions().parse().get_tokens(), ['i', 'am', 'done'])


class ProcessRequestTestCase(unittest.TestCase):
    def test_process_done(self):
        self.assertEqual(process_request('done')[1], 'OK, Bye Bye...')


if __name__ == '__main__':
    unittest.main()

import main_yandex
import unittest

class TestYandexTranslater(unittest.TestCase):

    def test_response_code(self):
        code = t.translater('trnsl.1.1.20200321T131833Z.751fc8fe0c12f0d0.d7007fb280b90f86676cdebf291b157a9747bf2e', \
        'en-ru', 'hi')['code']
        self.assertEqual(code, 200)

    def test_translation(self):
        text = ' '.join(t.translater('trnsl.1.1.20200321T131833Z.751fc8fe0c12f0d0.d7007fb280b90f86676cdebf291b157a9747bf2e', \
        'en-ru', 'hi')['text'])
        self.assertEqual(text, 'привет')

    def test_wrong_key(self):
        code = t.translater('test', 'en-ru', 'hi')['code']
        self.assertEqual(code, 401)

    def test_wrong_lang(self):
        code = t.translater('trnsl.1.1.20200321T131833Z.751fc8fe0c12f0d0.d7007fb280b90f86676cdebf291b157a9747bf2e', \
        'test', 'hi')['code']
        self.assertEqual(code, 501)

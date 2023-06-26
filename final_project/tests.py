from deep_translator import MyMemoryTranslator
from machinetranslation.translator import Translator
import unittest
class TranslationTests(unittest.TestCase):
    def setUp(self):
        self.translator = Translator(MyMemoryTranslator())
    def test_englishToFrench(self):
        # Test translation of 'Hello' to French
        english_text = 'Hello'
        expected_result = 'Bonjour'
        result = self.translator.englishToFrench(english_text)
        self.assertEqual(result, expected_result)
    def test_frenchToEnglish(self):
        # Test translation of 'Bonjour' to English
        french_text = 'Bonjour'
        expected_result = 'Hello'
        result = self.translator.frenchToEnglish(french_text)
        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()
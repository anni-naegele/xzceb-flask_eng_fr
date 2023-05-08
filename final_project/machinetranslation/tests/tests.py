import unittest
from machinetranslation.translatortranslator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase): 

    def test_french_to_english(self): 
        # 2a. assertEqual frenchToEnglish
        self.assertEqual(french_to_english('Ami'), 'Friend')
        # 2b. assertNotEqual frenchToEnglish
        self.assertNotEqual(french_to_english('Fleur'), 'Father')
        # 3. Test for null input for frenchToEnglish
        #self.assertIsNone(french_to_english(''), 'Test value is none.')
        # 6. Test for the translation of the world ‘Bonjour’ and ‘Hello’.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_english_to_french(self): 
        # 2c. assertEqual englishToFrench
        self.assertEqual(english_to_french('Friend'), 'Ami')
        # 2d. assertNotEqual englishToFrench
        self.assertNotEqual(english_to_french('Father'), 'Fleur')
        # 4. Test for null input for englishToFrench
        #self.assertIsNone(english_to_french(''), 'Test value is none.')
        # 5. Test for the translation of the world ‘Hello’ and ‘Bonjour’.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

if __name__=='__main__': 
    unittest.main()
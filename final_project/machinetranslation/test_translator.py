import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestEnglishToFrenchNull(unittest.TestCase):
    def test1(self): 
        self.assertEqual(english_to_french(""), "")

class TestFrenchToEnglish(unittest.TestCase):    
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        
class TestFrenchToEnglishNull(unittest.TestCase):    
    def test2(self):
        self.assertEqual(french_to_english(""), "")

unittest.main()

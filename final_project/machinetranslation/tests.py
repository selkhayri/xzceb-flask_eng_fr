import unittest
import json

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self): 
        self.assertEqual(englishToFrench("Hello")["translations"][0]["translation"], "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):    
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour")["translations"][0]["translation"], "Hello")
        
unittest.main()

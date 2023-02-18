'''
Date: Feb 01
Challenge: Count each letter from a given sentence
'''

#sentence = input("Frame a sentence: ")
def CountEachLetters(sentence):

    listSentence = list(sentence)
    setSentence = set(listSentence)
    dict = {}
    for iEach in setSentence:
        v = 0
        for jEach in listSentence:
            if iEach in jEach:
                v += 1
        dict[iEach] = v
    return dict
    
#print(CountEachLetters(input()))

import unittest

class VerifyLettersCount(unittest.TestCase):
    def testCountLetters(self):
        self.assertEqual(CountEachLetters('a'), {'a':1})
        self.assertEqual(CountEachLetters('ab'), {'a':1, 'b':1})
        self.assertEqual(CountEachLetters('aabbbcccc'), {'a':2, 'b':3, 'c':4})

if __name__ == "__main__":
    unittest.main()
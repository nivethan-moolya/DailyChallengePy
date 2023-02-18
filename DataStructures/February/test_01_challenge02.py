'''
Date: Feb 01
Challenge: Count each word from the given sentence
'''

#sentence = input("Frame a sentence:")

def countWords(sentence):
    splitSentence = sentence.split(' ')
    dict = {}

    for iEach in splitSentence:
        v = 0
        for jEach in splitSentence:
            if iEach == jEach:
                v += 1
        dict[iEach] = v
    #print(dict)
    return dict

import unittest


class VerifyLettersCount(unittest.TestCase):
    def testCountLetters(self):
        self.assertEqual(countWords('How are you?'), {'How':1, 'are':1, 'you?':1})

if __name__ == "__main__":
    unittest.main(verbosity=2)
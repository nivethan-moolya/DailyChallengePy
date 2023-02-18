'''
Date: Feb 07
Challenge: Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''

def GetMidLetter(value):
        if len(value) % 2 == 0:
            return ""
        else:
            position = len(value)//2
            return value[position]

import unittest

class VerifyMiddleleeter(unittest.TestCase):
    def testMidLetter(self):
        self.assertEqual(GetMidLetter('abc'), 'b')
        self.assertEqual(GetMidLetter('qwertyu'), 'r')
        self.assertEqual(GetMidLetter('asdf'), '')

if __name__=="__main__":
    unittest.main()

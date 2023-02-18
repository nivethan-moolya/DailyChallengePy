'''
Date: Feb 08
Challenge: Double letters
The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. 
For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
'''

def double_letters(value):
    k = [n for n in range(len(value)-1) if value[n] == value[n+1]]
    #print(k)
    return len(k)>0

#print(double_letters('hheloo'))

import unittest


class VerifyDoubleLetters(unittest.TestCase):
    def testDoubleLetters(self):
        self.assertEqual(double_letters('Hello'), True)
        self.assertEqual(double_letters('Helo'), False)
        self.assertEqual(double_letters('qwerty'), False)
        self.assertEqual(double_letters('qwertty'), True)
        self.assertNotEqual(double_letters('aa'), False)

if __name__=='__main__':
    unittest.main(verbosity=2)
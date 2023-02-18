'''
Date: Feb 02
Challenge: Check if the given two strings are Anagram
'''

'''
s1 = input(f'Provide me the first string: ')
s2 = input(f'Provide me the second string: ')

Output:
    Provide me the first string: abc def
    Provide me the second string: pqr xyz
    [' ', 'a', 'b', 'c', 'd', 'e', 'f']
    [' ', 'p', 'q', 'r', 'x', 'y', 'z']
'''


def anagramCheck(String01, String02):
    if(sorted(String01) == sorted(String02)):
        return 'Given strings are Anagrams'
    else:
        return 'Given strings are not an Anagrams'

import unittest


class VerifyAnagram(unittest.TestCase):
    def testAnagramValidation(self):
        self.assertEqual(anagramCheck('abc d', 'd abc'), 'Given strings are Anagrams')
        self.assertEqual(anagramCheck('abcd', 'd abc'), 'Given strings are not an Anagrams')

if __name__ == "__main__":
    unittest.main(verbosity=2)
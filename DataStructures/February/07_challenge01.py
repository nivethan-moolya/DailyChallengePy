'''
Date: Feb 07
Challenge: Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''

def capital_indexes(value):
    l = []
    for i in range(0,len(value)):
        if value[i].isupper():
            l.append(i)
    return l


# #Short answer
# def capital_indexes(value):
#     l = [i for i in range(len(value)) if value[i].isupper()]
#     print(l)

#print(capital_indexes(input(f'Provide the String: ')))

import unittest

class VerifyCapitalIndex(unittest.TestCase):
    def testCapitalIndex(self):
        self.assertEqual(capital_indexes('aBcd'), [1])
        self.assertEqual(capital_indexes('AbCdEf'), [0,2,4])
        self.assertNotEqual(capital_indexes('AbCdEf'), (0,2,4))

if __name__=="__main__":
    unittest.main()
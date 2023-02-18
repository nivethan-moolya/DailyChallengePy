'''
Date: Feb 08
Challenge: Type check
Write a function named only_ints that takes two parameters. 
Your function should return True if both parameters are integers, and False otherwise.
For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
'''

def only_ints(a,b):
    return type(a) == int and type(b) == int
        

#print(only_ints(4, 1))

import unittest

class VerifyBoolean(unittest.TestCase):
    def testOnlyInts(self):
        self.assertEqual(only_ints(2,5), True)
        self.assertEqual(only_ints(19283,1), True)
        self.assertEqual(only_ints(-2,0), True)
        self.assertEqual(only_ints(2,'5'), False)
        self.assertNotEqual(only_ints(2,'5'), True)
        
if __name__=='__main__':
    unittest.main()
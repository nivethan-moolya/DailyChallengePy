"""
Date: Feb 12
Challenge: Sample Input
1222311
Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
Explanation
First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.
Also, note the single space within each compression and between the compressions.
Refer: https://www.hackerrank.com/challenges/compress-the-string/problem
"""
from itertools import groupby

def SampleInput(value):
    listOutput = []
    iterValue = groupby(value)
    for uniqueKey, repeatValue in iterValue:
        lenValue = len(list(repeatValue))
        listOutput.append((lenValue, int(uniqueKey)))
    #print(listOutput)
    return listOutput

#print(SampleInput('1222311'))

import unittest


class VerifySampleTest(unittest.TestCase):
    def testSampleTest(self):
        self.assertEqual(SampleInput('1222311'), [(1, 1), (3, 2), (1, 3), (2, 1)])
        self.assertEqual(SampleInput('1222344'), [(1, 1), (3, 2), (1, 3), (2, 4)])
        self.assertNotEqual(SampleInput('1'), [(1, 2)])

if __name__=='__main__':
    unittest.main(verbosity=2)
'''
Date: Feb 06
Challenge: Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.

Examples
next_edge(8, 10) ➞ 17
next_edge(5, 7) ➞ 11
next_edge(9, 2) ➞ 10

Notes
(side1 + side2) - 1 = maximum range of third edge.
The side lengths of the triangle are positive integers.
Don't forget to return the result.

'''
def next_edge(side1:int, side2:int):
    return (side1+side2) -1

import unittest


class VerifyNextThirdTriangleSide(unittest.TestCase):

    def testNextTriagleSide(self):
        self.assertEqual(next_edge(5,4), 8)
        self.assertEqual(next_edge(10,4), 13)
        self.assertNotEqual(next_edge(11,11), 22)


if __name__ == "__main__":
    unittest.main(verbosity=2)

#next_edge(int(input(f'Prodide 1st side for the Triangle:')), int(input(f'Prodide 2nd side for the Triangle:')))
"""
Topic: Python challenge
Challenge:Cricket Balls to Overs!
In cricket, an over consists of six deliveries a bowler bowls from one end. Create a function that takes the number of balls 
bowled by a bowler and calculates the number of overs and balls bowled by him/her. 
Return the value as a float, in the format overs.balls.
Examples
total_overs(2400) ➞ 400

total_overs(164) ➞ 27.2
# 27 overs and 2 balls were bowled by the bowler.

total_overs(945) ➞ 157.3
# 157 overs and 3 balls were bowled by the bowler.

total_overs(5) ➞ 0.5
Notes
The number following the decimal point represents the balls remaining after the last over. Therefore, it will only ever have a value of 1-5.
Source: https://edabit.com/challenge/guR6aa2zytfZvywMS
"""

def total_overs(value):
    qualitative_output = int(value/6)
    decimal_output =  value%6
    if decimal_output != 0:
        return float(f'{qualitative_output}.{decimal_output}')
    else:
        return int(qualitative_output)


import unittest
class VerifyCricketBalls(unittest.TestCase):
    def testBallCounts(self):
        self.assertEqual(total_overs(2400), 400)
        self.assertEqual(total_overs(164), 27.2)
        self.assertEqual(total_overs(945), 157.3)
        self.assertEqual(total_overs(5), 0.5)
        self.assertEqual(total_overs(7), 1.1)
        self.assertEqual(total_overs(15), 2.3)
        self.assertEqual(total_overs(0), 0)

if __name__=='__main__':
    unittest.main()
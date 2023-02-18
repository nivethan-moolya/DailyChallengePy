'''
Date: Feb 07
Challenge: Online status
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
For example, consider the following dictionary:
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online"
}
In this case, the number of people online is 2.
Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
Your function should return the number of people who are online.
'''

import json
import unittest

#status = '{"Nikhil" :  "online", "Akshat" :  "online", "Akash" :  "offline"}'
def online_count(status):

    statuses = json.loads(status)
    v = list(statuses.values()) 
    l = [a for a in v if 'online' in a]
    #print(len(l))
    return len(l)

class VerifyOnline(unittest.TestCase):
    def testOnlineUsers(self):
        self.assertEqual(online_count('{"Nikhil" :  "online", "Akshat" :  "online"}'), 2)
        self.assertEqual(online_count('{"Nikhil" :  "online", "Akshat" :  "online", "Eve": "online"}'), 3)
        self.assertEqual(online_count('{"Nikhil" :  "online", "Akshat" :  "offline", "Eve": "offline"}'), 1)
        self.assertNotEqual(online_count('{"Nikhil" :  "online", "Akshat" :  "offline", "Eve": "offline"}'), 3)

if __name__=='__main__':
    unittest.main(verbosity=2)
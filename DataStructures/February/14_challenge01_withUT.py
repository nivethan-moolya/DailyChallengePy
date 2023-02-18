"""
Date: Feb 14
Challenge: Randomness
The Trains Are Delayed Again, Due to unforseen circumstances in Suburbia, the trains will be delayed by a further 10 minutes.
From: https://edabit.com/challenge/WpRhk6tKJFmvJA6cq
"""
import unittest
from datetime import datetime
from datetime import timedelta

class Train:
    def __init__(self, destinations, expected_time):
        self.destinations = destinations
        self.expected_time = expected_time

def manage_delays(train, destination, delay_time):
    if destination in train.destinations:
        default_time = datetime.strptime(train.expected_time, "%H:%M")
        updated_time = default_time + timedelta(minutes=delay_time)
        train.expected_time = updated_time.strftime("%H:%M")
        
class TrainSetBack(unittest.TestCase):
    def testTrainSetBack(self):
        trains = [
            Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
            Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
            Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")
        ]
        for train in trains:
            manage_delays(train, "Lakeside Valley", 60)
        self.assertEqual(trains[0].expected_time, "13:04")
        self.assertEqual(trains[1].expected_time, "14:20")
        self.assertEqual(trains[2].expected_time, "14:22")
        for train in trains:
            manage_delays(train, "Farmsdale", 20)
        self.assertEqual(trains[0].expected_time, "13:04")
        self.assertEqual(trains[1].expected_time, "14:40")
        self.assertEqual(trains[2].expected_time, "14:22")
        for train in trains:
            manage_delays(train, "Townsville", 100)
        self.assertEqual(trains[0].expected_time, "14:44")
        self.assertEqual(trains[1].expected_time, "14:40")
        self.assertEqual(trains[2].expected_time, "16:02")
if __name__ == "__main__":
    unittest.main()

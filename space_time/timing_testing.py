import unittest
from unittest import TestCase
from datetime import datetime, timedelta

from timing import Present, Past, Future


now = datetime.now
nxt = timedelta(microseconds=2000000)


class Timing(TestCase):
    def test_present(self):
        self.assertTrue(Present(now()))
        self.assertFalse(Present(now()-nxt))
        self.assertFalse(Present(now()+nxt))

    def test_past(self):
        self.assertTrue(Past(now() - nxt))
        self.assertFalse(Past(now()))
        self.assertFalse(Past(now()+ nxt))

    def test_future(self):
        self.assertTrue(Future(now() + nxt))
        self.assertFalse(Future(now()-nxt))
        self.assertFalse(Future(now()))

unittest.main()

print(Present(now()-nxt))
print(Present(now()+nxt))
print(Present(now()))

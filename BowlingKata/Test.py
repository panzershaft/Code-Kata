import unittest

from BowlingKata.Bowling import Bowling


class Test(unittest.TestCase):
    def setUp(self):
        self.obj = Bowling()

    def testZeroes(self):
        self.obj.roller(0, 20)
        self.assertEqual(0, self.obj.get_score())

    def testOnes(self):
        self.obj.roller(1, 20)
        self.assertEqual(20, self.obj.get_score())

    def testSpare(self):
        self.obj.roller(4, 1)
        self.obj.roller(6, 1)
        self.obj.roller(2, 1)
        self.obj.roller(0, 17)
        self.assertEqual(14, self.obj.get_score())

    def testStrike(self):
        self.obj.roller(10, 1)
        self.obj.roller(3, 1)
        self.obj.roller(3, 1)
        self.obj.roller(0, 16)
        self.assertEqual(22, self.obj.get_score())


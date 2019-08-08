import unittest


class SumPosNeg(object):
    def __init__(self):
        self.items = []
        self.final = []

    def count(self, lst):
        self.items = lst
        pos_sum = 0
        neg_sum = 0

        if not self.items:
            return self.items

        for num in self.items:
            if num > 0:
                pos_sum += 1
            elif num < 0:
                neg_sum += num
        self.final.append(pos_sum)
        self.final.append(neg_sum)
        print(self.final)
        return self.final


class Test(unittest.TestCase):

    def setUp(self):
        self.obj = SumPosNeg()

    def test(self):
        self.assertEqual([10, -65], self.obj.count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

    def test2(self):
        self.assertEqual([8, -50], self.obj.count([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))

    def test3(self):
        self.assertEqual([1, 0], self.obj.count([1]))

    def test4(self):
        self.assertEqual([0, -1], self.obj.count([-1]))

    def test5(self):
        self.assertEqual([0, 0], self.obj.count([0, 0, 0, 0, 0, 0, 0, 0, 0]))

    def test6(self):
        self.assertEqual([], self.obj.count([]))


if __name__ == '__main__':
    unittest.main()

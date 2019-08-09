import unittest


class CountBinary(object):

    def __init__(self):
        self.binary = 0
        self.count = 0

    def get_value(self, num):
        self.binary = '{0:08b}'.format(num)
        print(self.binary)
        for bit in self.binary:
            if int(bit) > 0:
                self.count += 1
        return self.count


class Test(unittest.TestCase):

    def setUp(self):
        self.obj = CountBinary()

    def test1(self):
        self.assertEqual(0, self.obj.get_value(0))

    def test2(self):
        self.assertEqual(2, self.obj.get_value(3))

    def test3(self):
        self.assertEqual(3, self.obj.get_value(7))

    def test4(self):
        self.assertEqual(2, self.obj.get_value(10))


if __name__ == '__main__':
    unittest.main()

import unittest

from SqreDigit import square_digits


class Test(unittest.TestCase):

    def setUp(self):
        self.obj = square_digits()

    def test(self):
        self.obj.set_num(9119)
        self.assertEqual(9119, self.obj.get_num())
        self.assertEqual(811181, self.obj.get_score())



if __name__ == '__main__':
    unittest.main()

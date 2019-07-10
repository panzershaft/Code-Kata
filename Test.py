import unittest

from Descending import Descending


class Test(unittest.TestCase):

    def setUp(self):
        self.obj = Descending()

    def test_getlist(self):
        self.assertEqual(71, self.obj.get_value(17))


if __name__ == '__main__':
    unittest.main()

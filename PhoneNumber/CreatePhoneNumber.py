import unittest


class CreateNumber:

    def display_number(self, n):
        ext_num = str(''.join(str(i) for i in n[0:3]))
        mid_num = str(''.join(str(i) for i in n[3:6]))
        lst_num = str(''.join(str(i) for i in n[6:10]))
        return '({}) {}-{}'.format(ext_num, mid_num, lst_num)


class Test(unittest.TestCase):

    def setUp(self):
        self.obj = CreateNumber()

    def test1(self):
        self.assertEqual("(123) 456-7890",
                         self.obj.display_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    def test2(self):
        self.assertEqual("(111) 111-1111",
                         self.obj.display_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

    def test3(self):
        self.assertEqual("(123) 456-7890",
                         self.obj.display_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    def test4(self):
        self.assertEqual("(023) 056-0890",
                         self.obj.display_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))

    def test4(self):
        self.assertEqual("(000) 000-0000",
                         self.obj.display_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))


if __name__ == '__main__':
    unittest.main()

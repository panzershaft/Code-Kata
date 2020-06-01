import unittest

from ExclaimationMark.ExclamationMark import ExclamationMark


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = ExclamationMark()

    def testRight(self):
        self.obj.set_values('!!', '??')
        self.assertEqual("Right", self.obj.get_score())
        self.obj.set_values('!!!!', '???')
        self.assertEqual("Right", self.obj.get_score())

    def testLeft(self):
        self.obj.set_values('!??', '?!!')
        self.assertEqual("Left", self.obj.get_score())
        self.obj.set_values('!?!!', '?!?')
        self.assertEqual("Left", self.obj.get_score())

    def testBalance(self):
        self.obj.set_values("!!???!????", "??!!?!!!!!!!")
        self.assertEqual("Balance", self.obj.get_score())

    def testEmpty(self):
        self.obj.set_values(" ", " ")
        self.assertEqual("Balance", self.obj.get_score())


if __name__ == '__main__':
    unittest.main()

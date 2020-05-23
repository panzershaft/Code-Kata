import unittest

from CorrectSoftwareRecog.Correct import Correct


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Correct()

    def test0s(self):
        self.obj.set_value('0')
        self.assertEqual('O', self.obj.cleaned_value())

    def test0sComplex(self):
        self.obj.set_value('L0L')
        self.assertEqual('LOL', self.obj.cleaned_value())

    def test5s(self):
        self.obj.set_value('5')
        self.assertEqual('S', self.obj.cleaned_value())

    def test5Complex(self):
        self.obj.set_value('5O5')
        self.assertEqual('SOS', self.obj.cleaned_value())

    def test1S(self):
        self.obj.set_value('1')
        self.assertEqual('I', self.obj.cleaned_value())

    def test1Complex(self):
        self.obj.set_value('1 for an 1')
        self.assertEqual('I for an I', self.obj.cleaned_value())

    def testAll(self):
        self.obj.set_value('L0ND0N')
        self.assertEqual('LONDON', self.obj.cleaned_value())
        self.obj.set_value('DUBL1N')
        self.assertEqual('DUBLIN', self.obj.cleaned_value())
        self.obj.set_value('51NGAP0RE')
        self.assertEqual('SINGAPORE', self.obj.cleaned_value())
        self.obj.set_value('BUDAPE5T')
        self.assertEqual('BUDAPEST', self.obj.cleaned_value())
        self.obj.set_value('PAR15')
        self.assertEqual('PARIS', self.obj.cleaned_value())


if __name__ == '__main__':
    unittest.main()

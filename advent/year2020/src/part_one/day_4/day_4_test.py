import unittest

from day_4 import *


class PassPortValidityTest(unittest.TestCase):

    def testCheckByr(self):
        self.assertTrue(checkByr("2002"))
        self.assertFalse(checkByr("2003"))

    def testCheckIyr(self):
        pass

    def testCheckHgt(self):
        pass

    def testCheckHcl(self):
        self.assertTrue(checkHcl('#123abc'))
        self.assertFalse(checkHcl('123abc'))
        self.assertFalse(checkHcl('123azc'))
        self.assertFalse(checkHcl('dab227'))
        self.assertFalse(checkHcl('z'))

    def testCheckEcl(self):
        self.assertTrue(checkEcl('gry'))
        self.assertFalse(checkEcl('sonne'))
        self.assertFalse(checkEcl('gr'))

    def testCheckPid(self):
        self.assertTrue(checkPid('087499704'))
        self.assertFalse(checkPid('3556412378'))


if __name__ == "__main__":
    unittest.main()

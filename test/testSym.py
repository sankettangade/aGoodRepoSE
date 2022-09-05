import unittest
s = __file__
s = s[0:len(s)-16]
s = s+"/lua"
import sys
sys.path.insert(1, s)
import Sym

class TestSym(unittest.TestCase):

    def testSym(self):
        str = "aaaabbc"
        sym = Sym.Sym(0, "symbols")
        for i, x in enumerate(str):
            sym.add(x)
        mode = sym.mid()
        entropy = sym.div()
        entropy = (1000*entropy//1)/1000
        print(" Mode =", mode)
        print("Entropy =", entropy)
        self.assertEqual(mode, "a", "Should be a")
        self.assertTrue(1.38 >= entropy >= 1.37)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

s = __file__
s = s[0:len(s)-16]
s = s+"/lua"
import sys
sys.path.insert(1, s)
import Sym

class TestSym:

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
        if mode == "a" and 1.38 >= entropy >= 1.37:
            return 0
        else:
            return 1

if __name__ == '__main__':
        result = TestSym.testSym(1)
        print(result)

import unittest
s = __file__
s = s[0:len(s)-19]
s = s+"/lua"
import sys
sys.path.insert(1, s)
import Num
import The

class TestBigNum(unittest.TestCase):
    
    def test_big_num(self):
        num = Num.Num(0, "Numbers")
        The.The.cap = 32

        for i in range(0,1000):
            num.add(i)
        print(num.nums())
        print(len(num.nums()))
        assert len(num.nums())==32

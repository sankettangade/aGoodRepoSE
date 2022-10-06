import sys
sys.path.insert(1, "../lua")
import Num
import The

class TestBigNum():
    
   def testBigNum(self):
        num = Num.Num(0, "Numbers")
        The.cap = 32

        for i in range(0,1000):
            num.add(i)
        print(num.nums())
        print(len(num.nums()))
        if(len(num.nums()) == 32):
            return 0
        else:
            return 1


if __name__ == '__main__':
    result = TestBigNum.testBigNum(1)
    print(result)

    

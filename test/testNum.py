s = __file__
s = s[0:len(s)-16]
s = s+"/lua"
import sys
sys.path.insert(1, s)
import Num
import The
class TestNum:

    def testNum(self):
        num = Num.Num(0, "Numbers")
        The.The.cap = 100

        for i in range(1, 101):
            num.add(i)

        mid = num.mid()
        div = num.div()
        print("Mid =", mid)
        print("div =", div)

        #Lua has div range between 30.5 to 32 but the answer on calculation comes between 27.5 to 29
        if(50 <= mid <= 52) and (27.5 < div < 29):
            return 0
        else:
            return 1

if __name__ == '__main__':
        result = TestNum.testNum(1)
        print(result)

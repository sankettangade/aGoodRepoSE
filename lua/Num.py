import math
import random
import The

class Num:
    def __init__(self, c:int, s:str):
        self.n = 0
        self.at = c
        self.name = s
        self._has = []
        self.lo = -math.inf
        self.hi = math.inf
        self.isSorted = True


    def nums(self):
        if not self.isSorted:
            self._has = sorted(self._has)
            self.isSorted = True
        return self._has.copy()
    

    def add(self, v:int):
        if v != "?":
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = min(v, self.hi)

            if len(self._has) >= The.The.cap:
                if random.randint(0,100) < 7 :
                    pos = random.randint(0, len(self._has)-1)
                    self._has[pos] = v
            else:
                self._has.append(v)

            self.isSorted = False


    def div(self):
        has = self.nums()
        print(has)
        n = len(has)
        mean = sum(has) / n
        var = sum((x - mean) ** 2 for x in has) / n
        std = math.sqrt(var)
        return std


    def mid(self):
        has = self.nums()
        print(has)
        if len(has) % 2 != 0:
            pos = int((len(has)+1)/2 - 1)
            return has[pos]
        else:
            pos1 = int(len(has)/2 - 1)
            pos2 = int(len(has)/2)
            return (has[pos1]+has[pos2])/2


if __name__ == "__main__":
    n = Num(0, "Numbers")
    n.add(1)
    n.add(2)
    n.add(3)
    n.add(1)
    n.add(4)
    n.add(1)
    n.add(10)
    n.add(97)
    n.add(45)
    n.add(12)
    n.add(6)
    print(n._has)
    print(n.div())
    print(n.mid())
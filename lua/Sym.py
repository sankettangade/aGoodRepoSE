import math

class Sym:
    # constructor for Sym class
    def __init__(self, c, s):
        self.at = c     # index of the column
        self.name = s   # name of the column
        self.n = 0      # number of items seen
        self._has = {}  # data in the column

    
    # method to add a new item in the column
    def add(self, v:str):
        if v != '?':
            self.n += 1
            if v in self._has:
                self._has[v] += 1
            else:
                self._has[v] = 1


    # method to calculate mode of the column, mode is the item which occurs the most
    def mid(self) -> str:
        most = -1
        mode = ""
        for key, val in self._has.items():
            if val > most :
                most = val
                mode = key
        return mode


    # method to calculate entropy of the column
    def div(self) -> float:
        e = 0
        for key, val in self._has.items():
            p = val/self.n
            e = e - p*math.log(p,2)
        return e


# basic testing to check the working of the class
if __name__ == "__main__":
    s = Sym(0, "symbols")
    s.add("1")
    s.add("1")
    s.add("1")
    s.add("2")
    s.add("2")
    s.add("3")
    s.add("3")
    s.add("3")
    s.add("3")
    s.add("3")
    print(s.mid())
    print(s.div())
    print(s._has)


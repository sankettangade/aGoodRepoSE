from re import split
import Cols
import Utils
import Num
import Sym
import The

class Data:
    def __init__(self,src) -> None:
        self.cols = None
        self.rows = []
        if type(src) == str:
            Utils.csv(src,self)
            self.add_to_columns()

    def add(self,xs):
        if not self.cols:
            self.cols = Cols.Cols(xs)
            temp = self.cols.x | self.cols.y 
            l = []
            self.rows.append(l)
            for i in range(len(xs)):
                if i in temp.values():
                    l.append(xs[i])
        else:
            l = []
            temp = self.cols.x | self.cols.y 
            for i in range(len(xs)):
                if i in self.cols.x.values():
                    if xs[i] != "?":
                        l.append(float(xs[i]))
                    else:
                        l.append(xs[i])
                elif i in self.cols.y.values():
                    l.append(xs[i])
            self.rows.append(l)
            
            
        
    # def add_to_columns(self):
    #     for col_name, col_index in self.cols.y.items():
    #         s = Sym.Sym(col_name, col_index)
    #         col_index = self.rows[0].index(col_name)
    #         for i in range(1,len(self.rows)-1):
    #             s.add(self.rows[i][col_index])
    #         The.column_objects[col_name] = s
    #
    #     for col_name, col_index in self.cols.x.items():
    #         s = Num.Num(col_name, col_index)
    #         col_index = self.rows[0].index(col_name)
    #         for i in range(1,len(self.rows)-1):
    #             # print((self.rows[i]))
    #             s.add(self.rows[i][col_index])
    #         The.column_objects[col_name] = s

    def print(self):
        print(self.rows)

    def stats(self, showCols,fun = "mid" ):
        temp = {}
        showCols = self.cols.x if showCols == None else self.cols.y
        for col in showCols:
            obj = The.column_objects[col]
            if fun == "mid":
                temp[col] = obj.mid()
            elif fun == "div":
                temp[col] = obj.div()

        return temp



a = Data("../data/lua_sample_data.csv")

print(a.stats(None, "div"))

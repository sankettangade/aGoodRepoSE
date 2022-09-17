import Cols
import Utils


class Data:
    def __init__(self, src = None) -> None:
        self.cols = None
        self.rows = []
        self.mapping = {}
        if type(src) == str:
            Utils.csv(src, self)

    def add(self, xs):
        if not self.cols:
            self.cols = Cols.Cols(xs)
            temp = {**self.cols.x,**self.cols.y}
            l = []
            indices = list(temp.values())
            for i in range(0,len(indices)):
                indices[i] = indices[i][0]
            indices.sort()
            self.rows.append(l)
            count = 0
            for i in indices:
                l.append(xs[i])
                self.mapping[i] = count
                count+=1

        else:
            l = []
            indices_x, indices_y = list(self.cols.x.values()), list(self.cols.y.values())
        
            for i in range(0,len(indices_x)):
                col_obj = indices_x[i][1]
                indices_x[i] = indices_x[i][0]
            for i in range(0,len(indices_y)):
                indices_y[i] = indices_y[i][0]

            for i in range(len(xs)):
                if i in indices_x:
                    if xs[i] != "?":
                        l.append(float(xs[i]))
                        self.cols.x[self.rows[0][self.mapping[i]]][1].add(float(xs[i]))
                    else:
                        l.append(xs[i])
                        self.cols.x[self.rows[0][self.mapping[i]]][1].add(xs[i])
                elif i in indices_y:
                    l.append(float(xs[i]))                    
                    self.cols.y[self.rows[0][self.mapping[i]]][1].add(float(xs[i]))
            self.rows.append(l)

    def print(self):
        print(self.rows)

    def stats(self, showCols, fun="mid"):
        temp = {}
        showCols = self.cols.x if showCols == None else self.cols.y
        for col in showCols:
            if fun == "mid":
                temp[col] = showCols[col][1].mid()
            elif fun == "div":
                temp[col] = showCols[col][1].div()

        return temp


a = Data("../data/lua_sample_data.csv")
# print(a.rows)
print(a.stats(None, "div"))

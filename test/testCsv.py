import sys
sys.path.insert(1, "../lua")
import Utils
import Data


class TestReadCsv:

    def testCsv(self):
        d = Data.Data()
        Utils.csv("../data/lua_sample_data.csv", d)
        for i in range(0, 11):
                print("Row No.",i," = ", d.rows[i])

    def testData(self):
        data = Data.Data("../data/lua_sample_data.csv")
        for i, x in enumerate(data.rows):
            print(i, "Value = ", x)

    def testColumn(self):
        data1 = Data.Data("../data/lua_sample_data.csv")

        print("xmid = ", data1.stats(data1.cols.x, "mid"))
        print("ymid = ", data1.stats(data1.cols.y, "mid"))
        print("xdiv = ", data1.stats(data1.cols.x, "div"))
        print("ydiv = ", data1.stats(data1.cols.y, "div"))


if __name__ == '__main__':
    TestReadCsv.testCsv(1)
    TestReadCsv.testData(1)
    TestReadCsv.testColumn(1)


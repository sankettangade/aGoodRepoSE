import Cli
import runpy
from test import testNum,test,testSym,testCsv,testBigNum
import The


cli = Cli.Cli()
the = cli.initialize_the()
the = cli.update_the(the)

The.The = the

if the["eg"] == "nums":
    testnum = testNum.TestNum()
    testnum.testNum()
elif the["eg"] == "sym":
    testsym = testSym.TestSym()
    testsym.testSym()
elif the["eg"] == "bignum":
    testbignum = testBigNum.TestBigNum()
    testbignum.testBigNum()
elif the["eg"] == "csv":
    testcsv = testCsv.TestReadCsv()
    testcsv.testCsv()
elif the["eg"] == "all":
    testnum = testNum.TestNum()
    testnum.testNum()
    testsym = testSym.TestSym()
    testsym.testSym()
    testbignum = testBigNum.TestBigNum()
    testbignum.testBigNum()
    testcsv = testCsv.TestReadCsv()
    testcsv.testCsv()




import re
import sys
from Utils import coerce

class Cli:
    The = {}
    def __init__(self) -> None:
        self.The = {}
        Cli.The = self.The
        self.help = """CSV : summarized csv file
        (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
        USAGE: lua seen.lua [OPTIONS]
        OPTIONS:
        -e  --eg        start-up example                      = nothing
        -d  --dump      on test failure, exit with stack dump = false
        -f  --file      file with csv data                    = csv.csv
        -h  --help      show help                             = false
        -n  --nums      number of nums to keep                = 512
        -s  --seed      random number seed                    = 10019
        -S  --seperator field seperator                       = ,"""

    def initialize_the(self):
        help = self.help
        reexp = r"[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
        dictre = re.findall(reexp, help)
        for key, value in dictre:
            self.The[key] = coerce(value)
        return self.The
    

    def update_the(self, the):
        slots = the.keys()
        args = sys.argv
        args = args[1:]
        for slot in slots:
            v = str(the[slot])
            for n,x in enumerate(args):
                if x == '-' + slot[0] or x == '--' + slot:
                    v = v == 'False' and 'True' or v == 'True' and 'False' or args[n+1]
            the[slot] = coerce(v)

        if the['help'] == True:
            print(self.help)
            exit()

        return the


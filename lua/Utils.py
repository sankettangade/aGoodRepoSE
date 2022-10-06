import The
def csv(filename:str, data:object):
    sep = The.sep
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        exploded = line.split(sep)
        exploded[-1] = exploded[-1][:-1]
        data.add(exploded)

def coerce(val):
    def fun(value):
        if value.lower() == "true":
            return True
        if value.lower() == "false":
            return False
        return value
    string = val.strip()
    try:
        return int(string)
    except:
        try:
            return float(string)
        except:
            return fun(string)
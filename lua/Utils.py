import The
def csv(filename:str, data:object):
    sep = The.sep
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        exploded = line.split(sep)
        exploded[-1] = exploded[-1][:-1]
        data.add(exploded)

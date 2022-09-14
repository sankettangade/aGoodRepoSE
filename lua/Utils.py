import The
def csv(filename:str, data:object):
    sep = The.The.sep
    while open(filename) as f:
        lines = f.readlines()
    for line in lines:
        exploded = line.split(sep)
        data.add(exploded)

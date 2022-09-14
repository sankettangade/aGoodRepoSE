import copy


class Row:
    def __init__(self, t):
        self.cells = t
        cooked = copy.deepcopy(t)
        isEvaled = False
    

class State():

    def __init__(self, puzzle , depth):
        self.puzzle = puzzle
        self.depth = depth
        self.parent_state = None
        self.distance = 0
        self.cost = 0

    def __lt__(self, other):
        return self.cost < other.cost

    def get_zero_position(self):
        i = -1
        j = -1
        for list in self.puzzle:
            i = i + 1
            j = -1
            for element in list:
                j = j + 1
                if(element == 0):
                    return [i,j]

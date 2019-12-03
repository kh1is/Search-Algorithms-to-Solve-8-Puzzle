class heuristic():

    def __init__(self, state , goal_list):
        self.state = state
        self.puzzle = self.state.puzzle
        self.goal_list = goal_list
        self.manhattan_distance = 0
        self.euclidian_distance = 0

    def calculate_manhattan_distance(self):
        for i in range(0,3):
            for j in range(0,3):
                [row , col] = self.get_element_position(self.puzzle[i][j])
                self.manhattan_distance = self.manhattan_distance + abs(i - row) + abs(j - col)


    def calculate_euclidian_distance(self):
        for i in range(0, 3):
            for j in range(0, 3):
                [row, col] = self.get_element_position(self.puzzle[i][j])
                self.euclidian_distance = self.euclidian_distance + ((i - row)**2 + (j - col)**2)**(1/2)

    def get_element_position(self , num):
        i = -1
        j = -1
        for list in self.goal_list:
            i = i + 1
            j = -1
            for element in list:
                j = j + 1
                if (element == num):
                    return [i, j]
from movment import Movment
from timeit import default_timer as timer

class depth_first_search():

    def __init__(self, initial_state , goal_list):
        self.initial_state = initial_state
        self.goal_list = goal_list
        self.final_state = None
        self.set = []
        self.stack = []
        self.stack_set = []
        self.path_to_goal = []
        self.cost = 0
        self.expanded_nodes = []
        self.max_depth = 0

    def get_dfs_report(self):
        start = timer()
        self.run_dfs()
        end = timer()

        self.get_path_to_goal()
        print("*************************************")
        print("Cost = ", self.cost)
        print("*************************************")
        self.get_nodes_expanded()
        print("*************************************")
        print("Max depth = ", self.max_depth)
        print("*************************************")
        print("Running time = " ,end - start)
        print("*************************************")

    def run_dfs(self):
        self.stack.append(self.initial_state)
        #self.stack_set.append(self.initial_state.puzzle)

        while(len(self.stack) != 0):
            current_state = self.stack.pop()
            #self.stack_set.pop()
            self.set.append(current_state.puzzle)

            if(self.is_final_state(current_state)):
                self.final_state = current_state
                return True
            else:
                movement = Movment(current_state)

                self.expanded_nodes.append(current_state)

                movement.right_movment()
                movement.left_movment()
                movement.up_movment()
                movement.down_movment()

                childs = [movement.right_state , movement.left_state , movement.up_state , movement.down_state]

                for child in childs:
                    if (child != None):
                        if (child.puzzle not in self.set):
                            if (child not in self.stack):
                                self.stack.append(child)
                                #self.stack_set.append(child.puzzle)
                        if (self.max_depth < child.depth):
                            self.max_depth = child.depth

        return False

    def is_final_state(self , state):
        if(state.puzzle == self.goal_list):
            return True
        return False

    def get_path_to_goal(self):
        print("Path to goal:")

        current_state = self.final_state

        while (current_state.puzzle != self.initial_state.puzzle):
            self.path_to_goal.append(current_state)
            current_state = current_state.parent_state
            self.cost = self.cost + 1

        self.path_to_goal.append(self.initial_state)

        while(len(self.path_to_goal) > 0):
            self.print_method(self.path_to_goal.pop().puzzle)
            print("-------------------------")

    def get_nodes_expanded(self):
        print("Nodes expanded:")
        for element in self.expanded_nodes:
            self.print_method(element.puzzle)
            print("-------------------------")

    def print_method(self , matrix):
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))
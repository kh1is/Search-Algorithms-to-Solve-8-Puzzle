from movment import Movment
from timeit import default_timer as timer
import copy

class bfs:

    def __init__(self, initial_state, goal_puzzle):
        self.initial_state = initial_state
        self.goal_puzzle = goal_puzzle
        self.final_state = None
        self.path_to_goal = []
        self.cost = 0
        self.expanded_nodes = []
        self.max_depth = 0

    def get_bfs_report(self):
        start = timer()
        self.search()
        end = timer()

        self.get_path_to_goal()
        print("*************************************")
        print("Cost = ", self.cost)
        print("*************************************")
        self.get_nodes_expanded()
        print("*************************************")
        print("Max depth = ", self.max_depth)
        print("*************************************")
        print("Running time = ", end - start)
        print("*************************************")

    def is_final_state(self,state):

        if(state.puzzle == self.goal_puzzle):
            return True
        return False

    def search(self):
        queue = []
        queue.append(self.initial_state)
        queue_set = [self.initial_state.puzzle]
        set = []


        while(len(queue) != 0):
            state = queue.pop(0)
            queue_set.pop(0)
            set.append(state.puzzle)

            if (self.is_final_state(state)):
                self.final_state = state
                self.max_depth = state.depth
                return True

            movement = Movment(state)

            self.expanded_nodes.append(state)

            movement.right_movment()
            movement.left_movment()
            movement.up_movment()
            movement.down_movment()

            if(movement.right_state != None):

                if(self.check_redundant_state(queue_set,set,movement.right_state) == False):
                    queue.append(movement.right_state)
                    queue_set.append(movement.right_state.puzzle)

            if (movement.left_state != None):

                if (self.check_redundant_state(queue_set, set, movement.left_state) == False):
                    queue.append(movement.left_state)
                    queue_set.append(movement.left_state.puzzle)

            if (movement.up_state != None):

                if (self.check_redundant_state(queue_set, set, movement.up_state) == False):
                    queue.append(movement.up_state)
                    queue_set.append(movement.up_state.puzzle)

            if (movement.down_state != None):

                if (self.check_redundant_state(queue_set, set, movement.down_state) == False):
                    queue.append(movement.down_state)
                    queue_set.append(movement.down_state.puzzle)

        return False


    def check_redundant_state(self,queue_set,set,state):

        if(state.puzzle not in queue_set):
            if(state.puzzle not in set):
                return False

        return True

    def get_path_to_goal(self):
        print("Path to goal:")

        current_state = self.final_state

        while (current_state.puzzle != self.initial_state.puzzle):
            self.path_to_goal.append(current_state)
            current_state = current_state.parent_state
            self.cost = self.cost + 1

        self.path_to_goal.append(self.initial_state)

        while (len(self.path_to_goal) > 0):
            self.print_method(self.path_to_goal.pop().puzzle)
            print("-------------------------")

    def get_nodes_expanded(self):
        print("Nodes expanded:")
        for element in self.expanded_nodes:
            self.print_method(element.puzzle)
            print("-------------------------")

    def print_method(self, matrix):
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))
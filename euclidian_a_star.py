from heuristic import heuristic
from movment import Movment
import heapq
from timeit import default_timer as timer

class Euclidian_A_Start():

    def __init__(self, initial_state , goal_list):
        self.initial_state = initial_state
        self.goal_list = goal_list
        self.final_state = None
        self.set = []
        self.heap = []
        self.path_to_goal = []
        self.cost = 0
        self.expanded_nodes = []
        self.max_depth = 0

    def get_euclidian_a_star_report(self):
        start = timer()
        self.run_euclidian_a_star()
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

    def calculate_state_heuristic(self , state):
        h = heuristic(state, self.goal_list)
        h.calculate_euclidian_distance()

        state.distance = h.euclidian_distance

        state.cost = state.distance + state.depth

    def run_euclidian_a_star(self):

        self.calculate_state_heuristic(self.initial_state)

        heapq.heappush(self.heap, (self.initial_state.cost, self.initial_state))

        while (len(self.heap) != 0):
            (key, current_state) = heapq.heappop(self.heap)

            self.set.append(current_state.puzzle)

            if (self.is_final_state(current_state)):
                self.final_state = current_state
                return True
            else:
                movement = Movment(current_state)

                self.expanded_nodes.append(current_state)

                movement.right_movment()
                movement.left_movment()
                movement.up_movment()
                movement.down_movment()

                childs = [movement.right_state, movement.left_state, movement.up_state, movement.down_state]

                for child in childs:
                    if (child != None):
                        if (child.puzzle not in self.set):
                            self.calculate_state_heuristic(child)
                            if (self.check_if_not_exits(child)):
                                heapq.heappush(self.heap, (child.cost, child))
                            else:
                                heapq.heapify(self.heap)
                        if (self.max_depth < child.depth):
                            self.max_depth = child.depth
        return False

    def check_if_not_exits(self , current_state):
        for i in range(0 , len(self.heap)):
            (key , state) = self.heap[i]
            if(state.puzzle == current_state.puzzle):
                if(current_state.cost < state.cost):
                    state.cost = current_state.cost
                    self.heap[i] = (state.cost , state)
                return False

        return True

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


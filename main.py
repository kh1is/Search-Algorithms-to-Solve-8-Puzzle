from state import State
from depth_first_search import depth_first_search
from bfs import bfs
from manhattan_a_start import Manhattan_A_Start
from euclidian_a_star import Euclidian_A_Start
import numpy as np

def getInitailPuzzle():
    print("Please enter start puzzle:")
    arr = list(map(int, input().split()))
    reshapedNumPyArray = np.array(arr).reshape(3, 3)
    return reshapedNumPyArray.tolist()

#initialStartList = getInitailPuzzle()
initial_start_list = [[1,2,5],
                      [3,4,6],
                      [0,7,8]]
goal_list= [[0,1,2],
            [3,4,5],
            [6,7,8]]

start_state = State(initial_start_list , 0)

dfs = depth_first_search(start_state , goal_list)
dfs.get_dfs_report()

bfs = bfs(start_state , goal_list)
#bfs.get_bfs_report()

manhattan_a_star = Manhattan_A_Start(start_state , goal_list)
#manhattan_a_star.get_manhattan_a_star_report()

euclidian_a_star = Euclidian_A_Start(start_state , goal_list)
#euclidian_a_star.get_euclidian_a_star_report()
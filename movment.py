from state import State
import copy

class Movment():

  def __init__(self,parent_state):
    self.parent_state = parent_state
    self.right_state = None
    self.left_state = None
    self.up_state = None
    self.down_state = None

# Check if move is aval
# Create new puzzle
# Create new state
# Set the state

  def right_movment(self):
    puzzle = copy.deepcopy(self.parent_state.puzzle)
    [row,col] = self.parent_state.get_zero_position()

    if(col < 2):
      puzzle[row][col] = puzzle[row][col+1]
      puzzle[row][col+1] = 0

      right_state = State(puzzle, self.parent_state.depth+1)
      right_state.parent_state = self.parent_state
      self.right_state = right_state

  def left_movment(self):
    puzzle = copy.deepcopy(self.parent_state.puzzle)
    [row, column] = self.parent_state.get_zero_position()
    if (column > 0):
      tmp = puzzle[row][column - 1]
      puzzle[row][column - 1] = 0
      puzzle[row][column] = tmp
      child_state = State(puzzle, (self.parent_state.depth + 1))
      child_state.parent_state = self.parent_state
      self.left_state = child_state

  def up_movment(self):
    puzzle = copy.deepcopy(self.parent_state.puzzle)
    [row,col] = self.parent_state.get_zero_position()

    if (row > 0):
      puzzle[row][col] = puzzle[row-1][col]
      puzzle[row-1][col] = 0

      up_state = State(puzzle, self.parent_state.depth+1)
      up_state.parent_state = self.parent_state
      self.up_state = up_state

  def down_movment(self):
    puzzle = copy.deepcopy(self.parent_state.puzzle)
    [row, column] = self.parent_state.get_zero_position()
    if (row < 2):
      tmp = puzzle[row + 1][column]
      puzzle[row + 1][column] = 0
      puzzle[row][column] = tmp
      child_state = State(puzzle, (self.parent_state.depth + 1))
      child_state.parent_state = self.parent_state
      self.down_state = child_state
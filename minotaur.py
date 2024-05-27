import random
from maze import Maze

class Minotaur:
    def __init__(self):
        self._maze = Maze()
        self._row, self._col = self._random_start_position()
        self._maze[self._row][self._col] = 'M'

    def _random_start_position(self):
        empty_spaces = []
        for row_idx, row in enumerate(self._maze):
            for col_idx, char in enumerate(row):
                if char == ' ':
                    empty_spaces.append((row_idx, col_idx))
        return random.choice(empty_spaces)

    def move_minotaur(self):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
        random.shuffle(directions)
        
        for dir_row, dir_col in directions:
            new_row, new_col = self._row + dir_row, self._col + dir_col
            if self._maze[new_row][new_col] != '*':
                old_row, old_col = self._row, self._col
                self._maze[old_row][old_col] = ' '
                self._row, self._col = new_row, new_col
                self._maze[self._row][self._col] = 'M'
                return self._maze[old_row][old_col]

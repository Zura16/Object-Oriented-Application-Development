from maze import Maze

class Hero:
    def __init__(self):
        self._maze = Maze()
        start_pos = self._maze.search_maze('s')
        self._row, self._col = start_pos
        self._maze[start_pos[0]][start_pos[1]] = 'H'

    def go_up(self):
        return self._move(self._row - 1, self._col)

    def go_down(self):
        return self._move(self._row + 1, self._col)

    def go_left(self):
        return self._move(self._row, self._col - 1)

    def go_right(self):
        return self._move(self._row, self._col + 1)

    def _move(self, new_row, new_col):
        char_at_new_pos = self._maze[new_row][new_col]
        if char_at_new_pos == '*':  
            return '*'
        elif char_at_new_pos == ' ' or char_at_new_pos == 'f':  
            self._maze[self._row][self._col] = ' '
            self._row, self._col = new_row, new_col
            self._maze[self._row][self._col] = 'H'
            return char_at_new_pos
        elif char_at_new_pos == 'M':  
            return 'M'


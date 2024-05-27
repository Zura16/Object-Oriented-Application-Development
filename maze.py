
class Maze:
  _instance = None
  _initialized = False

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    if not Maze._initialized:
      file = open("minomaze.txt")
      
      maze2d = []
      for row in file:
        list = []
        for item in row:
          if item != '\n':
            list.append(item)
        maze2d.append(list)
        
      self._maze = maze2d
      
      file.close()
      Maze._initialized = True
      
  def __getitem__(self, row):
    #Confused?
    return self._maze[row]

  def __len__(self):
    #fix?
    num_rows = len(self._maze)
    
    return num_rows


  def __str__(self):
    labyrinth = ""
    
    for row in self._maze:
      for item in row:
        labyrinth+= item + ' '
      labyrinth+= '\n'
      
    return labyrinth
    #return str(" "+ " ".join(self._maze))


  def search_maze(self, ch):
    loc = [-1, -1]
    
    for i in range(len(self._maze)):
      for j in range(len(self._maze[i])):
        if self._maze[i][j] == ch:
          loc = [i, j]

    #reverse() so it appears as [x, y]
    #loc.reverse()
    return loc
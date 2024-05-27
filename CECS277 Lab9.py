import maze
import hero2
import minotaur


def main():
  m = maze.Maze()
  player = hero2.Hero()
  mino = minotaur.Minotaur()
  
  #play = True
  spot_info = ''
  mino_spot_info = ''
  
  #print(m)

  #print(m.search_maze("H"))
  #print(m.search_maze("s"))
  #print(m.search_maze("f"))
  
  while True:
    print(m)
    
    while True:
      move = input("Choose a direction (WASD):")
      move = move.upper()
  
  
      #Movement check
      if move == "W":
        spot_info = player.go_up()
        break
        
      elif move == "A":
        spot_info = player.go_left()
        break
        
      elif move == "S":
        spot_info = player.go_down()
        break
        
      elif move == "D":
        spot_info = player.go_right()
        break
  

    #Check if ran into anything
    if spot_info == '*':
      print("You ran into a wall!")
      
    elif spot_info == 'M':
      cap_spot = m.search_maze('H')
      m[cap_spot[0]][cap_spot[1]] = 'M'
      break
      
    elif spot_info == 'f':
      break
    
    
    #Minotaur's turn
    
    if spot_info != 'M':
      mino_spot_info = mino.move_minotaur()

      if mino_spot_info == 'H':
        break

  
  print(m)
  if spot_info == 'M' or mino_spot_info == 'H':
    print("The Minotaur captured you. . .\nGame over!")
    
  else:
    print("You found the exit!")

  
main()
from debug import debug

#A class representing a snek, its current position, and direction
class Snek:
  def __init__(self, x, y, direction, name, prog_name):
    #pos on board (of the head)
    self.x = x
    self.y = y
    #direction the snek is headering in
    #0=left, 1=up, 2=right, 3=down
    self.direction = direction
    #the name of the snek, probabbly YELLOW_SNEK
    self.name = name
    #the name of the snek in /progress, probably YELLOW
    self.prog_name = prog_name

  #move the snek based on a turn (-1=left, 0=forwards, 1=right)
  def move(self, turn):
    #adjust direction
    self.direction += turn
    #normalize direction
    if self.direction > 3:
      self.direction -= 4
    elif self.direction < 0:
      self.direction += 4

    #move snek based on current direction
    #move left
    if self.direction == 0:
      self.x -= 1
    #move up
    elif self.direction == 1:
      self.y -= 1
    #move right
    elif self.direction == 2:
      self.x += 1
    #move down
    elif self.direction == 3:
      self.y += 1

  #get the new pos where a move would place the snek
  def move_pos(self, turn):
    #adjust direction
    direct = self.direction + turn
    #normalize direction
    if direct > 3:
      direct -= 4
    elif direct < 0:
      direct += 4

    x = self.x
    y = self.y
    #move snek based on current direction
    #move left
    if direct == 0:
      x -= 1
    #move up
    elif direct == 1:
      y -= 1
    #move right
    elif direct == 2:
      x += 1
    #move down
    elif direct == 3:
      y += 1

    return x, y, direct

# a class representing an enemy snek - for tracking their heads
class EnemySnek:
  #init with their x and y pos
  def __init__(self, x, y, name, prog_name):
    self.x = x
    self.y = y
    #mark pos's that they occupy
    self.pos = [[x, y]]
    #the name (with _SNEK - RED_SNEK, for example)
    self.name = name
    #name in /progress
    self.prog_name = prog_name
    #if the snek is alive
    self.is_alive = True

  #kill the snek
  def kill(self):
    self.is_alive = False

  #from a board, update their head's position
  #do this by seeing which squares are occupied now that weren't before
  def update_head(self, board):
    #new array of pos
    new_pos = []
    for x in range(35):
      for y in range(35):
        #this square contains the snek
        if board[y][x] == self.name:
          #add to the new pos
          new_pos.append([x, y])
          #check if this is a newly occupied square
          if not [x,y] in self.pos:
            self.x = x
            self.y = y
    self.pos = new_pos
    return
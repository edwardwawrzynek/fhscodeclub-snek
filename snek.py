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

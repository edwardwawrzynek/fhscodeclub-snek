from base_ai import BaseAI
from debug import debug

class SmartAI(BaseAI):
  def make_move(self):
    #get apple
    apple_x, apple_y = self.find_apple()
    #if there is no apple, move to the middle
    if apple_x == -1 or apple_y == -1:
      apple_x = 17
      apple_y = 17

    #Print out target
    debug("SmartAI: Target Position: " + str(apple_x) + ", " + str(apple_y))

    #Get all the possible moves we could make
    moves = self.get_potential_moves()
    minDist = 1000
    moveIndex = 0
    i = 0
    for m in moves:
      dist = self.dist_to(m[0], m[1], apple_x, apple_y)
      if dist < minDist and self.is_empty(m[0], m[1]):
        minDist = dist
        moveIndex = i
      i+=1
    return moveIndex-1

    return 0
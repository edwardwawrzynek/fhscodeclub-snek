from base_ai import BaseAI

class SmartAI(BaseAI):
  def make_move(self):
    #get apple
    apple_x, apple_y = self.find_apple()
    #if there is an apple, move to it
    if True:#apple_x != -1 and apple_y != -1:
      print("SmartAI: Apple target: " + str(apple_x) + ", " + str(apple_y))
      #out of the possible moves, choose the one closest to the apple
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
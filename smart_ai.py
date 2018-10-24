from base_ai import BaseAI
from debug import debug

class SmartAI(BaseAI):
  def make_move(self):
    #get apple
    apple_x, apple_y = self.find_apple()
    #if there is no apple, move to the middle as the target instead
    if apple_x == -1 or apple_y == -1:
      apple_x = 17
      apple_y = 17

    move = self.choose_best_square(True, apple_x, apple_y)
    #if we couldn't find a perfectly safe move, pick a probably safe one
    if move < -1:
      move = self.choose_best_square(False, apple_x, apple_y)

    return move
  '''
  def choose_best_square(self, check_enemies, apple_x, apple_y):
    #Get all the possible moves we could make
    moves = self.get_potential_moves()

    minDist = 1000
    moveIndex = -1
    i = 0
    for m in moves:
      dist = self.dist_to(m[0], m[1], apple_x, apple_y)
      #make sure that the square is the closest to the apple and is empty
      if dist < minDist and self.is_empty(m[0], m[1]):
        #also make sure that the square isn't a square that an enemy head could move into next turn
        isNearEnemy = False
        for e in self.enemy_sneks:
          if self.dist_to(m[0], m[1], e.x, e.y) < 1.01:
            isNearEnemy = True

        if (not isNearEnemy) or (not check_enemies):
          minDist = dist
          moveIndex = i
      i+=1

    return moveIndex - 1
  '''
  def choose_best_square(self, check_enemies, apple_x, apple_y):
    #Get all the possible moves we could make
    moves = self.get_potential_moves()
    #all the moves - not filtered
    all_moves = self.get_potential_moves()

    #remove non empty squares
    moves = list (filter(lambda move: self.is_empty(move[0], move[1]), moves))

    #if asked for, filter aout squares within two squares of an enemy head

    #find the min distance to the apple
    minDist = 1000
    for m in moves:
      dist = self.dist_to(m[0], m[1], apple_x, apple_y)
      if dist < minDist:
        minDist = dist

    #filter out elements less than that distance
    moves = list (filter(lambda move: (self.dist_to(move[0], move[1], apple_x, apple_y) <= minDist), moves))

    return all_moves.index(moves[0])-1

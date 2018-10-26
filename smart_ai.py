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

    move = self.choose_best_square(apple_x, apple_y)
    return move

  def choose_best_square(self, apple_x, apple_y):
     #Get all the possible moves we could make
    moves = self.get_potential_moves()
    #the scores for each square - higher is better
    scores = []
    #calculate scores
    for m in moves:
      #start at 0
      scores.append(0)

      #if the square isn't empty, rank it low
      if not self.is_empty(m[0], m[1]):
        scores[-1] -= 1000

      #if the square is within range of an enemy's head, rank it lower
      for e in self.enemy_sneks:
        if self.dist_to(m[0], m[1], e.x, e.y) < 1.01:
          scores[-1] -= 100

      #subtract distance to apple
      scores[-1] -= self.dist_to(m[0], m[1], apple_x, apple_y)

    #choose the square with the highest score (-1 is because turn options start with -1)
    return scores.index(max(scores))-1
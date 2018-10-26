from base_ai import BaseAI
from debug import debug
import random

#Control Wights

#How much to try to avoid being near other snakes
#Setting this high may cause the snek to not take risks to go for food

# 0=don't care how close to other sneks
# ~0.2=try to avoid, but still take a decent amount of risks for food
# ~1=try to avoid, but still take some amount of risks for food
# ~5=fairly safe avoidance
# ~50=pretty much always avoid
SNEK_AVOIDANCE = 2

#the width of the area to search for sneks to avoid (5 good for fair avoidance)
SNEK_AVOIDANCE_WIDTH = 5

#How much to avoid moving into a square that another snek could also move to in the same tunr
#SNEK_AVOIDANCE is more preemptive, this doesn't look ahead
#probably should be at least 100, unless we are okay taking high chances of dying

EAT_RISK_AVOIDANCE = 50

#How much random-ness to induce
RANDOM_PARAM = 0.4

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

      #if a square is on the board, give it a boost (to avoid crashing into walls - an quare with something in it *may* be an enemy's tail)
      if self.on_board(m[0], m[1]):
        scores[-1] += 200

      #if the square is within range of an enemy's head, rank it lower
      for e in self.enemy_sneks:
        if self.dist_to(m[0], m[1], e.x, e.y) < 1.01:
          scores[-1] -= EAT_RISK_AVOIDANCE

      #adjust for how many sneks are in the proximity of a move - sum number of snek squares in 5x5 area, and multiply by SNEK_AVOIDANCE
      scores[-1] -= self.sneks_in_area(m[0], m[1]) * SNEK_AVOIDANCE

      #subtract distance to apple
      scores[-1] -= self.dist_to(m[0], m[1], apple_x, apple_y)

      #add slight random element - doesn't really do anything, except when traveling to a square (randomizes order of turns)
      scores[-1] += random.random()*RANDOM_PARAM

    #choose the square with the highest score (-1 is because turn options start with -1)
    return scores.index(max(scores))-1

  def sneks_in_area(self, x, y):
    total = 0
    board = self.get_board()
    width = int(SNEK_AVOIDANCE_WIDTH/2)
    for x_coord in range(x-width, x+width+1):
      for y_coord in range(y-width, y+width+1):
        #make sure it is on the board - don't count cells outside board as containing enemies
        if self.on_board(x_coord, y_coord):
          if board[y_coord][x_coord] != "EMPTY" and board[y_coord][x_coord] != "APPLE" and board[y_coord][x_coord] != self.snek.name:
            total += 1
    return total

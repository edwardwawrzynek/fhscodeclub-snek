from snek import Snek
from api import API

#a base class for other ai's

class BaseAI:
  #don't override constructor
  def __init__(self, snek, api):
    #the api object - don't use this directly
    self._api = api

    #--- these attributes can be accessed by AI's ---
    #the snek object
    self.snek = snek
    #the board
    self.board = self._api.board

  #main ai function - based on the board, decide on a move, and return it
  #the move returned is either a -1, 0, or 1, for left, forwards, or right
  #new AI's should override this
  def make_move(self):
    #place overriden ai here

    #always go forwards
    return 0

  #check whether a spot on the board is empty (or contains an apple) or not
  def is_empty(self, x, y):
    return self.board[y][x] == "EMPTY" or self.board[y][x] == "APPLE"

  #get the position of the apple on the board - return it as an (x,y) tuple,
  #or return -1,-1 if no apple was found
  def find_apple(self):
    for x in range(35):
      for y in range(35):
        if self.board[y][x] == "APPLE":
          return x, y
    #no apple?
    print("AI- Warning: No apple found")
    return -1, -1

  #--- private methods ---
  #don't overload these

  #check if we are dead
  def is_dead(self):
    prog = self._api.check_progress()
    if self.snek.prog_name in prog:
      return prog[self.snek.prog_name]["isDead"]
    return False

  #make the ai's move
  def run_move(self):
    if self.is_dead():
      print("AI: WARNING: OUR SNEK IS DEAD")
    move = self.make_move()
    print("AI: making move: " + str(move))
    self._api.send_turn(move)
    print("AI: done")

  #start the ai loop
  def run(self):
    #reset
    self._api.reset_test()
    #update the board
    self._api.update_board()

    #make the first move
    self.run_move()
    #and loop
    while True:
      #wait for the board to change
      self._api.wait_for_change()
      #and make move
      self.run_move()

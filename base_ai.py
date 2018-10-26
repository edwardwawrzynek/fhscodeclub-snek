from snek import Snek
from api import API
import random
from debug import debug

#a base class for other ai's

class BaseAI:
  #don't override constructor
  def __init__(self, snek, api, draw_board, enemy_sneks):
    #the api object - don't use this directly
    self._api = api
    self._draw_board = draw_board

    #--- these attributes can be accessed by AI's ---
    #the snek object
    self.snek = snek
    #the enemy sneks
    self.enemy_sneks = enemy_sneks

  #main ai function - based on the board, decide on a move, and return it
  #the move returned is either a -1, 0, or 1, for left, forwards, or right
  #new AI's should override this
  def make_move(self):
    #place overriden ai here - self.get_board, self.is_empty, self.get_apple, and other functions are useful here,
    #along with self.snek.x and self.snek.y

    #make a random move
    return random.randrange(-1,2,1)

  #get the board state
  def get_board(self):
    return self._api.board

  #check whether a spot on the board is empty (or contains an apple) or not
  def is_empty(self, x, y):
    if x < 0 or x >= 35 or y < 0 or y >= 35:
      return False
    return self.get_board()[y][x] == "EMPTY" or self.get_board()[y][x] == "APPLE"

  #get the position of the apple on the board - return it as an (x,y) tuple,
  #or return -1,-1 if no apple was found
  def find_apple(self):
    for x in range(35):
      for y in range(35):
        if self.get_board()[y][x] == "APPLE":
          return x, y
    #no apple?
    debug("AI- Warning: No apple found")
    return -1, -1

  #return a three item list of where each move would place the head of the snek
  #array item 0 is left turn, item 1 forward turn, and 2 right turn
  def get_potential_moves(self):
    res = []
    turn = -1
    for i in range(3):
      x, y, new_dir = self.snek.move_pos(turn)
      res.append([x, y])
      turn += 1

    return res

  #get the distance between cells
  def dist_to(self, x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

  #check if a cell is on the board
  def on_board(self, x, y):
    return x>=0 and x<35 and y>=0 and y<35

  #--- private methods ---
  #don't overload these

  #check if we are dead
  def is_dead(self):
    debug("AI: checking if we are dead");
    prog = self._api.check_progress()
    if self.snek.prog_name in prog:
      return prog[self.snek.prog_name]["isDead"]
    return False

  #make the ai's move
  def run_move(self):
    #update enemy sneks
    for s in self.enemy_sneks:
      s.update_head(self._api.board)
    if self._draw_board:
      self.print_board()
    debug("Snek: Pos: " + str(self.snek.x) + ", " + str(self.snek.y))
    debug("Snek: Direction: " + str(self.snek.direction))
    if self.is_dead():
      debug("AI: WARNING: THE SNEK IS DEAD")
    move = self.make_move()
    debug("AI: making move: " + str(move))
    self._api.send_turn(move)
    self.snek.move(move)
    debug("AI: done")

  #start the ai loop
  def run(self):
    #update the board
    self._api.update_board()
    #make the first move
    self.run_move()
    #and loop
    while True:
      #wait for the board to change
      self._api.wait_for_change(self.snek.prog_name)
      #and make move
      self.run_move()

  #debug - print the board in the terminal
  def print_board(self):
    board = self.get_board()
    print("#" * 37)
    for y in range(35):
      print("#",end="", flush=False)
      for x in range(35):
        if board[y][x] == "EMPTY":
          print(".", end="", flush=False)
        else:
          if board[y][x] == "RED_SNEK":
            print("\x1b[31m", end="", flush=False)
          if board[y][x] == "GREEN_SNEK":
            print("\x1b[32m", end="", flush=False)
          if board[y][x] == "BLUE_SNEK":
            print("\x1b[34m", end="", flush=False)
          if board[y][x] == "YELLOW_SNEK":
            print("\x1b[33m", end="", flush=False)
          print(u"\u2588\x1b[0m", end="", flush=False)

      print("#", flush=False)
    print("#" * 37, flush=True)
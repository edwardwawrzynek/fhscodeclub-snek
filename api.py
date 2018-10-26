import requests, time

#to copy board to prev_board
#if deepcopy isn't used, array rows will be copied, but will point to the same objects
from copy import deepcopy

from debug import debug

#the api interface
class API:
  def __init__(self, url, key):
    #the url to work with (/ or /test - DON'T include /api)
    self.url = url
    #the api key
    self.key = key
    #the current board
    self.board = []
    #the previous board - for waiting for changes
    self.prev_board = []
    #the last turn number on pos
    self.last_turn_num = 0
    #the last submitted value
    self.last_submit = -2
    #init the board
    debug("API: loading initial board state...")
    self.update_board()
    debug("API: board state loaded")

  #reset the test api state
  def reset_test(self):
    params = {"key": self.key}
    requests.post(self.url + "/api", params=params)

  #update the current api board state
  def update_board(self):
    params = {"key": self.key}
    self.prev_board = deepcopy(self.board)
    self.board = requests.get(self.url + "/api", params=params).json()
    return self.board

  #do a turn (-1, 0, or 1)
  def send_turn(self, direction):
    params = {"turnDirection": direction, "key": self.key}
    self.last_submit = direction
    self.last_turn_num = requests.post(self.url + "/api", params=params).json()

  #check the progress
  def check_progress(self):
    params = {"key": self.key}
    return requests.get(self.url + "/api/progress", params=params).json()

  #wait for the board state to change from prev_board, and return when it does
  def wait_for_change(self, snek_prog_name):
    debug("API: waiting for board to change", end="", flush=True)
    while True:
      prog = self.check_progress()
      #get turn
      turn = prog["turn"]
      #if new turn, return
      if turn > self.last_turn_num:
        self.last_turn_num = turn
        debug("\nAPI: board change detected\nAPI: updating board")
        self.update_board()
        debug("API: done")
        return
      debug(".", end="", flush=True)
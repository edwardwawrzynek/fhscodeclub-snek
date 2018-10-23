import requests, time

#to copy board to prev_board
#if deepcopy isn't used, array rows will be copied, but will point to the same objects
from copy import deepcopy

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
    #init the board
    print("API: loading initial board state...")
    self.update_board()
    print("API: board state loaded")

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
    requests.post(self.url + "/api", params=params)

  #check the progress
  def check_progress(self):
    params = {"key": self.key}
    return requests.get(self.url + "/api/progress", params=params).json()

  #wait for the board state to change from prev_board, and return when it does
  def wait_for_change(self):
    #get new board
    print("API: waiting for board to change", end="")
    self.update_board()
    #wait for a change
    while self.board == self.prev_board:
      #wait a bit so we don't overload the server
      time.sleep(0.05)
      #get new board
      self.update_board()
      print(".", end="", flush=True)
    print("\nAPI: board change detected")

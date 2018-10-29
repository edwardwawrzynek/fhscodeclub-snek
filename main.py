from api import API
from snek import Snek, EnemySnek
from base_ai import BaseAI
from keyboard_ai import KeyboardAI
from smart_ai import SmartAI
import debug
import sys

# The different sneks, going clockwise
SNEK_NAMES = ["RED_SNEK", "GREEN_SNEK", "YELLOW_SNEK", "BLUE_SNEK"]
SNEK_PROG_NAMES = ["RED", "GREEN", "YELLOW", "BLUE"]
SNEK_KEYS = ["RED5", "GREEN5", "YELLOW5", "BLUE5"]

SNEK_LOCATIONS = [[1, 0], [34, 1], [33, 34], [0, 33]]
SNEK_DIRECTS = [2, 3, 0, 1]

#the ai's to use
AIS = [BaseAI, KeyboardAI, SmartAI]
#the ai names to choose from
AI_NAMES = ["BaseAI", "KeyboardAI", "SmartAI"]

#specify color and ai name on command line

if len(sys.argv) != 3:
  print("usage: main.py [snek_color] [AI name]\nsnek_color - RED, GREEN, etc\nAI name - BaseAI, KeyboardAI, SmartAI, etc")
  exit(0)

SNEK_INDEX = SNEK_PROG_NAMES.index(sys.argv[1])
CHOOSEN_AI = AIS[AI_NAMES.index(sys.argv[2])]

#create the array of enemy sneks
ENEMY_SNEKS = []
for i in range(len(SNEK_LOCATIONS)):
  if i != SNEK_INDEX:
    ENEMY_SNEKS.append(EnemySnek(
      SNEK_LOCATIONS[i][0], SNEK_LOCATIONS[i][1],
      SNEK_NAMES[i],
      SNEK_PROG_NAMES[i]
    ))

#The URL to use
API_URL = "http://fairviewcodekatasnek.herokuapp.com"
#API_URL = "http://localhost:8080"
#The key to use
API_KEY = SNEK_KEYS[SNEK_INDEX]
#the name of the snek
SNEK_NAME = SNEK_NAMES[SNEK_INDEX]
#the name of the snek in /progress
SNEK_PROG_NAME = SNEK_PROG_NAMES[SNEK_INDEX]

#whether to draw the board for debug
DRAW_BOARD = True
#whether to print out other debug information
debug.DEBUG_ENABLED = True

def main():
  #main snek - in the lower right corner, heading left
  snek = Snek(SNEK_LOCATIONS[SNEK_INDEX][0], SNEK_LOCATIONS[SNEK_INDEX][1], SNEK_DIRECTS[SNEK_INDEX], SNEK_NAME, SNEK_PROG_NAME)
  #api object
  api = API(API_URL, API_KEY)
  #reset
  api.reset_test()
  #create the ai
  ai = CHOOSEN_AI(snek, api, DRAW_BOARD, ENEMY_SNEKS)
  #run the ai
  ai.run()

main()

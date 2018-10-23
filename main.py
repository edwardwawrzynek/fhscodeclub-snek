from api import API
from snek import Snek
from base_ai import BaseAI
from keyboard_ai import KeyboardAI

#The URL to use
API_URL = "http://fairviewcodekatasnek.herokuapp.com/test"
#The key to use
API_KEY = "YELLOW5"
#the name of the snek
SNEK_NAME = "YELLOW_SNEK"
#the name of the snek in /progress
SNEK_PROG_NAME = "YELLOW"

#the ai's to use
AIS = [BaseAI, KeyboardAI]
#the ai names to choose from
AI_NAMES = ["BaseAI", "KeyboardAI"]

def main():
  #main snek - in the lower right corner, heading left
  snek = Snek(33, 34, 0, SNEK_NAME, SNEK_PROG_NAME)
  #api object
  api = API(API_URL, API_KEY)
  #create the ai
  ai = choose_ai()(snek, api)
  #run the ai
  ai.run()

#choose an ai from the command line
def choose_ai():
  while True:
    ai_name = input("Choose an ai to use(" + str(AI_NAMES)[1:-1] + "):")
    try:
      return AIS[AI_NAMES.index(ai_name)]
    except ValueError:
      print("No such AI:" + ai_name)
      continue

main()
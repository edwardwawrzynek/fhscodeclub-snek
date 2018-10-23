from api import API
from snek import Snek
from base_ai import BaseAI

#The URL to use
API_URL = "http://fairviewcodekatasnek.herokuapp.com/test"
#The key to use
API_KEY = "YELLOW5"
#the name of the snek
SNEK_NAME = "YELLOW_SNEK"
#the name of the snek in /progress
SNEK_PROG_NAME = "YELLOW"

def main():
  #main snek - in the lower right corner, heading left
  snek = Snek(33, 34, 1, SNEK_NAME, SNEK_PROG_NAME)
  #api object
  api = API(API_URL, API_KEY)
  #create the ai
  ai = BaseAI(snek, api)
  #run the ai
  ai.run()


main()
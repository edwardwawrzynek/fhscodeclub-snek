import requests
import random

#url for app - switch for testing
APP_URL = "http://fairviewcodekatasnek.herokuapp.com"
#key to send with data
API_KEY = "YELLOW5"
#our snake
SNAKE_NAME = "YELLOW_SNEK"

#Starting Position
INIT_POS = 0
#Direction (0=left, 1=up, 2=right, 2=down)
CUR_DIR = 0

class BoardPos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#get a 34 x 34 array of strings representing the board
def api_get_board():
    params = {"key": API_KEY}
    return requests.get(APP_URL + "/api", params=params).json()

#rotate a cur dir
def rotate_cur_dir(cur_dir, turn_dir):

    if turn_dir == 0:
        return cur_dir
    if turn_dir == 1:
        cur_dir += 1
        if cur_dir == 4:
            cur_dir = 0
    elif turn_dir == -1:
        cur_dir -= 1
        if cur_dir == -1:
            cur_dir = 3

    return cur_dir

def api_reset():
    params = {"key": API_KEY}
    #requests.post(APP_URL + "/api", params=params)
    requests.post(APP_URL + "/api")

#turn the snake
#direction is int -1=left 0=forwards 1=right
def api_turn(direction):
    global CUR_DIR
    #turn CUR_DIR
    CUR_DIR = rotate_cur_dir(CUR_DIR, direction)
    #adjust pos
    if CUR_DIR == 0:
        INIT_POS.x -= 1
    elif CUR_DIR == 1:
        INIT_POS.y -= 1
    elif CUR_DIR == 2:
        INIT_POS.x += 1
    elif CUR_DIR == 3:
        INIT_POS.y += 1
    params = {"turnDirection": direction, "key": API_KEY}
    requests.post(APP_URL + "/api", params=params)

#Hacky Keyboard Control (As a last resort)
def keyboard_control():
    print("Position:" + str(INIT_POS.x) + "," + str(INIT_POS.y))
    while True:
        #get direction (l, f, r) for left, forward, or right
        dir = input("Direction (l, f, r):")
        if dir == "l":
            api_turn(-1)
        elif dir == "f":
            api_turn(0)
        elif dir == "r":
            api_turn(1)
        else:
            print("unrecognized option")
            continue
        print("good")
        print("Position:" + str(INIT_POS.x) + "," + str(INIT_POS.y))

def main():
    api_reset()
    keyboard_control()

INIT_POS = BoardPos(33, 34)
CUR_DIR = 0
main()
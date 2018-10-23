from base_ai import BaseAI

class KeyboardAI(BaseAI):
  def make_move(self):
    dir = input("Move (l,f,r):")
    if dir == "l":
      return -1
    elif dir == "f":
      return 0
    elif dir == "r":
      return 1
    print("Unrecognized choice")
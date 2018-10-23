from base_ai import BaseAI

class KeyboardAI(BaseAI):
  def make_move(self):
    while True:
      dir = input("Move (l,f,r):")
      if len(dir) < 1:
        print("Unrecognized choice")
        continue
      if dir[-1] == "l":
        return -1
      elif dir[-1] == "f":
        return 0
      elif dir[-1] == "r":
        return 1
      print("Unrecognized choice")
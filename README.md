# Snek AI
Note: I changed the layout of the project. It is described below.

The following files make up the project:
* `api.py` - the API interface
* `snek.py` - the Snek class, representing our snek and where it is
* `main.py` - the script to run - it starts up the API and starts the AI
* `base_ai.py` - the BaseAI class, which all other AI's inherit from. It provides some helper functions, and method to override.
  * `keyboard_ai.py` - an ai that moves based on keyboard input.

## Making a new AI
See `keyboard_ai.py` for an example. The AI should define a class inheriting from `BaseAI`, and override the `make_move` method. The ai class should also be added to `AIS`, and the name to `AI_NAMES` in `main.py`.

### `make_move`
`make_move` accepts no inputs, and must return an output of the move it whishes to make given the current state. The returned move is -1,0,or 1, (left, forwards, right).

`make_move` can use the following attributes and methods to decide what move to make:
* `self.get_board()` - returns the current board state. It is a 35 x 35 array indexed as `self.get_board()[y][x]`. Each entry is either `"EMPTY"`, `"APPLE"`, `"RED_SNEK"`, `"BLUE_SNEK"` etc.
* `self.snek.x` - the current x position of the snek.
* `self.snek.y` - the current y position of the snek.
* `self.snek.direction` - the current direction the snek is heading. 0=left, 1=up, 2=right, 3=down.
* `self.is_empty(x,y)` return `True` if a cell on the board is empty (or has the apple), or `False` if something is in it. It will also return `False` if the specified cell isn't on the board.
* `self.find_apple()` return `(x,y)`, where x and y are the coordinates of the apple on the board. Returns `(-1, -1)` if no apple is found.
#debug output enable
DEBUG_ENABLED = True

def debug(msg, end="\n", flush=True):
  if DEBUG_ENABLED:
    print(msg, end=end, flush=flush)

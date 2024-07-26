import random
import curses
from curses import wrapper

with open("terminal.txt", "r") as f:
  terminal = f.read()

def random_terminal():
  print(random.choice(get_terminal_blocks()))

  
def get_terminal_blocks():
  blocks = []
  start_of_block = -1
  target_start = "<"
  target_end = ">"

  for i, char in enumerate(terminal):
    if char == target_start:
      start_of_block = i
    
    if char == target_end and start_of_block != -1:
      block = terminal[start_of_block: i + 1]
      blocks.add(block)
      start_of_block = -1
  
  return blocks
  

def main(stdscr):
  curses.use_default_colors()
  curses.init_pair(1, curses.COLOR_GREEN, -1)

  stdscr.clear()
  stdscr.refresh()

  while True:
    key = stdscr.getkey()

    try:
      if ord(key) == 27:
        break
      elif ord(key) == 10:
        print(get_terminal_blocks())
      else:
        stdscr.addstr("Blah")
    except:
      pass

wrapper(main)

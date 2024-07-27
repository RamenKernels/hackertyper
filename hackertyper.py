import random
import keyboard
import time
import sys
from colorama import Fore

with open("terminal.txt", "r") as f:
  terminal = f.read()

with open("code.txt", "r") as s:
  code = s.read()

def get_terminal_blocks():
  blocks = terminal.split("\n")
  
  return blocks

def run_terminal():
  line_num = 0
  start_time = time.time()

  while True:
    try:
      line = get_terminal_blocks()[line_num]
      print(Fore.GREEN + f"{line}")
    except:
      print("\n")
    line_num += 1
    if line_num > 22:
      line_num = 0
    end_time = time.time()
    if end_time - start_time >= 10:
      break

    time.sleep(random.uniform(0.001, 0.6))

def main():
  i = 0
  while True:
    if keyboard.is_pressed("escape"):
      break
    elif keyboard.is_pressed("enter"):
      run_terminal()
    elif keyboard.read_hotkey():
      sys.stdout.write(Fore.GREEN + code[i])
      i += 1
      if i >= len(code):
        i = 0

main()

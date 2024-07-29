import random
import time
import sys
from datetime import datetime
from colorama import Fore

with open("terminal.txt", "r") as f:
  terminal = f.read()

def get_terminal_blocks():
  blocks = terminal.split("\n")
  return blocks

def run_terminal():
  line_num = 0
  start_time = time.time()

  while True:
    try:
      line = random.choice(get_terminal_blocks())
      dt_string = datetime.now().strftime("%m/%d/%y %H:%M:%S")
      print(Fore.GREEN + f"{dt_string}{line}")
    except:
      pass
    end_time = time.time()
    if end_time - start_time >= 10:
      break

    time.sleep(random.uniform(0.01, 0.1))

def main():
  input("\nPress enter to run")
  time.sleep(1)
  run_terminal()
  print("\nActivation Complete!")

if __name__ == "__main__":
    main()

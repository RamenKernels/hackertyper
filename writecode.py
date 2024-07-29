import random
import getch
import time
from colorama import Fore
import terminal

speed: int = 2

with open("code.txt", "r") as f:
    code = f.read()

def initialize() -> None:
    print(Fore.GREEN)
    print("Initializing.")
    time.sleep(0.5)
    print("Initializing..")
    time.sleep(0.5)
    print("Initializing...")
    time.sleep(0.5)
    print("Initialization Complete!\n")

def writecode() -> None:
    i = 0
    while True:
        key = getch.getch()
        if key == "\n":
            terminal.main()
        elif key == "\u001b":
            return
        else:
            for i in range(i+speed):
                print(code[i], end="", flush=True)
        i += 1
        if i > 6934:
            i = 0

def main():
    initialize()
    writecode()

    print(Fore.RESET, end="\n", flush=False)

if __name__ == "__main__":
    main()
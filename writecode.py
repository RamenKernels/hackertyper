import random
import getch
import time
from colorama import Fore
import terminal

with open("code.txt", "r") as f:
    code = f.read()


def get_speed() -> int:
    while True:
        usr_input = input("Choose a typing speed >> ")
        try:
            if int(usr_input) < 1:
                print("Value must be a positive integer!")
            else:
                return int(usr_input)
        except:
            print("Value must be a positive integer!")


def initialize() -> None:
    print(Fore.GREEN)
    time.sleep(0.5)
    print("Initializing.")
    time.sleep(0.5)
    print("Initializing..")
    time.sleep(0.5)
    print("Initializing...")
    time.sleep(0.5)
    print("Initialization Complete!\n")


def writecode(type_speed) -> None:
    i = 0
    while True:
        key = getch.getch()
        if key == "\n":
            terminal.main()
        elif key == "\u001b":
            return
        else:

            for j in range(0, type_speed):
                print(code[i + j], end="", flush=True)

        i += type_speed
        if i > 6934:
            i = 0


def main():
    initialize()
    writecode(get_speed())

    print(Fore.RESET, end="\n", flush=False)


if __name__ == "__main__":
    main()

import random
import getch
import time
from colorama import Fore
import terminal

with open("code.txt", "r") as f:
    code = f.read()

def main():
    print(Fore.GREEN, "Initializing.")
    time.sleep(1)
    print(Fore.GREEN, "Initializing..")
    time.sleep(1)
    print(Fore.GREEN, "Initializing...")
    time.sleep(1)
    print(Fore.GREEN, "Activation Complete! \n")
    while True:
        for char in code:
            key = getch.getch()
            if key in ['\r\n', "\r", "\n", 13, 10, 0xd]:
                terminal.main()
            else:
                print(char, end="", flush=True)

if __name__ == "__main__":
    main()
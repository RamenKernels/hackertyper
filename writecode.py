import random
import curses
import time
from colorama import Fore

speed = 5

with open("code.txt", "r") as f:
    code = f.read()

with open("terminal.txt", "r") as g:
    terminal_lines = g.readlines()


def get_input(stdscr):
    key = stdscr.getch()
    if key == 263:
        stdscr.clear()
        stdscr.addstr(0, 0, "Quitting the program...", curses.color_pair(1))
        return
    elif key == 10:
        stdscr.clear()
        while True:
            for line in terminal_lines:
                stdscr.addstr(line, curses.color_pair(1))
                stdscr.refresh()
                time.sleep(random.random() / 2)


def main(stdscr):
    stdscr.clear()

    curses.cbreak()
    stdscr.keypad(True)
    stdscr.scrollok(True)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    while True:
        for i in range(0, len(code)):
            if i % speed == 0:
                get_input()

            stdscr.addstr(code[i], curses.color_pair(1))
            stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)


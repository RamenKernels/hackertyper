import random
import curses
import time
from colorama import Fore

with open("code.txt", "r") as f:
    code = f.read()

with open("terminal.txt", "r") as g:
    terminal_lines = g.readlines()

def run_terminal(stdscr):
    while True:
        for line in terminal_lines:
            stdscr.addstr(line, curses.color_pair(1))
            stdscr.refresh()
            time.sleep(random.random() / 20)

def main(stdscr):
    speed = 5
    current_index = 0
    char_queue = []
    frame_count = 0

    stdscr.clear()

    curses.cbreak()
    stdscr.keypad(True)
    stdscr.scrollok(True)
    stdscr.nodelay(True)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    while True:
        key = stdscr.getch()
        if key == 27:
            stdscr.clear()
            stdscr.addstr(0, 0, "Quitting the program...", curses.color_pair(1))
            return
        elif key == 10:
            stdscr.clear()
            run_terminal()
        elif key != -1:
            for i in enumerate(range(speed)):
                char_queue.append(code[current_index])
                current_index += 1

        if char_queue != []:
            stdscr.addstr(char_queue[0], curses.color_pair(1))
            char_queue.pop(0)
            frame_count = 0

        frame_count += 1
        time.sleep(0.02)


if __name__ == "__main__":
    curses.wrapper(main)


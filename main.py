import random
import curses
import time

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


def get_speed(frames_elapsed):
    return 50 - frames_elapsed


def main(stdscr):
    speed_mult = 5
    current_index = 0
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
            run_terminal(stdscr)
        elif key in [curses.KEY_BACKSPACE, 127, 8]:
            y, x = stdscr.getyx()
            if x > 0:
                stdscr.move(y, x - 1)
                stdscr.delch()
        elif key != -1:
            char = chr(key) if 0 <= key <= 255 else None

            if frame_count > 50:
                stdscr.addstr(char, curses.color_pair(1))
            else:
                for _ in enumerate(range(get_speed(frame_count))):
                    stdscr.addstr(code[current_index], curses.color_pair(1))
                    current_index += 1

                    if current_index >= len(code):
                        current_index = 0
                        stdscr.addstr("\n")
            frame_count = 0

        frame_count += 1
        time.sleep(0.02)


if __name__ == "__main__":
    curses.wrapper(main)

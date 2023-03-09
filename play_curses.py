import curses
import os
from time import sleep


def main(win):
    win.nodelay(True)
    key = ""
    win.clear()
    win.addstr("Detected key:")
    while 1:
        try:
            key = win.getch()
            if key > 0:
                win.clear()
                win.addstr("Detected key: ")
                win.addstr(str(key))
                if key == os.linesep:
                    break
            sleep(0.1)
        except Exception as e:
            # No input
            pass


curses.wrapper(main)

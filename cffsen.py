#!/usr/bin/env python3

from curses import *
from sys import argv, exit
import os

if len(argv) < 2:
    print('You must give me some video files.')
    exit(1)

def main(scr):
    scr.clear()

    for i in range(0, 9):
        v = i-10
        scr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    scr.refresh()
    os.system('imgcat "/Users/chrissx/Desktop/Screenshot 2021-02-25 at 11.21.06.png"')
    scr.getkey()

wrapper(main)

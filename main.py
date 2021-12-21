import curses
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target_text, current_text, wpm=0):
    stdscr.addstr(target_text)

    for pos, char in enumerate(current_text):
        correct_char = target_text[pos]
        color = curses.color_pair(1)

        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, pos, char, color)

wrapper(main)

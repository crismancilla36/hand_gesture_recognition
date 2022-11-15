from modules.load_data import *

import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    if len(sys.argv) == 1:
        pass
    elif sys.argv[1] == 'save_gesture':
        save_gesture(sys.argv[2])

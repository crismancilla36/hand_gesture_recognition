from modules.input import *
from modules.load_data import *
from modules.training import *

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        model, labels = train_model()
        get_gesture(model, labels)
    elif sys.argv[1] == 'save_gesture':
        save_gesture(sys.argv[2])
    elif sys.argv[1] == 'training':
        train_model()
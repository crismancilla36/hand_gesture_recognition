from modules.input import *
from modules.load_data import *
from modules.training import *

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        model, labels = train_model()

        iterator = get_gesture(model, labels)
        for it in iterator:
            """
                it: (gesture_index, gesture_label)
            """
            print(it[0], it[1])

    elif sys.argv[1] == 'save_gesture':
        save_gesture(sys.argv[2])
    elif sys.argv[1] == 'training':
        train_model()
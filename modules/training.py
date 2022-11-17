import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score


def load_dataset():
    print("Loading data...")
    arr = np.loadtxt("resources/data.csv",
                     delimiter=",", dtype=str)
    n_col = arr.shape[1]

    map_to_float = np.vectorize(float)
    x = map_to_float(arr[:, :n_col - 1])

    labels, y = np.unique(arr[:, n_col - 1:], return_inverse=True)

    print("Spliting data")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    return x_train, x_test, y_train, y_test, labels


def train_model():
    x_train, x_test, y_train, y_test, labels = load_dataset()
    model = DecisionTreeClassifier(random_state=13)
    print('training')
    model.fit(x_train, y_train)
    predicted = model.predict(x_test)

    accuracy = accuracy_score(predicted, y_test)
    print(f'Precision: {accuracy}')
    return model, labels

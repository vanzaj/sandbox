import os.path as path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def this_dir():
    return path.dirname(path.abspath(__file__))


def read_bank_note_data():
    return pd.read_csv(path.join(this_dir(), "bank_note_auth.csv"))


def split_training_data(data):
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    return train_test_split(X, y, test_size=0.3, random_state=42)


def train_model(X_train, X_test, y_train, y_test):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy


def main():
    data = read_bank_note_data()
    X_train, X_test, y_train, y_test = split_training_data(data)
    model, accuracy = train_model(X_train, X_test, y_train, y_test)
    return model, accuracy


if __name__ == "__main__":
    model, accuracy = main()
    model.accuracy = accuracy
    joblib.dump(model, path.join(this_dir(), "bank_note_model.joblib"))

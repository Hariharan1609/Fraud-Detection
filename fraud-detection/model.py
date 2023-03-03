import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
def predictions(path):
    credit_card_data = pd.read_csv(path)
    loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
    legit = credit_card_data[credit_card_data.Class == 0]
    fraud = credit_card_data[credit_card_data.Class == 1]
    legit_sample = legit.sample(n=492)
    new_dataset = pd.concat([legit_sample, fraud], axis=0)
    X = new_dataset.drop(columns='Class', axis=1)
    Y = new_dataset['Class']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    X_train_prediction = model.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
    X_test_prediction = model.predict(X_test)
    test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
    x=[i for i in X_train_prediction if i==0]
    y = [i for i in X_train_prediction if i == 1]
    print(training_data_accuracy)
    print(X_train_prediction)
    training_data_accuracy*=100
    training_data_accuracy=round(training_data_accuracy,3)
    test_data_accuracy*=100
    test_data_accuracy=round(test_data_accuracy,3)
    return len(x),len(y),training_data_accuracy,test_data_accuracy









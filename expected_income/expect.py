import pandas
import pickle

def expect(size, year):
    with open('trainend-model.pickle', 'rb') as b:
        reg = pickle.load(b)
    predicted_income = reg.predict([[size, year]])[0]
    rounded_income = round(predicted_income, 1)
    return rounded_income
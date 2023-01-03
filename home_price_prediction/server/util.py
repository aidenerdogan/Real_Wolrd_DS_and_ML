import json
import pickle
import numpy as np


#creating global variabes
__locations = None
__data_columns = None
__model = None

def get_estimated_price(locations, sqft, bath_num, bhk):
    try:
        loc_index = __locations.index(locations.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath_num
    x[2] = bhk
    if loc_index >= 0:
        loc_index = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...Started! ")
    global __data_columns
    global __locations
    global __model

    with open('/Users/ahmeterdogan/Desktop/DS---ML-Real-World-Projects/Home Price Prediction/server/artifacts/columns.json', 'r') as file:
        __data_columns = json.load(file)['data_columns']
        __locations = __data_columns[3:]
    
    with open('/Users/ahmeterdogan/Desktop/DS---ML-Real-World-Projects/Home Price Prediction/server/artifacts/home_prices_prediction_model.pickle', 'rb') as file:
        __model = pickle.load(file)
    
    print("Loading saved artifacts is done!")



if __name__ == '__main__':
    print("I am wroking")
    load_saved_artifacts()
    print(get_location_names())

    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
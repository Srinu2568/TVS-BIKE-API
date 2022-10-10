# imports
import uvicorn
from fastapi import FastAPI
from FeaturesNote import FeatureNote
import pickle
import json
import numpy as np
import pandas as pd

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

pickle_in = open('bike_price_predictor.sav', 'rb')
rf = pickle.load(pickle_in)

params = '''bike_name city kms_driven owner age power brand'''

# index func - route('/')
@app.get('/')
def index():
    return {'message': 'This API is for two wheeler'}

@app.post('/bike-predict')
def predict_price(data: FeatureNote):
    data = data.dict()
    print(data)
    bike_name = data['bike_name']
    city = data['city']
    kms_driven = data['kms_driven']
    owner = data['owner']
    age = data['age']
    power = data['power']
    brand = data['age']
    bike_price_prediction = rf.predict([[bike_name, city, kms_driven, owner, age, power, brand]])
    return {
        'bike_price_prediction': bike_price_prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
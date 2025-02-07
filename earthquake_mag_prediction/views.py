import calendar
import joblib
import numpy as np
import pandas as pd
import datetime
import time
import pickle
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from xgboost import XGBRegressor
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from sklearn.ensemble import VotingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
import mlflow
import mlflow.sklearn
import datetime
# from earthquake_mag_prediction.views import scale_inputs

# Load the model from the file
model_file_path = 'C:/Users/dell/Downloads/knn_model_2025-02-07_11-36-33.pkl'
knn = joblib.load(model_file_path)

with open('C:/Users/dell/Downloads/scaler_2025-02-07_11-36-33.pkl', 'rb') as f:
    scaler = pickle.load(f)
#################################

#################################
def home(request):
    return render(request,'home.html')

def predict(request):
   
    return render(request,'predict.html')

def result(request):
    
    var1 = float(request.GET['longitude'])
    var2 = float(request.GET['latitude'])
    var3 = float(request.GET['depth'])
    time_t = request.GET['timestamp']
    var4 = convert_time_to_timestamp(time_t)
    
    scaled_values=scale_inputs(var1, var2, var3, var4)

    # pred = knn.predict(np.array([var1, var2, var3, var4]).reshape(1, -1))
    pred = knn.predict(scaled_values.reshape(1, -1))
   
    # pred = pred[0]
    
    magnitude = 'the predicted magnitude is: ' + str(pred)
    print(f"Predicted Magnitude: {pred}")
   
    
    
    return HttpResponse(magnitude, content_type="text/plain")
    # return render(request, 'predict.html', {'magnitude': magnitude})

# here we will define functionsto use it in other function
# like we want to convert time to timestamp
# and also make scale for the input data
def convert_time_to_timestamp(real_time):
        # Adjust format string to match 'YYYY-MM-DDTHH:MM:SS.sssZ' format
        ts = datetime.datetime.strptime(real_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        # Use calendar.timegm to get the Unix timestamp
        timestamp = calendar.timegm(ts.utctimetuple())
        return float(timestamp)

# here we will define function to scale data 
# using standard scaler
def scale_inputs(var1, var2, var3, var4):
    """
    Scales the input data using StandardScaler.

    Parameters:
    var1, var2, var3, var4 (float): The input values to be scaled.
    Returns:
    np.ndarray: An array containing the scaled values.
    """
    values = np.array([var1, var2, var3, var4], dtype=float).reshape(1, -1)
    scaled_values = scaler.transform(values)
    print(scaled_values[0])
    return scaled_values[0]

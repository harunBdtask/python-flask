from flask import Blueprint, jsonify, request
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import linregress
from sklearn import linear_model
stat = Blueprint('stat', __name__)
# Simple Route
@stat.route('/home')
def home():
    return 'Hello, Stat!'
# post request demo
@stat.route('/demo', methods=['POST'])
def demo():
    # Access the request parameters
    name = request.form.get('name')

    data = request.get_json()
     # Access the parameters from the JSON data
    name = data.get('name')
    cart_details = data.get('cart_details')
    # Create a response
    response = {'name': name, 'cart_details':cart_details}

    return jsonify(response)
# extrapolation route
@stat.route('/extrapolation')
def extrapolation():
    # Year=[2010,2011,2012,2013,2014]
    # Death=[25,30,24,26,31]
    Year=[2016,2017,2018,2019]
    Death=[25,30,20,25]
    X = np.array(Year)
    y = np.array(Death)
    X = X.reshape(-1,1)
    y = y.reshape(-1,1)
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    Year_1=Year[-1]+1
    mymodel = np.poly1d(np.polyfit(Year, Death, 3))
    A = np.array(Year)
    B = np.array(Death)
    fit = np.polyfit(np.log(A), B, 1)
    theDict = {
        'linear': str(regr.predict([[Year_1]])),
        'polynomial': round(mymodel(Year_1),2),
        'logarithmic': str(fit)
    }
    return jsonify(theDict)

# correlation route
@stat.route('/correlation')
def correlation():
    X_Variable=[1,2,3,4,5,6,7]
    Y_Death=[1.5,3.8,6.7,9.0,11.2,13.6,16]

    X = np.array(X_Variable)
    y = np.array(Y_Death)
    corr, _ = pearsonr(X, y)
    data = np.sort(Y_Death)
    minSlopeX = X.min()
    maxSlopeX = X.max()
    linregressValue = linregress(X, y)
    slopeValue = linregressValue[0]
    intercept = linregressValue[1]
    minSlopeY = (slopeValue * minSlopeX) + intercept
    maxSlopeY = (slopeValue * maxSlopeX) + intercept

    thisdictTest = {
        "0_min": int(X.min()),
        "1_max": int(X.max()),
        "2_linregress": (linregress(X, y)),
        "3_mean": np.median(data),
        "4_sort": data.tolist(),
        "5_pearsonr": ('Pearsons correlation: %.3f' % corr),
        "6_Min_Slope_X": int(X.min()),
        "7_Max_Slope_X": int(X.max()),
        "8_Min_Slope_Y": ('%.3f' % minSlopeY),
        "9_MAX_Slope_Y": ('%.3f' % maxSlopeY),
    }

    thisdict = {
        "Min_Slope_X": ('%.2f' % X.min()),
        "Max_Slope_X": ('%.2f' % X.max()),
        "Min_Slope_Y": ('%.2f' % minSlopeY),
        "MAX_Slope_Y": ('%.2f' % maxSlopeY),
    }
    return jsonify(thisdict)


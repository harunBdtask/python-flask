from flask import Blueprint, jsonify
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import linregress
stat = Blueprint('stat', __name__)
# Simple Route
@stat.route('/home')
def home():
    return 'Hello, Stat!'
# Example route for returning a JSON response
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


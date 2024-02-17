'''
This program is for transforming non-statinary time series data(i.e., data having more fluctuation) into
stationary time series data by using the method of:-

Simple Exponential Smoothing: giving more wieghtage to recent data than previous data.

'''

# Importing necessary libraries
import pandas as pd 
from matplotlib import pyplot as plt

# statsmodels.tsa.api used to import time series techniques to make data stationary
from statsmodels.tsa.api import SimpleExpSmoothing 


# Read data from csv
dataset = pd.read_csv('sinewave.csv')
print (dataset)

# Simple exponential Smoothing: for more weightage to recent data___________________

for i in range(1,10):
    
    i=i*0.1 # range of 'i' becomes 0.1 to 1.0
    
    fit1 = SimpleExpSmoothing(dataset).fit(smoothing_level=i, optimized = False)# Alpha = i
    
    plt.plot(fit1.fittedvalues, label= 'simple exponential approach data', color='r')
    plt.legend()

    plt.plot(dataset, label='original data', color = 'g')
    plt.legend()
    plt.text(0,0.5,'Alpha= '+str(round(i,2))) # round off Alpha to 1 decimal place
    plt.show()


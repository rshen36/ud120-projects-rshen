#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    s = int(0.9*(len(predictions)))
    residuals = abs(np.subtract(predictions, net_worths))
    cleaned_data = sorted(zip(ages, net_worths, residuals), key=lambda x: x[2])
    cleaned_data = cleaned_data[:s]

    return cleaned_data


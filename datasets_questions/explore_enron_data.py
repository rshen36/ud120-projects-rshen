#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np
import imp

path = '/Users/rshen/github/Udacity/ud120-projects/tools/feature_format.py'
feature_format = imp.load_source('featureFormat', path)
target_feature_split = imp.load_source('targetFeatureSplit', path)

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count = 0.0
for person in enron_data:
  if enron_data[person]['poi'] == 1:
    if enron_data[person]['total_payments'] == 'NaN': count += 1
print count
print len(enron_data.keys())
print count/len(enron_data.keys())
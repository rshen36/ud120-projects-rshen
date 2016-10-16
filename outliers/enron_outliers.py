#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.preprocessing import MinMaxScaler
import numpy as np

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)
features = ["salary", "exercised_stock_options"]
data = featureFormat(data_dict, features)
data = data.astype(np.float64, copy=False)
scaled_data = []
for i in range(data.shape[0]):
  if data[i][0] > 0 and data[i][1] > 0:
    scaled_data.append(data[i])
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(scaled_data)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

for point in scaled_data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
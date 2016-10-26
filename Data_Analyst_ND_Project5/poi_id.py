#!/usr/bin/python

import sys
import pickle
import numpy as np
import pandas as pd

from sklearn import neighbors
from sklearn.cross_validation import train_test_split

from tester import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

# You will need to use more features

### Load the dictionary containing the dataset
enron_data = pickle.load(open("final_project_dataset.pkl", "r"))

### Task 2: Remove outliers

# Delete the record 'TOTAL'
del enron_data['TOTAL']

# Replacing values in 2 rows in the dictionary
enron_data['BELFER ROBERT']['deferred_income'] = -102500
enron_data['BELFER ROBERT']['deferral_payments'] = 'NaN'
enron_data['BELFER ROBERT']['director_fees'] = 102500
enron_data['BELFER ROBERT']['expenses'] = 3285
enron_data['BELFER ROBERT']['total_payments'] = 3285
enron_data['BELFER ROBERT']['exercised_stock_options'] = 'NaN'
enron_data['BELFER ROBERT']['restricted_stock'] = 44093
enron_data['BELFER ROBERT']['restricted_stock_deferred'] = -44093
enron_data['BELFER ROBERT']['total_stock_value'] = 'NaN'

enron_data['BHATNAGAR SANJAY']['director_fees'] = 'NaN'
enron_data['BHATNAGAR SANJAY']['expenses'] = 137864
enron_data['BHATNAGAR SANJAY']['other'] = 'NaN'
enron_data['BHATNAGAR SANJAY']['total_payments'] = 137864
enron_data['BHATNAGAR SANJAY']['exercised_stock_options'] = 15456290
enron_data['BHATNAGAR SANJAY']['restricted_stock'] = 2604490
enron_data['BHATNAGAR SANJAY']['restricted_stock_deferred'] = -2604490
enron_data['BHATNAGAR SANJAY']['total_stock_value'] = 15456290

# Setup the final feature list
features_list05 = ['poi','salary', 'bonus', 'exercised_stock_options', 'deferred_income', 
                  'from_poi_to_this_person', 'from_this_person_to_poi', 'shared_receipt_with_poi']

### Store to my_dataset for easy export below.
my_dataset = enron_data

### Extract features and labels from dataset for local testing
data05 = featureFormat(my_dataset, features_list05, sort_keys = True)
labels05, features05 = targetFeatureSplit(data05)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

clf05 =  neighbors.KNeighborsClassifier()

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!

features_train05, features_test05, labels_train05, labels_test05 = \
    train_test_split(features05, labels05, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf05, my_dataset, features_list05)
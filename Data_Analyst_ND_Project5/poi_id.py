#!/usr/bin/python

import sys
import pickle
import numpy as np
import pandas as pd

from functools import partial

from sklearn.preprocessing import Imputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
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

# Function for reading dictionary as a dataframe 
def dict_to_dataframe(dictionary):

    df = pd.DataFrame.from_dict(dictionary).transpose()
    df.apply(partial(pd.to_numeric, errors='ignore'))

    df.reset_index(level=0, inplace=True)
    columns = list(df.columns)
    columns[0] = 'staff_name'
    df.columns = columns
    
    return(df)

enron_df = dict_to_dataframe(enron_data)

# Function for cleaning 'NaN' values with replacing
def column_with_npnan(column):
    data = []
    for value in column:
        if value == 'NaN':
            value = np.nan
        data.append(value)
    return np.array(data)

# Replace string NaN by np.nan
enron_df_np = enron_df.apply(column_with_npnan)

# Setup Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=1)

# Setup the finance feature list
finance_feature_list = ['bonus', 'deferral_payments', 'deferred_income', 
                        'director_fees', 'exercised_stock_options',
                        'expenses', 'loan_advances', 'long_term_incentive', 
                        'other', 'restricted_stock', 'restricted_stock_deferred', 
                        'salary', 'total_payments', 'total_stock_value']
# Setup variable for finance features after Imputer
finance_feature_imp = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]

# Transform data for finance features by Imputer
for i in range(len(finance_feature_list)):
    element = finance_feature_list[i]
    imp.fit([enron_df_np[element]])
    finance_feature_imp[i] = imp.transform([enron_df_np[element]])
    finance_feature_imp[i] = finance_feature_imp[i][0]

# New variables for transromed data
bonus_imp =  finance_feature_imp[0]
deferral_payments_imp = finance_feature_imp[1]
deferred_income_imp = finance_feature_imp[2]
director_fees_imp = finance_feature_imp[3]
exercised_stock_options_imp = finance_feature_imp[4]
expenses_imp = finance_feature_imp[5] 
loan_advances_imp = finance_feature_imp[6]
long_term_incentive_imp = finance_feature_imp[7]
other_imp = finance_feature_imp [8]
restricted_stock_imp = finance_feature_imp[9] 
restricted_stock_deferred_imp = finance_feature_imp[10]
salary_imp = finance_feature_imp[11]
total_payments_imp = finance_feature_imp[12]
total_stock_value_imp = finance_feature_imp[13]

# Setup the email feature list
email_feature_list = ['to_messages', 'from_poi_to_this_person', 'from_messages', 
                      'from_this_person_to_poi', 'shared_receipt_with_poi']

# Setup variable for email features after Imputer
email_feature_imp = [[0], [0], [0], [0], [0]]

# Transform data for email features by Imputer
for i in range(len(email_feature_list)):
    element = email_feature_list[i]
    imp.fit([enron_df_np[element]])
    email_feature_imp[i] = imp.transform([enron_df_np[element]])
    email_feature_imp[i] = email_feature_imp[i][0]

# New variables for transromed data
to_messages_imp =  email_feature_imp[0]
from_poi_to_this_person_imp = email_feature_imp[1]
from_messages_imp = email_feature_imp[2]
from_this_person_to_poi_imp = email_feature_imp[3]
shared_receipt_with_poi_imp = email_feature_imp[4] 

# Setup scaler
scaler = MinMaxScaler()

# Create a scaled dataframe
df0 = enron_df['staff_name']
df1 = pd.Series(scaler.fit_transform(bonus_imp), name = 'bonus')
df2 = pd.Series(scaler.fit_transform(deferral_payments_imp), name = 'deferral_payments')
df3 = pd.Series(scaler.fit_transform(deferred_income_imp), name = 'deferred_income')
df4 = pd.Series(scaler.fit_transform(director_fees_imp), name = 'director_fees')
df5 = pd.Series(scaler.fit_transform(exercised_stock_options_imp), name = 'exercised_stock_options')
df6 = pd.Series(scaler.fit_transform(expenses_imp), name = 'expenses')
df7 = pd.Series(scaler.fit_transform(loan_advances_imp), name = 'loan_advances')
df8 = pd.Series(scaler.fit_transform(long_term_incentive_imp), name = 'long_term_incentive')
df9 = pd.Series(scaler.fit_transform(other_imp), name = 'other')
df10 = enron_df['poi']
df11 = pd.Series(scaler.fit_transform(restricted_stock_imp), name = 'restricted_stock')
df12 = pd.Series(scaler.fit_transform(restricted_stock_deferred_imp), name = 'restricted_stock_deferred')
df13 = pd.Series(scaler.fit_transform(salary_imp), name = 'salary')
df14 = pd.Series(scaler.fit_transform(total_payments_imp), name = 'total_payments')
df15 = pd.Series(scaler.fit_transform(total_stock_value_imp), name = 'total_stock_value')
df16 = pd.Series(scaler.fit_transform(to_messages_imp), name = 'to_messages')
df17 = pd.Series(scaler.fit_transform(from_poi_to_this_person_imp), name = 'from_poi_to_this_person')
df18 = pd.Series(scaler.fit_transform(from_messages_imp), name = 'from_messages')
df19 = pd.Series(scaler.fit_transform(from_this_person_to_poi_imp), name = 'from_this_person_to_poi')
df20 = pd.Series(scaler.fit_transform(shared_receipt_with_poi_imp), name = 'shared_receipt_with_poi')
df21 = enron_df['email_address']

scaled_enron_df = pd.concat([df0, df1, df2, df3, df4, df5, df6, 
                             df7, df8, df9, df10, df11, df12, 
                             df13, df14, df15, df16, df17, df18,
                             df19, df20, df21], axis=1)

### Task 3: Create new feature(s)

# Create a dataframe for engineering
engineer_enron_df = pd.DataFrame(scaled_enron_df)

# Create new features
engineer_enron_df['coefficient_bonus_salary'] = 0.0
engineer_enron_df['coefficient_from_poi_all'] = 0.0
engineer_enron_df['coefficient_to_poi_all'] = 0.0

for i in range(len(scaled_enron_df['salary'])):
    if scaled_enron_df['salary'][i] > 0:
        engineer_enron_df['coefficient_bonus_salary'][i] = \
        1.0 * scaled_enron_df['bonus'][i] / scaled_enron_df['salary'][i]
for i in range(len(scaled_enron_df['to_messages'])):
    if scaled_enron_df['to_messages'][i] > 0:
        engineer_enron_df['coefficient_from_poi_all'][i] = \
        1.0 * scaled_enron_df['from_poi_to_this_person'][i] / scaled_enron_df['to_messages'][i]
for i in range(len(scaled_enron_df['from_messages'])):
    if scaled_enron_df['from_messages'][i] > 0:
        engineer_enron_df['coefficient_to_poi_all'][i] = \
        1.0 * scaled_enron_df['from_this_person_to_poi'][i] / scaled_enron_df['from_messages'][i]

# Reading the dataframe into a dictionary
engineer_enron_data = engineer_enron_df.to_dict(orient="index")

# Setup the final feature list
features_list06 = ['poi', 'coefficient_bonus_salary', 'coefficient_from_poi_all', 
                   'coefficient_to_poi_all', 'exercised_stock_options', 
                   'deferred_income', 'shared_receipt_with_poi']

### Store to my_dataset for easy export below.
my_dataset3 = engineer_enron_data

### Extract features and labels from dataset for local testing
data36 = featureFormat(my_dataset3, features_list06, sort_keys = True)
labels36, features36 = targetFeatureSplit(data36)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

clf11 =  DecisionTreeClassifier(max_depth=1)

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!

features_train36, features_test36, labels_train36, labels_test36 = \
    train_test_split(features36, labels36, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf11, my_dataset3, features_list06)
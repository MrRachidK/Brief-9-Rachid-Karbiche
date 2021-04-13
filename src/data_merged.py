# Import of all the libraries we'll need to work on the datasets

import pandas as pd
from functions import namestr

# Reading of the available datasets

properties_2016 = pd.read_csv('data/01_raw/properties_2016.csv')
train_2016 = pd.read_csv('data/01_raw/train_2016_v2.csv')

properties_2017 = pd.read_csv('data/01_raw/properties_2017.csv')
train_2017 = pd.read_csv('data/01_raw/train_2017.csv')

# Exploring the shape of the datasets

print('The dataset {} is composed by {} rows and {} columns'.format(namestr(properties_2016, globals()), properties_2016.shape[0], properties_2016.shape[1]))
print('The dataset {} is composed by {} rows and {} columns'.format(namestr(train_2016, globals()), train_2016.shape[0], train_2016.shape[1]))
print('The dataset {} is composed by {} rows and {} columns'.format(namestr(properties_2017, globals()), properties_2017.shape[0], properties_2017.shape[1]))
print('The dataset {} is composed by {} rows and {} columns'.format(namestr(train_2017, globals()), train_2017.shape[0], train_2017.shape[1]))

# Merging the datasets by year

data_2016 = pd.merge(train_2016, properties_2016, how = 'left', on = 'parcelid')
data_2017 = pd.merge(train_2017, properties_2017, how = 'left', on = 'parcelid')

print('The dataset {} is composed by {} rows and {} columns'.format(namestr(data_2016, globals()), data_2016.shape[0], data_2016.shape[1]))
print('The dataset {} is composed by {} rows and {} columns'.format(namestr(data_2017, globals()), data_2017.shape[0], data_2017.shape[1]))

# Concatenating of the two datasets

merged_data = pd.concat([data_2016, data_2017], axis = 0)

# Recording of a CSV file for the merged data

merged_data.to_csv('data/02_intermediate/merged_data.csv', index=False)
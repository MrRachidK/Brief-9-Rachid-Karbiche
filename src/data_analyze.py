# Import of all the libraries we'll need to work on the datasets

import pandas as pd
from functions import namestr, reduce_mem_usage

# Reading of the available datasets

data_2016_2017 = pd.read_csv('data/02_intermediate/merged_data.csv')
print(data_2016_2017.select_dtypes('object'))

# 1. Let's check the missing values

na_ratio = data_2016_2017.isna().sum().sort_values(ascending = False)/len(data_2016_2017)
print(na_ratio)

## Let's drop columns where the ratio of missing values is greater than 0.9

columns_to_drop = na_ratio[na_ratio>0.9].index.tolist()
print(data_2016_2017[columns_to_drop].dtypes)

## By looking to the list, we notice that, among the variables where the ratio of missing values is greater than 0.9, there are some categorical variables : fireplaceflag, hashottuborspa, taxdelinquencyflag. It means the missing values describe a 'None' status, so it can be useful. However, as for the float64-type variables, we can delete them. We can fill the missing values of these categorical variables with 'None'.

na_obj = data_2016_2017[columns_to_drop].select_dtypes('object').columns
data_2016_2017[na_obj] = data_2016_2017[na_obj].fillna('None')

## So, let's delete the float64-type variables with a ratio of missing values greater than 0.9 :

na_float = data_2016_2017[columns_to_drop].select_dtypes('float').columns 
data_2016_2017.drop(na_float, axis = 1, inplace = True)

print('The dataset {} is composed by {} rows and {} columns'.format(namestr(data_2016_2017, globals()), data_2016_2017.shape[0], data_2016_2017.shape[1]))

## Let's check more in-depth the missing values :

na_ratio = data_2016_2017.isna().sum().sort_values(ascending = False)/len(data_2016_2017)
na_cols = na_ratio[na_ratio>0].index
print(data_2016_2017[na_cols].dtypes)

## Let's harmonize our data by filling the missing values with 0 :

data_2016_2017[na_cols] = data_2016_2017[na_cols].fillna(0)

## Now, the remaining variables where there are missing values are object-type variables. 

na_ratio = data_2016_2017.isna().sum().sort_values(ascending = False)/len(data_2016_2017)
print(na_ratio[na_ratio>0])

## Let's check variables where there are only one unique value. We can't consider they are useful variables they will influence the 'logerror' variable :

one_col = data_2016_2017.columns[data_2016_2017.nunique()==1]
data_2016_2017.drop(one_col, axis = 1, inplace = True)

print('The dataset {} is composed by {} rows and {} columns'.format(namestr(data_2016_2017, globals()), data_2016_2017.shape[0], data_2016_2017.shape[1]))

# 2. Let's convert the types of our variables to reduce the memory of our dataset

data_2016_2017, NAlist = reduce_mem_usage(data_2016_2017)
print("_________________")
print("")
print("Warning: the following columns have missing values filled with 'df['column_name'].min() -1': ")
print("_________________")
print("")
print(NAlist)

# 3. Let's recuperate some datas from transaction date

data_2016_2017['transactiondate'] =  pd.to_datetime(data_2016_2017['transactiondate'], infer_datetime_format=True)
data_2016_2017['transaction_month'] = data_2016_2017['transactiondate'].dt.month
data_2016_2017['transaction_year'] = data_2016_2017['transactiondate'].dt.year

print(data_2016_2017.head())

print('The dataset {} is composed by {} rows and {} columns'.format(namestr(data_2016_2017, globals()), data_2016_2017.shape[0], data_2016_2017.shape[1]))

cleaned_data = data_2016_2017.to_csv('data/02_intermediate/cleaned_data.csv', index=False)
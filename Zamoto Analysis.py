# Zomato_Analysis

# Import Libraries
import pandas as pd
import numpy as np

# Loading .csv file of zomato data using pandas
df_data = pd.read_csv(r"C:\Users\goura\Documents\project data analysis\power bi project\Zomoto project\Zomato raw data\Zomato.csv")

# Loading excel file of country code using pandas
df_country = pd.read_excel(r"C:\Users\goura\Documents\project data analysis\power bi project\Zomoto project\Zomato raw data\Country-Code.xlsx")
print(df_country)


# Data Cleaning (Zomato data)
#check the datatype
df_data.info()

# Check the Null Values
print(df_data.isnull().sum())

# the top 5 rows of sales data
print(df_data.head(10))

# describe return description of the data in the DataFrame
print(df_data.describe())

# Check Duplicates
print(df_data.duplicated().sum())

# Columns Names
print(df_data.columns)

#check the datatype
print(df_data.dtypes)

print(df_data.shape)


# Now clean the Country Code Data

# View data of country code
print(df_country.head())

print(df_country.info)

print(df_country.shape)

# Checking null values
print(df_country.isnull().sum())

# Checking Duplicates
df_country.duplicated().sum()


# Merging country code and Data file)
df=pd.merge(df_data,df_country,on='Country Code', how= 'left')
print(df.head())


# Droping unwanted columns
df.drop(['Restaurant ID','Locality Verbose','Country Code','Longitude','Latitude'],axis=1,inplace=True)
print(df.columns)

# Checking the null values after merging
df.isnull().sum()

# Remove null values
df=df.dropna()
print(df.isnull().sum())

# Count total transcation happen in all the world
print(df.Country.value_counts())


# Downlaod data
print(df.to_string)
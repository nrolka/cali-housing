import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('California Housing Data Set (1990) by Nate Rolka')
housing = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
default = housing["median_house_value"].median()
housing_filter = st.slider('Median House Price', 0.0, 500001.0, default)  # min, max, default
housing = housing[housing.median_house_value >= housing_filter]

location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df["ocean_proximity"].unique(), 
     df["ocean_proximity"].unique())  
housing = housing[housing.ocean_proximity.isin(location_filter)]

income = st.sidebar.radio(
     "Choose income level",
     ('Low', 'Medium', 'High'))
if income == "Low":
    housing = housing[housing.median_income <= 2.5]
elif income == "Medium":
    housing = housing[housing.median_income <= 4.5]
elif income == "High":
    housing = housing[housing.median_income > 4.5]

# show on map
st.map(housing)

st.subheader('Histogram of the Median House Value')
fig = plt.figure(figsize=(20, 5))
housing_median = housing.groupby(["median_house_value"]).mean()
plt.hist(housing_median)
st.pyplot(fig)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data Set (1990) by Nate Rolka')
df = pd.read_csv('housing.csv')

housing_filter = st.slider('Median House Price', 0.0, 500001.0, 200000.0) 

location_filter = st.sidebar.multiselect(
     'Choose the location type',
    df.ocean_proximity.unique())

income = st.sidebar.radio(
     "Choose income level",
     ('Low', 'Medium', 'High'))

df = df[df.median_house_value <= housing_filter]
df = df[df.ocean_proximity.isin(location_filter)]

if income == "Low":
    df = df[df.median_income <= 2.5]
elif income == "Medium":
    df = df[(df.median_income > 2.5) & (df.median_income <= 4.5)]
elif income == "High":
    df = df[df.median_income > 4.5]

st.map(housing)

st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots()
df.median_house_value.hist(ax=ax,bins=30)
st.pyplot(fig)

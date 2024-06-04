import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Mapping of days
day_mapping = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}

# Hide the PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the dataset
dataset = pd.read_csv('main_data.csv')

# Set the dashboard title
st.title("Most Popular Day for User Groups")

# Group the data by weekday
weekday_group = dataset.groupby('weekday')
casual_users_by_day = weekday_group['casual'].sum()
registered_users_by_day = weekday_group['registered'].sum()

# Find the day with the maximum casual users
top_day_casual = casual_users_by_day.idxmax()

# Find the day with the maximum registered users
top_day_registered = registered_users_by_day.idxmax()

# User selection for the type of users
user_type_choice = st.selectbox('Select User Type', ['casual', 'registered'])

plt.figure(figsize=(10, 6))
if user_type_choice == 'casual':
    plt.title('Casual Users by Weekday')
    plt.bar(casual_users_by_day.index, casual_users_by_day.values)
    st.write("The most popular day for casual users is", day_mapping[top_day_casual])
else:
    plt.title('Registered Users by Weekday')
    plt.bar(registered_users_by_day.index, registered_users_by_day.values)
    st.write("The most popular day for registered users is", day_mapping[top_day_registered])

st.pyplot()

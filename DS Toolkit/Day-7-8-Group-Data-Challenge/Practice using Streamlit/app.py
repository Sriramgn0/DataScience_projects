#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:21:05 2019

@author: timothypillow
"""

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title("Tim's first app using Streamlit -  It's Lit! ")


st.title('Here is a table of twitter followers for political candidates')
df_mod = pd.DataFrame({'Total Followers': [66874041, 3491777 , 2314968,3952536,9995976,1543833]},
                      index=['realDonaldTrump', 'ewarren', 'MikeBloomberg','JoeBiden','BernieSanders','PeteButtigieg'])

st.dataframe(df_mod)

st.title('This is a map of 100 random points plotted over the Propulsion Academy')
map_data = pd.DataFrame(np.random.randn(100, 2) / [1000, 1000] + [47.390274, 8.515761],columns=['lat', 'lon'])

st.map(map_data)

st.title("Propulsion Academy is loacated in Zurich ")
from PIL import Image
image = Image.open('pa_logo.png')

st.image(image, caption='Propulsion Academy Logo',use_column_width=True)

from PIL import Image
image = Image.open('zurich.jpg')

st.image(image, caption='Zurich',use_column_width=True)



import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading data... done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)



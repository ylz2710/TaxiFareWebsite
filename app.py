import streamlit as st
import pandas as pd
import numpy as np
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

st.date_input('Enter date')
st.time_input('Enter time')
#st.text_input('Enter name of the location')
#st.text_input('Enter name of the destination')
st.number_input('pickup longitude')
st.number_input('pickup latitude')
st.number_input('dropoff longitude')
st.number_input('dropoff latitude')
st.number_input('passenger count')
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''



2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown
#     import requests 
#     params={"date and time",
#         "pickup longitude",
#         "pickup latitude",
#         "dropoff longitude",
#         "dropoff latitude",
#         "passenger count",
        
#     }
#     url="https://taxifare.lewagon.ai/predict"
#     response=requests.get(url, params=params)
#     response.json()
    
    

# below code is from Simone. Above commented code what I tried 
st.title("Welcome!")
st.title("🚕 Best price ever")
'''

'''


st.markdown('''#

### Please specify your request:
''')
st.markdown("***")
key = 42


st.markdown('''
### Date and time:
''')
d = st.date_input(
    "Choose a date for your drive",
    datetime.date(2021, 3, 12))
st.write('You chose:', d)

st.markdown('##')

t = st.time_input('Choose a time for your drive', datetime.time(8, 45))

date_time = datetime.datetime.combine(d,t).strftime("%Y-%m-%d %H:%M:%S UTC")

st.write('You chose', t)


st.markdown("***")


st.markdown('''
### Pickup and dropoff details:
''')

pickup_lon = st.number_input('Insert the pickup longitude')
st.write('Your pickup longitude is ', pickup_lon)

st.markdown('##')
pickup_lat = st.number_input('Insert the pickup latitude')
st.write('Your pickup latitude is ', pickup_lat)

st.markdown('##')
dropoff_lon = st.number_input('Insert the dropoff longitude')
st.write('Your dropoff longitude is ', dropoff_lon)

st.markdown('##')
dropoff_lat = st.number_input('Insert the dropoff latitude')
st.write('Your dropoff latitude is ', dropoff_lat)



st.markdown("***")

st.markdown('''### Number of passengers:''')
number_passengers = st.number_input('', min_value=1, max_value=10, value=1, step=1)
st.write('Your number of passengers is ', number_passengers)



url = 'http://taxifare.lewagon.ai/predict_fare/'
params = {'key': key,
          'pickup_datetime': date_time,
          'pickup_longitude': float(pickup_lon),
          'pickup_latitude': float(pickup_lat),
          'dropoff_longitude': float(dropoff_lon),
          'dropoff_latitude': float(dropoff_lat),
          'passenger_count': int(number_passengers)}

prediction = requests.get(url=url, params=params).json()
st.markdown("***")
#st.write('## Your predicted fare is', prediction['prediction'], "$")


st.write('## Your predicted fare:')
st.write('##', prediction['prediction'], "$")
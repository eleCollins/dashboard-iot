import streamlit as st
import requests
import pandas as pd
from api.sensor_ids import get_ids

st.title("Manage my Sensors 🧰")
st.divider()

st.subheader("Add a new sensor 🔧")
# Add sensor information
sensor_type = st.text_input(label="Add the sensor type")
unit = st.text_input(label="Add unit")
room_id = st.number_input(label="Add room id", min_value=int(1), max_value=int(100))
if st.button(label='Add sensor'):
    response_add_sensor = requests.post("http://127.0.0.1:8000/add-sensor", json={
        "type_": sensor_type,
        "unit": unit,
        "room_id": room_id
    })
    if response_add_sensor.status_code == 200:
        st.success("Sensor added!")
    else: 
        st.error(f"Failed to add sensor: {response_add_sensor.status_code}")

st.divider()
response_sensor = requests.get("http://127.0.0.1:8000/get-all-sensors")
# Fetch sensor information
st.subheader('Sensor Information 🧲')
if response_sensor.status_code == 200:
    sensor_data = response_sensor.json()
    df = pd.DataFrame(sensor_data)
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_sensor.status_code}")

st.divider()

st.write("Specify sensor ids to classify historical data")
st.write("This will help out to make your queries on our database")
get_ids()
if st.button(label="Send sensor IDs to filter information", key="ids"):
    st.divider()
    st.subheader("Ultrasonic Sensor")

    st.divider()
    st.subheader("Push Button")

    st.divider()
    st.subheader("IR Sensor")

    st.divider()
    st.subheader("Sound Sensor")
    response_sound = requests.get("http://127.0.0.1:8000/sound-sensor-logs")
    # Fetch sound sensor information
    if response_sound.status_code == 200:
        sound_data = response_sound.json()
        df = pd.DataFrame(sound_data)
        st.table(df)  
    else:
        st.error(f"Failed to fetch data: {response_sound.status_code}")

    st.divider()
    st.subheader("Magnetic Sensor")
else: 
    st.error("Error sendind IDs to query")
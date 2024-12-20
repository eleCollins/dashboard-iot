import streamlit as st
import requests
import pandas as pd

st.title("Manage my Sensors 🧰")
st.divider()

st.subheader("Add a new sensor 🔧")
# Add sensor information
sensor_type = st.text_input(label="Add the sensor type")
unit = st.text_input(label="Add unit")
room_id = st.number_input(label="Add room id", min_value=int(1), max_value=int(100))
if st.button(label='Add sensor'):
    response_add_sensor = requests.post("https://fast-api-reto.onrender.com/add-sensor", json={
        "type_": sensor_type,
        "unit": unit,
        "room_id": room_id
    })
    if response_add_sensor.status_code == 200:
        st.success("Sensor added!")
    else: 
        st.error(f"Failed to add sensor: {response_add_sensor.status_code}")

st.divider()
response_sensor = requests.get("https://fast-api-reto.onrender.com/get-all-sensors")
# Fetch sensor information
st.subheader('Sensor Information 🧲')
if response_sensor.status_code == 200:
    sensor_data = response_sensor.json()
    df = pd.DataFrame(sensor_data)
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_sensor.status_code}")

st.divider()
st.subheader("Ultrasonic Sensor")
response_ultrasonic = requests.get("https://fast-api-reto.onrender.com/get-ultrasonic-logs")
if response_ultrasonic.status_code == 200:
    ultrasonic_data = response_ultrasonic.json()
    df = pd.DataFrame(ultrasonic_data)
    df['date_'] = pd.to_datetime(df['date_'])
    st.line_chart(df.set_index('date_')['measure']) 
    st.table(df)
else:
    st.error(f"Failed to fetch data: {response_ultrasonic.status_code}")

st.divider()
st.subheader("Magnetic Sensor")
response_magnetic = requests.get("https://fast-api-reto.onrender.com/get-magnetic-logs")
if response_magnetic.status_code == 200:
    magnetic_data = response_magnetic.json()
    df = pd.DataFrame(magnetic_data)
    df['date_'] = df['date_'].str.replace('T', ' ')
    df['date_'] = pd.to_datetime(df['date_'])
    st.line_chart(df.set_index('date_')['measure']) 
    st.table(df)
    #df['date_'] = pd.to_datetime(df['date_'])
   # st.bar_chart(df.set_index('date_')['measure'])
    
else:
    st.error(f"Failed to fetch data: {response_magnetic.status_code}")

st.divider()
st.subheader("Push Button Sensor")
response_push = requests.get("https://fast-api-reto.onrender.com/get-push-logs")
if response_push.status_code == 200:
    push_data = response_push.json()
    df = pd.DataFrame(push_data)
    df['date_'] = df['date_'].str.replace('T', ' ')
    df['date_'] = pd.to_datetime(df['date_'])
    st.line_chart(df.set_index('date_')['measure'])
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_push.status_code}")

st.divider()
st.subheader("IR Sensor")
response_ir = requests.get("https://fast-api-reto.onrender.com/get-ir-logs")
if response_ir.status_code == 200:
    ir_data = response_ir.json()
    df = pd.DataFrame(ir_data)
    df['date_'] = pd.to_datetime(df['date_'])
    st.line_chart(df.set_index('date_')['measure'])
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_ir.status_code}")

st.divider()
st.subheader("Sound Sensor")
response_sound = requests.get("https://fast-api-reto.onrender.com/get-sound-logs")
if response_sound.status_code == 200:
    sound_data = response_sound.json()
    df = pd.DataFrame(sound_data)
    df['date_'] = df['date_'].str.replace('T', ' ')
    df['date_'] = pd.to_datetime(df['date_'])
    st.line_chart(df.set_index('date_')['measure'])
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_sound.status_code}")
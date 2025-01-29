import streamlit as st

st.title("Streamlit is amzanzing")

st.title("Hello world")

st.write("This is my first web app..")

number = st.slider("Pick a number",1,100)

st.write(f"You picked: {number}")

# My Plot of data

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)


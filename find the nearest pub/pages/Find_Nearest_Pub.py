import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# from matplotlib import image
# import plotly.express as px
# import os


# # absolute path to this file
# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# # absolute path to this file's root directory
# PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# # absolute path of directory_of_interest
# dir_of_interest = os.path.join(PARENT_DIR, "resources")

# IMAGE_PATH = os.path.join(dir_of_interest, "images", "pub_image.jpg")
# DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs_data_cleaned.csv")



st.set_page_config(
    page_title="Nearest Pub"
)

image = Image.open('pub.jpg')
st.image(image)

# img = image.imread(IMAGE_PATH)
# st.image(img)

st.header("DataSet: ")
df = pd.read_csv("open_pubs_data_cleaned.csv")
st.dataframe(df)
# df = pd.read_csv(DATA_PATH)
# st.dataframe(df)

# make header
st.header("5 Nearest Pubs from your Location")


lat = st.number_input('Latitude of Place')
lon = st.number_input('Longitude of Place')
button = st.button("Submit")
df_new = df[['latitude', 'longitude']]
new_points = np.array([lat, lon])
# Calculate distance between new_points and all points in df_new
distances = np.sqrt(np.sum((new_points - df_new)**2, axis = 1))


# sort the array using arg partition and keep n elements
n = 5
min_indices = np.argpartition(distances,n-1)[:n]
if button:
    st.text("Location based on below minimum distances : ")
    st.dataframe(df.iloc[min_indices])
    st.text("Minimum Distances :")
    st.dataframe(distances.head(5))
    st.map(df.iloc[min_indices])
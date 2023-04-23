import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# from matplotlib import image
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
st.header("Location of Bars in UK based on the Local Authority")
# enter either postal code or local authority

local_auth = st.selectbox('Local Authority of the Area', set(df['local_authority']))
button_1 = st.button("Submit")

if button_1:
    df_new = df.loc[(df['local_authority'] == local_auth)]
    st.text("Pubs in Region:")
    st.dataframe(df_new)
    st.map(df_new)
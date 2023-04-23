import streamlit as st
import pandas as pd
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
# DATA_PATH1 = os.path.join(dir_of_interest, "data1", "data_dictionary.xlsx")

# base="light"
# primaryColor="#bf1919"
# backgroundColor="#d8ce14"
# secondaryBackgroundColor="#44bb72"
# font="serif"

image = Image.open('pub.jpg')

# img = image.imread(IMAGE_PATH)

st.set_page_config(
    page_title="Home"
)
# make title and header
st.title("Open Pub Application")
st.image(image)
# st.image(img)
st.header("Introduction ")

# import the modified data
df = pd.read_csv("open_pubs_data_cleaned.csv")

st.text(''' Let’s assume you are on a vacation in the United Kingdom with your friends. 
For fun, you decided to go to the Pubs nearby for some drinks. Google Map is down because of 
some issues.
While searching the internet, you came across https://www.getthedata.com/open-pubs. 
On this website, you found all the pub locations (Specifically Latitude and 
Longitude info).
''')

st.header("Problem Statement ")

st.text(''' Create a web application with the data available in your hand. 
(Go through the requirements mentioned below) ''')

# df = pd.read_csv(DATA_PATH)
# st.dataframe(df)
# df=df.drop(df.columns['Unnamed:0'])

st.header("Available DataSet: ")

# print the data frame
st.dataframe(df)

st.header("DataSet Information")

ds = pd.read_excel("data_dictionary.xlsx")
st.dataframe(ds)

# ds = pd.read_excel(DATA_PATH1)
# st.dataframe(ds)

rows = df.count()[0]
columns = df.shape[1] - 1
st.subheader(f'Total Number of Rows in the data : {rows}')
st.subheader(f'Total Number of Columns in the data : {columns}')

st.header("Statistical Information of the DataSet :")
x = df.describe()
x

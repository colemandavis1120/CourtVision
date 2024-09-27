import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title='CourtVision',
                   layout="wide", 
                   page_icon="courtVisionLogoV1.png",
                   initial_sidebar_state="expanded")
col1, col2 = st.columns([6, 1])
with col1:
    st.title("CourtVision")
with col2:
    st.image("courtVisionLogoBlackV1.png", width=100)
st.markdown("___")
#################################################



advancedDatabase = 'advancedDatabase.xlsx'
averages = 'Averages'

df1 = pd.read_excel(advancedDatabase,
                   sheet_name=averages,
                   usecols='A:V',
                   header=1)


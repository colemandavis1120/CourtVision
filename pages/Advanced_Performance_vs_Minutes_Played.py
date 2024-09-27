import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title='Huntsville MBB Performance Analysis',
                   layout="wide", 
                   page_icon="whitelogo.png",
                   initial_sidebar_state="expanded")
col1, col2 = st.columns([6, 1])
with col1:
    st.title("Performance vs Minutes Played")
    st.header('2024-2025')
    st.markdown("""
    <style>
    .big-font {font-size:15px !important;}
</style>
""", unsafe_allow_html=True)
    
st.markdown('<p class="big-font">Analyze player performance compared to their playing time</p>', unsafe_allow_html=True)

with col2:
    st.image("whitelogo.png", width=175)
st.markdown("___")
###################################################


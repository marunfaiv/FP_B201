import streamlit as st
from loadStarter import loadStarter
from mainApp import mainApp

if 'runpage' not in st.session_state:
    st.session_state.runpage = loadStarter
    
if 'label' not in st.session_state:
    st.session_state.label = 0

st.session_state.runpage()

if (st.session_state.label == 0):
    st.session_state.label = 1
    st.session_state.runpage = mainApp
    st.session_state.runpage()
    st.experimental_rerun()
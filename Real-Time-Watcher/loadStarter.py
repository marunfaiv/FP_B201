import streamlit as st
import os
from PIL import Image
import numpy as np
import hydralit_components as hc
import time

def loadStarter():
    path = os.path.dirname(__file__)
    my_file = path+'/Real-Time Watcher (Loading Logo).png'
    image = np.array(Image.open(my_file))
    with st.container():
        st.image(image)
    with hc.HyLoader(' ',hc.Loaders.standard_loaders,index=3):
        time.sleep(10)    
        

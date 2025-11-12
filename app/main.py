import streamlit as st
import pandas as pd
from app.utils import load_data,get_summary_stats
st.title("Solar Resource Dashboard")
st.write("welcome to the solar resource analysis Dashboard")
data=load_data("Benin")
print(data.head())
summary=get_summary_stats(data)
print(summary)






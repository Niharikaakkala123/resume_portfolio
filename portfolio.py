import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import image

st.title(":black[Niharika Akkala] :smile:")

st.header(":red[Data Scientist]")

tab1, tab2, tab3,tab4,tab5 = st.tabs(["About Me","Projects","Skills","Education","Contact"])
with tab1:
    st.markdown("Data Science Intern at Innomatics Research Labs")
    st.markdown("I am a self-motivated and hardworking person")

with tab2:
    st.markdown("Web scrapping")
    st.markdown("Machine learning")
    st.markdown("Natural Language Processing-NLP")
    st.markdown("Flask")

with tab3:
    st.markdown("Python")
    st.markdown("Data Analysis")
    st.markdown("Machine Learning")
    st.markdown("HTML")
    st.markdown("SQL")

with tab4:
    st.markdown("B-Tech : Ace Engineering College")
    st.markdown("Intermediate : Sri Vedha Junior College")
    st.markdown("SSC : Sadhana High School")

with tab5:
    st.caption("Linkedin--https://www.linkedin.com/in/niharika-akkala-15696b256?")
    st.caption("Github--https://github.com/Niharikaakkala123")


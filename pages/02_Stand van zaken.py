import streamlit as st
import pandas as pd
import folium
import numpy as np
from streamlit_folium import st_folium

st.set_page_config(page_title=None, page_icon=None, initial_sidebar_state="auto", menu_items=None, layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFFFFF;  /* Replace with your desired color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
            <style>
            [data-testid="stSidebar"] {
                display: none
            }

            [data-testid="collapsedControl"] {
                display: none
            }
            </style>
            """, unsafe_allow_html=True)


st.markdown("""
    <style>
        [data-testid="column"]:nth-child(1){
            background-color: #a2cce9;
            font-size: 20px;
        }
    </style>
    """, unsafe_allow_html=True
)

col2, col3, col4, = st.columns([1.5,5,2])
with col2:
    st.markdown('#')
    st.page_link("pages/01_Start.py", label="### **Start**", )
    st.page_link("pages/02_Stand van zaken.py", label="### **Stand van zaken**")
    st.page_link("pages/03_Q&A.py", label="### **Q&A**")

with col3:
    st.title("Stand van zaken")
    
    st.markdown("Momenteel zijn er 500 laadpalen actief met netbewust.")
    st.markdown("Het project is in juni 2024 gelanceerd. Zie het persbericht rondom de lancering.", unsafe_allow_html=True)
    st.markdown(f''' <a href = "https://www.liander.nl/over-ons/nieuws/2024/equans-en-liander-gaan-in-amsterdam-netbewust-laden-uitbreiden-naar-1000-laadpalen"> Link </a>''', unsafe_allow_html=True)
    
    st.subheader("Welke laadpalen doen mee aan netbewust laden")
    
    st.markdown("In onderstaande kaart kunt u zien welke laadpalen meedoen aan netbewust laden en welke laadpalen meedoen aan het programma Actief Slim laden", unsafe_allow_html=True)
    
    
    # Make an empty map
    
    data = pd.read_csv("pages/Locaties.csv", sep=";")
    m = folium.Map(location=[data.iloc[1]['Latitude'], data.iloc[1]['Longitude']], tiles="OpenStreetMap", zoom_start=10)
    #st.dataframe(data)
    data["colour"] = np.where(data["District"] == "Zuid", "Blue", "Red")
    radius = 12
    for i in range(0,len(data)):
        folium.CircleMarker(
        location=[data.iloc[i]['Latitude'], data.iloc[i]['Longitude']],
        radius=radius,
        fill=True,
        fill_opacity=1,
        color=data.iloc[i]['colour'],
        popup=data.iloc[i]['Address'],
           
       ).add_to(m)
    
    st_folium(m, width=750, height=300)

with col4:
    st.markdown('#')
####Design footer        
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<img src="https://www.theleansixsigmacompany.eu/wp-content/uploads/sites/30/equans-logo.png", height=80>
<img src="https://www.liander.nl/assets/logo.png", height=80>
<img src="https://upload.wikimedia.org/wikipedia/commons/4/4c/Logo_of_Gemeente_Amsterdam.svg", height=80>
<img src="https://zakelijkschrijven.nl/wp-content/uploads/2021/01/HvA-logo.png", height=80>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)        
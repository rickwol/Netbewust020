import streamlit as st
from time import sleep
from st_pages import Page, add_page_title


st.set_page_config(page_title=None, page_icon=None, initial_sidebar_state="collapsed", menu_items=None, layout="wide")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
    .reportview-container .main .block-container{{f"max-width: 1000px;"
    }}

</style>
""",
    unsafe_allow_html=True,
)

st.title("Login Netbewustladen")

st.write("Please log in to continue")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "slimladen" and password == "Netbewust020!":
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/01_Start.py")
    else:
        st.error("Incorrect username or password")


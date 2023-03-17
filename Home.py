import streamlit as st
from PIL import Image
import os

# import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns
import streamlit as st
from django.core.wsgi import get_wsgi_application
# from sklearn.cluster import KMeans

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

from django.contrib.auth import authenticate


def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        user = authenticate(
            username=st.session_state["username"], password=st.session_state["password"]
        )

        if user is not None:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True
if check_password():

    im = Image.open("image.ico")
    st.set_page_config(
        page_title="Tork Analytics",
        page_icon=im,
    )
    st.title("Customer's Behaviour with Kratos")
    st.write(
        """Here I am going to represent my findings with the Telematics historical data.
    It would helpful in finding the customer's behaviour Insight and will helpful in planing accordingly"""
    )
    st.markdown(
        """
        ### 💾 Index:
        **Page**|**Description**
        -----|-----
        |Charging Insight| Insights about when customer chargeIn and chargeOut|
        |Distance per Day| Average Distance Travelled per day|
        """
    )
    st.text("")
    st.markdown(
        """
            ### 💪 Challenge:
            ##### Here I am creating a report to summarizing my research including:
            - Avg charging time taken by customers for full charge in Pune, Mumbai, Nashik and Aurangabad (separate for each city)
            - Are customers charging full (i.e. say from 5% to 100%) or only incremental charging every time (i.e. say from 25% to 80%)
            - What time of the day the charging takes place (are people charging the most during day or nighttime?)
            - Avg daily k.m. run of customers in Pune, Mumbai, Nashik and Aurangabad (separate for each city)
            - Highest k.m. run so far in single charge in Pune, Mumbai, Nashik and Aurangabad (separate for each city)
            """
    )

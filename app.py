# test
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st

st.write("hello world")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

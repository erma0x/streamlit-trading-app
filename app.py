import pandas as pd
import streamlit as st
import statsmodels.api as sm
import numpy as np
import scipy as sp
from scipy import stats

st.title('The Hodrick–Prescott filter for Fintech')

description = """
Seasonality decomposition in time series analysis with Hodrick–Prescott filter.
The Hodrick–Prescott filter is a mathematical tool used in macroeconomics, 
especially in real business cycle theory, to remove the cyclical component 
of a time series from raw data. It is used to obtain a smoothed-curve representation
of a time series, one that is more sensitive to long-term than to short-term fluctuations.

Hodrick Prescott Filter does Time series decomposition which involves separating 
a time series into several distinct components(Cycle component and Trend Component).  
And this filter looks like it can be applied to any time-series data especially with stock prices 
to understand the underlying trend and the cycle involved in it. 

The HP filter is one of the most widely used tools in macroeconomic analysis.
It tends to have favorable results if the noise is distributed normally,
and when the analysis being conducted is historical.
According to a paper published by economist and professor James Hamilton—which
appears on the National Bureau of Economic Research website—there are several reasons why
the HP filter should not be used. Hamilton first proposes that the filer produces outcomes
that have no basis in the process of generating data. He also states that the values
that are filtered at the sample's end are totally different from those in the middle. 

"""

st.write(description)

datasets_available  = ("Microsoft MSFT - adjusted close price - daily - 2017-01-03 to 2021-09-10",
                       "(Test) Apple APPL")

choosen_ticker = st.radio(label='Datesets avaiable:', options=datasets_available)

def app():
    if  'Microsoft' in choosen_ticker:
        
        df = pd.read_csv('MSFT.csv')
        
        st.write('Microsoft (MSFT) dataset (first 5 rows)')
        st.write(df.head())
        
        st.write('Microsoft daily adjusted close price ')
        st.line_chart(df['Adj Close'])

        # PRICE DECOMPOSITION
        data_cycle, data_trend = sm.tsa.filters.hpfilter(df['Adj Close'])
        
        st.write("Mircosoft data cycle with HP filter")
        st.area_chart(data_cycle)
        
        st.write("Microsoft data trend with HP filter")
        st.line_chart(data_trend)
        
        st.write("Microsoft daily return")
        st.line_chart(df['daily_return'])
        
        ## generate the data and plot it for an ideal normal curve
        st.write("Microsoft daily return mean ",df['daily_return'].mean())
        st.write("Microsoft daily return standard deviation ",df['daily_return'].std())

    else:
        st.write("Sorry, we could't solve your request")

app()
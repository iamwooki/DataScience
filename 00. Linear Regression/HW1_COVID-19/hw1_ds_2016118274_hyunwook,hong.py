# -*- coding: utf-8 -*-
"""HW1_DS_2016118274_HyunWook,Hong.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pVv9TA3d3n6QeMWlujl6y3tCGx_DgYpn

Data Science<br>
CSE 2016118274 HyunWook, Hong
"""

# Commented out IPython magic to ensure Python compatibility.
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta,date
from scipy import stats
from scipy.optimize import curve_fit

from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima_model import ARIMA
from random import random

import seaborn as sns
import matplotlib.pyplot as plt
import gc
import fbprophet


# %config InlineBackend.figure_format = 'retina'

plt.rc("font", family="AppleGothic")
plt.rc('axes', unicode_minus=False)

df_covid19 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv")
df_covid19.index=df_covid19["Country_Region"]
df_covid19.head()

df_covid19.sort_values(by="Confirmed", ascending=False )

f = plt.figure(figsize=(10,5))
f.add_subplot(111)

plt.axes(axisbelow=True)
plt.barh(df_covid19.sort_values('Confirmed')["Confirmed"].index[-10:],df_covid19.sort_values('Confirmed')["Confirmed"].values[-10:],color="darkcyan")
plt.tick_params(size=5,labelsize = 13)
plt.xlabel("Confirmed Cases",fontsize=15)
plt.ylabel("Countries",fontsize=15)
plt.title("Figure.1 COVID-19 Top 10 Countries (Confirmed Cases)",fontsize=20)
plt.grid(alpha=0.5)
plt.show()

from google.colab import files

upload = files.upload()



features = ['Province_State','Country_Region','Date','ConfirmedCases','Fatalities']
df=pd.read_csv("train.csv",usecols=features)
df.fillna(' ',inplace=True)
df['Lat']=df['Province_State']+df['Country_Region']
top10=df
df['ConfirmedCases_cum'] = df.groupby(['Country_Region','Date'])['ConfirmedCases'].transform(pd.Series.sum)
top10 = df.groupby(['Country_Region']).agg({ 'Country_Region':'min','ConfirmedCases': 'sum'})
countries_list=df.Lat.unique()

top10Countries = top10.sort_values(['ConfirmedCases'],ascending=False)['Country_Region'].head(10).to_numpy()
display(top10Countries)

sns.set() 
df_top=df.loc[df['Country_Region'].isin(top10Countries)]
df_top=df_top.drop('Lat',axis=1 )
plt.figure(figsize=(16, 6))
sns.set_style("whitegrid")
ax = sns.lineplot(x="Date", y="ConfirmedCases_cum", hue="Country_Region",
                   estimator=None, lw=1, 
                  data=df_top, #df[df["Country"Reigon"]=="US"]
                  marker='o',markersize=8,linewidth=2)
ax.set_title("Figure2.")
plt.draw()
ax.set_xticklabels(ax.get_xticklabels(), rotation=75, ha='right')

df_us = pd.read_csv('us_states_covid19_daily.csv')
df_us.head()

df_cleaning = df_us.copy()

df_cleaning['date'] = df_cleaning['date'].apply(lambda x: datetime.strptime(str(x), '%Y%m%d'))

df_cleaning = df_cleaning.rename(columns={'total':'total_tests_inc_pending', 
                                          'totalTestResults':'total_tests', 
                                          'death':'deaths'})
df_cleaning = df_cleaning.drop(columns=['dateChecked',
                                        'hash',
                                        'fips', 
                                        'deathIncrease',
                                        'hospitalizedIncrease',
                                        'negativeIncrease',
                                        'positiveIncrease',
                                        'totalTestResultsIncrease'])

state_dict = {}
for state in df_cleaning.state.unique():
    state_df = df_cleaning[df_cleaning['state']==state].copy()
    state_df = state_df.sort_values(by='date', ascending=True)
    state_df = state_df.reset_index(drop=True)
    state_df.loc[0] = state_df.loc[0].fillna(0)
    state_df.index = state_df.index + 1
    state_df = state_df.fillna(method='ffill')
    state_dict[state] = state_df
    
df = pd.DataFrame()
for state_df in state_dict.values():
    df = pd.concat([df, state_df])
df= df.reset_index()

def format_plot(fig):
    plt.xlabel('Data')
    plt.xticks(rotation=45)
    plt.legend(loc='upper left', fontsize='large')
  
def best_and_worst(df, rank_on, y_label, states_per_plot=5, more_is_worse=True):
    most_recent_day = df.date.max()
    if more_is_worse:
        ranked = df[df['date']==most_recent_day].sort_values(by=rank_on, ascending=False)
    else:
        ranked = df[df['date']==most_recent_day].sort_values(by=rank_on, ascending=True)
    worst = ranked.head(states_per_plot).state
    best = ranked.tail(states_per_plot).state

    fig=plt.figure(figsize=(20,5))
    plt.subplot(1, 2, 1)
    for state in worst:
        state_df = df[df['state']== state].copy()
        plt.plot(state_df.date, state_df[rank_on], label=state)
        plt.title('Worst States')
        plt.ylabel(y_label)
        format_plot(fig)
    plt.subplot(1, 2, 2)
    for state in best:
        state_df = df[df['state']== state].copy()
        plt.plot(state_df.date, state_df[rank_on], label=state)
        plt.title('Best States')
        plt.ylabel(y_label)
        format_plot(fig)
        
    plt.show()

best_and_worst(df=df, rank_on='positive', y_label='Number of Positive Cases')

def get_lin_exp_fits(state_df, col='positive'):
    #linear regression
    linear_coeffs = stats.linregress(x=state_df.index, y=state_df[col])
    positive_values = state_df[col]>0
    #exp regression
    exp_coeffs = stats.linregress(x=state_df.index[positive_values], y=np.log(state_df.loc[positive_values, col]))
    return linear_coeffs, exp_coeffs

def plot_lin_vs_exp(state_df, col='positive', y_label='Number of Positive Cases'):
    linear_coeffs, exp_coeffs = get_lin_exp_fits(state_df, col=col)
    
    # Plot the results.
    fig=plt.figure(figsize=(20,5))
    plt.subplot(1, 3, 1)
    plt.plot(state_df.date, state_df[col], label="NY")
    plt.plot(state_df.date,  linear_coeffs[1] + state_df.index*linear_coeffs[0], label="linear prediction")
    plt.title('Figure4. Linear Regression')
    plt.ylabel(y_label)
    format_plot(fig)
    plt.subplot(1, 3, 2)
    plt.plot(state_df.date, state_df[col], label="NY")
    plt.plot(state_df.date,  np.exp(exp_coeffs[1])  * (np.exp(exp_coeffs[0])**state_df.index), label="exp prediction")
    plt.title('Exponential Regression')
    plt.ylabel(y_label)
    format_plot(fig)

plot_lin_vs_exp(state_df=state_dict["NY"])
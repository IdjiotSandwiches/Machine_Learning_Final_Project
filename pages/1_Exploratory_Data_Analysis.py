import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import mpld3 
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import math

st.set_page_config(
	page_title="Exploratory Data Analysis",
	layout='wide'
)

#@st.cache
def load_data():
   csv = pd.read_csv('dataset/german.csv', sep=';')
   return csv

def description():
   st.info(
      f'''
         When a bank receives a loan application, based on the applicants profile the bank has to make a decision regarding whether to go ahead with the loan approval or not. Two types of risks are associated with the banks decision
         - If the applicant is a good credit risk, i.e. is likely to repay the loan, then not approving the loan to the person results in a loss of business to the bank
         - If the applicant is a bad credit risk, i.e. is not likely to repay the loan, then approving the loan to the person results in a financial loss to the bank
      ''', icon='ℹ️'
   )
   st.write('For futher information visit:')
   if st.button('Dataset Encoding'):
      st.switch_page('pages/2_Description_Page.py')
    
def preview(df):
   st.write('**Desciptive Analysis**')
   st.dataframe(df.head())
    
def desciptive(df):
   st.write('**Desciptive Analysis**')  
   st.write(df.describe())
   st.divider()

def histogram(df):
   columns = df.columns.tolist()
   plot_all = st.checkbox("Plot all columns for histogram")
    
   if plot_all:
      fig = make_subplots(rows=5, cols=5, subplot_titles=columns)
      for i, column in enumerate(columns):
         row = i // 5 + 1
         col = i % 5 + 1
         fig.add_trace(
            go.Histogram(
               x=df[column], 
               name=column,
            ),
            row=row, 
            col=col,
         )

      fig.update_layout(
         title_text="Histograms for all",
         height=400*5,
         showlegend=False,
         bargap=0.2,
         xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickformat='d')
      )
   else:
      select_col = st.selectbox("Select a Column for Histogram", columns)
      if select_col:
         fig = px.histogram(
            df[select_col], 
            x=select_col,
            title=f'Histogram for {select_col}',
            color_discrete_sequence=['rgb(158, 185, 243)'],
         )
         fig.update_layout(
            bargap=0.2, 
            height=800,
            xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickformat='d')
         )

   st.plotly_chart(fig, theme="streamlit")
   st.divider()

def correlation(df):
   corr = df.corr()
   fig = px.imshow(
      corr, 
      text_auto=True,
      title='Correlation Matrix',
      aspect='auto',
   )
   fig.update_layout(
      height=1200,
      coloraxis_colorscale='plasma'
   )
   st.plotly_chart(fig, theme="streamlit")
   st.divider()
   
    
def box_plot(df):
   st.write("Box Plot")
   columns = df.columns.tolist()
   plot_all = st.checkbox("Plot all columns for box plot")
    
   if plot_all:
      fig = px.box(
            df, 
            title='Box Plot for all'
      )
      fig.update_layout(
         height=800,
      )
   else:
      select_col = st.selectbox("Select a Column for Box Plot", columns)
      if select_col:
         fig = px.box(
            df, 
            y=select_col,
            title=f'Box Plot for {select_col}'
         )
         fig.update_layout(
            height=800,
         )
   st.plotly_chart(fig, theme="streamlit")
    
def main():
   st.title('Explatory Data Analysis')
   df = load_data()
   description()
   preview(df)
   desciptive(df)
   histogram(df)
   correlation(df)
   box_plot(df)
    
if __name__ == '__main__':
	main()
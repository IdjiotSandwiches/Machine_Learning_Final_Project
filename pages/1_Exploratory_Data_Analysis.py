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
   desc = '''
   When a bank receives a loan application, based on the applicants profile the bank has to make a decision regarding whether to go ahead with the loan approval or not. Two types of risks are associated with the banks decision
   '''
   st.markdown(desc)
   risk ='''
   - If the applicant is a good credit risk, i.e. is likely to repay the loan, then not approving the loan to the person results in a loss of business to the bank
   '''
   st.markdown(risk)
   risk_2 ='''
   - If the applicant is a bad credit risk, i.e. is not likely to repay the loan, then approving the loan to the person results in a financial loss to the bank
   '''
   st.markdown(risk_2)
   st.markdown("For futher information visit:")
   if st.button('Dataset Encoding'):
      st.switch_page('pages/2_Description_Page.py')
    
def preview(df):
   st.write('Desciptive Analysis')
   st.dataframe(df.head())
    
def desciptive(df):
   st.write('Desciptive Analysis')  
   st.write(df.describe())

def histogram(df):
   columns = df.columns.tolist()
   plot_all = st.checkbox("Plot all columns for histogram")
    
   if plot_all:
      # st.write(f"Histogram for all")
      # fig,ax = plt.subplots(figsize=(18, 18))
      # df[columns].hist(ax=ax)
      # st.pyplot(fig)

      fig = make_subplots(rows=5, cols=5, subplot_titles=columns)
      for i, column in enumerate(columns):
         row = i // 5 + 1
         col = i % 5 + 1
         fig.add_trace(
            go.Histogram(
               x=df[column] if (column == 'Credit_Amount' or column == 'Duration_of_Credit_monthly' or column == 'Age_years') else df[column].sort_values().astype(str), 
               name=column,
            ),
            row=row, 
            col=col,
         )

      fig.update_layout(
         title_text="Histograms for all",
         height=400*5,
         showlegend=False,
         bargap=0.2
      )
      st.plotly_chart(fig, theme="streamlit")
   else:
      select_col = st.selectbox("Select a Column for Histogram", columns)
      if select_col:
         # st.write(f'Histogram for {select_col}')
         # fig, ax = plt.subplots()
         # df[select_col].hist(ax=ax)
         
         fig = px.histogram(
            df[select_col] if (select_col == 'Credit_Amount' or select_col == 'Duration_of_Credit_monthly' or select_col == 'Age_years') else df[select_col].sort_values().astype(str), 
            x=select_col,
            title=f'Histogram for {select_col}',
            color_discrete_sequence=['rgb(158, 185, 243)'],
         )
         fig.update_layout(
            bargap=0.2, 
            height=800
         )
         st.plotly_chart(fig, theme="streamlit")
             
         # fig_html = mpld3.fig_to_html(fig)
         # components.html(fig_html, height=600)

def correlation(df):
   st.write('Correlation Matrix')
   corr = df.corr()
   # fig, ax = plt.subplots(figsize=(12, 12))
   # sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
   # st.pyplot(fig)

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
    
def box_plot(df):
   st.write("Box Plot")
   column = df.columns.tolist()
   plot_all = st.checkbox("Plot all columns for box plot")
    
   if plot_all:
      st.write(f"Box Plot for all")
      fig, ax = plt.subplots(figsize=(18, 18))
      sns.boxplot(data=df, ax=ax)
      st.pyplot(fig)
   else:
      select_col = st.selectbox("Select a Column for Box Plot", column)
      if select_col:
         st.write(f"Box Plot for {select_col}")
         fig, ax = plt.subplots(figsize=(12, 12))
         sns.boxplot(data=df, y=select_col, ax=ax)
            
         fig_html = mpld3.fig_to_html(fig)
         components.html(fig_html, height=1080)
    
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
import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
	page_title="Home",
	layout="wide"
)

def load_data():
	if 'df' not in st.session_state:
		st.session_state.df = pd.read_csv('dataset/german.csv', sep=';')

def main():
	load_data()
	st.title('Machine Learning Project')
	st.write('Member:')
	st.markdown("""
		1. 2602063913 - Bernardus Ignasio
		2. 2602070093 - Evan Somangkey
		3. 2602082452 - Rendy Susanto
		4. 2602071291 - Theo Deannata Harjanto
		5. 2602063421 - Vincen		 
	""")

	if st.button('Explore the Data? ➤'):
		st.switch_page('pages/1_Exploratory_Data_Analysis.py')
    
	if st.button('Use Demo ➤'):
		st.switch_page('pages/5_Prediction_Demo.py')

if __name__ == '__main__':
	main()

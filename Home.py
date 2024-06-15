import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
	page_title="Home",
	layout="wide"
)

def main():
	st.title('Machine Learning Project')
	st.write('Member:')
	st.markdown("""
		1. Theo
		2. Ignas
		3. Rendy
		4. Evan
		5. Vincen		 
	""")

	if st.button('Explore the Data?'):
		st.switch_page('pages/1_Exploratory_Data_Analysis.py')
	if st.button('Use Demo'):
		st.switch_page('pages/2_Prediction_Demo.py')

main()
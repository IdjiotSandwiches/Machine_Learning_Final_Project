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

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 55984ea558587e1eb662bd78074fcf6f1c3ae5a7
	if st.button('Explore the Data?'):
		st.switch_page('pages/1_Exploratory_Data_Analysis.py')
	if st.button('Use Demo'):
		st.switch_page('pages/2_Prediction_Demo.py')

<<<<<<< HEAD
=======
>>>>>>> 1d3ec723eac47e244b6228e6d96167f4455457de
=======
>>>>>>> 55984ea558587e1eb662bd78074fcf6f1c3ae5a7

main()
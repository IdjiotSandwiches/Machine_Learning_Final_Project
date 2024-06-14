import pandas as pd
import numpy as np
import streamlit as st
from sklearn.utils import resample, shuffle

st.set_page_config(
	page_title="Preparing the data",
	layout="wide"
)

class DataPreprocessing:
	def __init__(self, df):
		self.df = df
		
	def drop_na(self):
		self.df.dropna(inplace=True)

	def resampling(self):
		credible = self.df[self.df['Creditability'] == 1]
		non_credible = self.df[self.df['Creditability'] == 0]

		non_credible = resample(
			non_credible, 
			replace=True,
			n_samples=len(credible),
			random_state=42
		)
		self.df = pd.concat([credible, non_credible])
	
	def shuffle(self):
		self.df = shuffle(self.df)

@st.cache_data
def load_data():
	return st.session_state.df

def main():
	data = DataPreprocessing(load_data())
	st.header('Data preprocessing:')
	drop_na(data)
	resampling_data(data)
	shuffle_data(data)
	
	if 'prep_data' not in st.session_state:
		st.session_state.prep_data = data

def drop_na(data):
	st.write('1. Drop NULL value')
	if st.button('Click to drop NULL value'):
		st.spinner('Dropping NULL value...')
		data.drop_na()
		st.success('NULL value dropped!!')

def resampling_data(data):
	st.write('2. Resampling')
	if st.button('Click to resampling data'):
		st.spinner('Resampling data...')
		data.resampling()
		st.success('Resampling data success!!')

def shuffle_data(data):
	st.write('3. Shuffle')
	if st.button('Click to shuffle data'):
		st.spinner('Shuffling data...')
		data.shuffle()
		st.success('Shuffling data success!!')

if __name__ == '__main__':
	main()

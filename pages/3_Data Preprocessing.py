import time
import pandas as pd
import streamlit as st
from sklearn.utils import resample, shuffle

class DataPreprocessing:
	def __init__(self, file_path):
		self.file_path = file_path
		self.df = None
		
	def load_data(self):
		self.df = pd.read_csv(self.file_path, sep=';')

	def drop_na(self):
		self.df.dropna(inplace=True)
	def mean_na(self):
		column_means = self.df.mean()
		self.df.fillna(column_means, inplace=True)

	def resampling(self):
		credible = self.df[self.df['Creditability'] == 1]
		non_credible = self.df[self.df['Creditability'] == 0]

		non_credible = resample(
			non_credible, 
			replace=True,
			n_samples=max(len(credible), len(non_credible)),
			random_state=42
		)
		self.df = pd.concat([credible, non_credible])
	
	def shuffle(self):
		self.df = shuffle(self.df)
  
def data_preprocessing(file_path, null_handle, resample, shuffle):
   data_prep = DataPreprocessing(file_path=file_path)
   data_prep.load_data()
   if null_handle == "Drop":
      data_prep.drop_na()
   else:
      data_prep.mean_na()
   if resample==True:
      data_prep.resampling()
   if shuffle==True:
      data_prep.shuffle()
	
   return data_prep

def form_preprocessing():
   with st.form("preprocessing"):
      #   null_handle = st.selectbox("NA Handle", ["Drop", "Mean"], index=0)
      null_handle = st.radio("NA Handle", ["Drop", "Mean"], index=0, horizontal=True)
      resample = st.toggle("Resample")
      shuffle = st.toggle("Shuffle")
      if st.form_submit_button("Submit"):
         dp = data_preprocessing("dataset/german.csv", null_handle, resample, shuffle)
         st.success("Data Preprocessing Success")
         st.session_state["data_preprocessing"] = dp
         time.sleep(1)
         st.switch_page('pages/4_Train_Your_Model.py')

st.set_page_config(
	page_title="Data Preprocessing",
	layout="wide"
)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Training Model')

df = form_preprocessing()


        
            

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
  
def data_preprocessing(data_prep, null_handle, resample, shuffle):
   if null_handle == "Drop":
      data_prep.drop_na()
   else:
      data_prep.mean_na()
   if resample==True:
      data_prep.resampling()
   if shuffle==True:
      data_prep.shuffle()
	
   return data_prep

def df_info(df):
   df_info = pd.DataFrame({
      'Creditability': ['Not Eligible', 'Eligible'],
      'Count': df['Creditability'].groupby(df['Creditability']).count()
	})
   df_null = df.isnull().sum()
   df_null.name = 'Null Count'
   tab_1, tab_2, tab_3 = st.tabs(['Data count', 'Data preview', 'Data null'])
   with tab_1:
      st.dataframe(df_info, hide_index=True)
   with tab_2:
      st.dataframe(df.head(), hide_index=True)
   with tab_3:
      st.dataframe(df_null)

def form_preprocessing():
   data_prep = DataPreprocessing(file_path="dataset/german.csv")
   data_prep.load_data()
   st.header('Raw data')
   df_info(data_prep.df)
   st.header('Choose your own data handling method')
   with st.form("preprocessing"):
      st.info('Recommended to resampling data because data not balanced!', icon='ℹ')
      null_handle = st.radio("Null value handling", ["Drop", "Mean"], index=0, horizontal=True)
      resample = st.toggle("Resample")
      shuffle = st.toggle("Shuffle")
      if st.form_submit_button('Submit'):
         dp = data_preprocessing(data_prep, null_handle, resample, shuffle)
         st.success("Data Preprocessing Success")
         st.header('Preprocessed Data')
         df_info(dp.df)
         st.session_state["data_preprocessing"] = dp
   
   if 'data_preprocessing' in st.session_state:
      if st.button('Train your model'):
         st.switch_page('pages/4_Train_Your_Model.py')

st.set_page_config(
	page_title="Data Preprocessing",
	layout="wide"
)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Preprocess Your Data')

df = form_preprocessing()


        
            

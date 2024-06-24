import time
import pandas as pd
import streamlit as st
import pickle
from sklearn.utils import resample, shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class DataPreprocessing:
	def __init__(self, file_path):
		self.file_path = file_path
		self.df = None
		self.X = None
		self.Y = None
		self.x_train, self.x_test, self.y_train, self.y_test = [None] * 4
		
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
  
	def seperate_data(self):
		self.X = self.df.drop('Creditability', axis=1)
		self.Y = self.df['Creditability']
  
	def split_data(self, test_size=0.2, random_state=42):
		self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.X, self.Y, test_size=test_size, random_state=random_state
        )
  
	def Scaler(self, scaler, scaler_name):
		self.x_train = scaler.fit_transform(self.x_train)
		self.x_test = scaler.transform(self.x_test)
		self.scaler = scaler
		self.save_scaler(f'scaler/user_trained/{scaler_name}.pickle')
  
	def save_scaler(self, path):
		with open(path, 'wb') as file:
			pickle.dump(self.scaler, file)
  
def data_preprocessing(data_prep, null_handle, resample, shuffle, test_size, scaler, scaler_name):
	data_prep.load_data()
	if null_handle == "Drop":
		data_prep.drop_na()
	else:
		data_prep.mean_na()
	if resample==True:
		data_prep.resampling()
	if shuffle==True:
		data_prep.shuffle()
	data_prep.seperate_data()
	data_prep.split_data(test_size)
	data_prep.Scaler(scaler, scaler_name)
	
	return data_prep

def df_info(df, data_preview, tab_title):
   df_info = pd.DataFrame({
      'Creditability': ['Not Eligible', 'Eligible'],
      'Count': df['Creditability'].groupby(df['Creditability']).count()
	})
   df_null = df.isnull().sum()
   df_null.name = 'Null Count'
   tab_1, tab_2, tab_3 = st.tabs(['Data count', tab_title, 'Data null'])
   with tab_1:
      st.dataframe(df_info, hide_index=True)
   with tab_2:
      st.dataframe(data_preview, hide_index=True)
   with tab_3:
      st.dataframe(df_null)

def form_preprocessing():
	data_prep = DataPreprocessing(file_path="dataset/german.csv")
	data_prep.load_data()
	st.header('Raw data')
	df_info(data_prep.df, data_prep.df.head(), 'Data preview')
	st.header('Choose your own data handling method')
	with st.form("preprocessing"):
		st.info('Recommended to resampling data because data not balanced!', icon='ℹ')
		test_size = st.slider(label="Test Size",  min_value=0.10, max_value=0.90, format="%.2f")
		null_handle = st.radio("NA Handle", ["Drop", "Mean"], index=0, horizontal=True)
		col1, col2 = st.columns(2)
		with col1:
			resample = st.toggle("Resample")
		with col2:
			shuffle = st.toggle("Shuffle")
		scaler = st.selectbox("Scaler", options=["StandardScaler", "MinMaxScaler"], index=0)
		scaler_name = st.text_input("Enter your scaler name", value='user_scaler')
		if st.form_submit_button("Submit"):
			if scaler == "StandardScaler":
				scaler = StandardScaler()
			else:
				scaler = MinMaxScaler()
			dp = data_preprocessing(data_prep, null_handle, resample, shuffle, test_size, scaler, scaler_name)
			st.success("Data Preprocessing Success")
			st.session_state["data_preprocessing"] = dp
			st.header('Preprocessed Data')
			df_info(dp.df, dp.x_train[:5], 'Scaled data')
			st.session_state["data_preprocessing"] = dp
			
	if 'data_preprocessing' in st.session_state:
		if st.button('Train your model', use_container_width=True, type='primary'):
			st.switch_page('pages/4_Train_Your_Model.py')
			
st.set_page_config(
	page_title="Data Preprocessing",
	layout="wide"
)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Preprocess Your Data')

df = form_preprocessing()


        
            

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
import os

st.set_page_config(
	page_title="Prediction Demo",
	layout="wide"
)

def load_data(is_user_model, is_user_scaler):
	if is_user_model:
		model = load_user_model()
	else:
		model = load_default_model()

	if is_user_scaler:
		scaler = load_user_scaler()
	else:
		scaler = load_default_scaler()
	return model, scaler

def load_default_model():
	with open('model/default.pickle', 'rb') as file:
		model = pickle.load(file)
	return model

def load_default_scaler():
	with open('scaler/default.pickle', 'rb') as file:
		scaler = pickle.load(file)
	return scaler

def load_user_model():
	folder_path = 'model/user_trained'
	file_list = os.listdir(folder_path)
	pickle_files = [f for f in file_list if f.endswith('.pickle')]

	model = {}
	for pickle_file in pickle_files:
		file_path = os.path.join(folder_path, pickle_file)
		with open(file_path, 'rb') as file:
			model[pickle_file] = pickle.load(file)
	return model

def load_user_scaler():
	folder_path = 'scaler/user_trained'
	file_list = os.listdir(folder_path)
	pickle_files = [f for f in file_list if f.endswith('.pickle')]

	scaler = {}
	for pickle_file in pickle_files:
		file_path = os.path.join(folder_path, pickle_file)
		with open(file_path, 'rb') as file:
			scaler[pickle_file] = pickle.load(file)
		print(scaler)
	return scaler

def form():
	form = st.form('my_form')
	
	with form:
		col_1, col_2 = st.columns(2)

		with col_1:
			acc_balance = st.selectbox(
				'Account Balance',
				['No Account', 'No Balance', 'Below 200DM', '200DM or Above'],
				index=0,
			)
			credit_monthly = st.number_input('Duration of credit monthly', value=0)
			payment_status = st.selectbox(
				'Payment status',
				['Delayed', 'Other Credits', 'Paid Up', 'No Problem with Current Credits', 'Previous Credits Paid'],
				index=0,
			)
			purpose = st.selectbox(
				'Purpose',
				['New Car', 'Used Car', 'Furniture', 'Radio/TV', 'Appliances', 'Repair', 'Vacation', 'Retraining', 'Business', 'Other'],
				index=0,
			)
			credit_amount = st.number_input('Credit Amount', value=0)
			value_savings = st.selectbox(
				'Saving/Stock value',
				['None', 'Below 100DM', '100-500DM', '500-1000DM', 'Above 1000DM'],
				index=0,
			)
			current_employment = st.selectbox(
				'Length of current employment',
				['Unemployed', '<1 Year', '1-4 Year', '4-7 Year', 'Above 7 Year'],
				index=0,
			)
			instalment_per_cent = st.selectbox(
				'Installments %',
				['Above 35%', '25-35%', '20-25%', 'Below 20%'],
				index=0,
			)
			sex_martial = st.selectbox(
				'Sex and martial status',
				['Male, Divorced', 'Male, Single', 'Male, Married/Widowed', 'Female'],
				index=0,
			)
			guarantors = st.selectbox(
				'Guarantor',
				['None', 'Co-applicant', 'Guarantor'],
				index=0,
			)

		with col_2:
			duration_address = st.selectbox(
				'Duration in current address',
				['<1 Year', '1-4 Year', '4-7 Year', 'Above 7 Year'],
				index=0,
			)
			valuable_asset = st.selectbox(
				'Most valuable asset',
				['None', 'Car', 'Life Insurance', 'Real Estate'],
				index=0,
			)
			age = st.number_input('Age years', value=0)
			concurrent_credits = st.selectbox(
				'Concurrent credits',
				['Other Banks', 'Dept. Store', 'None'],
				index=0,
			)
			apartment = st.selectbox(
				'Type of apartment',
				['Free', 'Rented', 'Owned'],
				index=0,
			)
			credit_this_bank = st.selectbox(
				'Number of credits at bank',
				['1', '2 or 3', '4 or 5', 'Above 6'],
				index=0,
			)
			occupation = st.selectbox(
				'Occupation',
				['Unemployed unskilled', 'Unskilled permanent resident', 'Skilled', 'Executive'],
				index=0,
			)
			dependents = st.selectbox(
				'Number of dependents',
				['3 or More', 'Less than 3'],
				index=0,
			)
			telephone = st.selectbox(
				'Telephone',
				['Yes', 'No'],
				index=0,
	 		)
			foreign_worker = st.selectbox(
				'Foreign worker',
				['Yes', 'No'],
				index=0,
	 		)

		submitted = st.form_submit_button('Predict')
	if submitted:
		df = [[
			['No Account', 'No Balance', 'Below 200DM', '200DM or Above'].index(acc_balance)+1,
			credit_monthly,
			['Delayed', 'Other Credits', 'Paid Up', 'No Problem with Current Credits', 'Previous Credits Paid'].index(payment_status)+1,
			['New Car', 'Used Car', 'Furniture', 'Radio/TV', 'Appliances', 'Repair', 'Vacation', 'Retraining', 'Business', 'Other'].index(purpose), 
			credit_amount,
			['None', 'Below 100DM', '100-500DM', '500-1000DM', 'Above 1000DM'].index(value_savings)+1,
			['Unemployed', '<1 Year', '1-4 Year', '4-7 Year', 'Above 7 Year'].index(current_employment)+1,
			['Above 35%', '25-35%', '20-25%', 'Below 20%'].index(instalment_per_cent)+1,
			['Male, Divorced', 'Male, Single', 'Male, Married/Widowed', 'Female'].index(sex_martial)+1,
			['None', 'Co-applicant', 'Guarantor'].index(guarantors)+1, 
			['<1 Year', '1-4 Year', '4-7 Year', 'Above 7 Year'].index(duration_address)+1,
			['None', 'Car', 'Life Insurance', 'Real Estate'].index(valuable_asset)+1,
			age, 
			['Other Banks', 'Dept. Store', 'None'].index(concurrent_credits)+1,
			['Free', 'Rented', 'Owned'].index(apartment)+1,
			['1', '2 or 3', '4 or 5', 'Above 6'].index(credit_this_bank)+1,
			['Unemployed unskilled', 'Unskilled permanent resident', 'Skilled', 'Executive'].index(occupation)+1,
			['3 or More', 'Less than 3'].index(dependents)+1,
			['Yes', 'No'].index(telephone)+1,
			['Yes', 'No'].index(foreign_worker)+1
		]]

		return df

def predict_creditability(model, scaler, df):
	df = scaler.transform(df)
	return model.predict(df)

def is_folder_empty(folder_path):
	if not os.path.exists(folder_path):
		print(f"The folder {folder_path} does not exist.")
		return False
	dir = os.listdir(folder_path)
	return True if not dir else False

def main():
	is_user_model_empty, is_user_scaler_empty = is_folder_empty('model/user_trained'), is_folder_empty('scaler/user_trained')
	st.header('Choose your own model and scaler')
	st.warning('*If has not train a model the button will be disabled')
	st.warning('*Default model: Random Forest Classifier, Default scaler: Standard Scaler')
	col_model, col_scaler =  st.columns(2)
	with col_model:
		is_user_model = st.toggle('Use your trained model', disabled=is_user_model_empty)
	with col_scaler:
		is_user_scaler = st.toggle('Use your trained scaler', disabled=is_user_scaler_empty)

	MODELS, SCALERS = load_data(
		is_user_model=is_user_model,
		is_user_scaler=is_user_scaler
	)

	model = MODELS if not is_user_model else st.selectbox(
		'Choose your model',
		MODELS.keys()
	)

	scaler = SCALERS if not is_user_scaler else st.selectbox(
		'Choose your scaler',
		SCALERS.keys()
	)

	st.header('Loan Approval')
	col_form, col_prediction = st.columns(2)
	with col_form:
		df = form()

	with col_prediction:
		st.write('Creditability')
		if df is not None:
			prediction = predict_creditability(
				model=MODELS if not is_user_model else MODELS[model], 
				scaler=SCALERS if not is_user_scaler else SCALERS[scaler], 
				df=df)
			if prediction == 0:
				st.warning('Not eligible')
			else:
				st.success('Eligible')

if __name__ == '__main__':
	main()


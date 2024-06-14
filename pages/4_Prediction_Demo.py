import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
	page_title="Prediction Demo",
	layout="wide"
)

@st.cache_data
def load_data():
	st.spinner('Loading model...')
	with open('model/model.pickle', 'rb') as file:
		model = pickle.load(file)
		st.success('Model loaded!!')
	
	st.spinner('Loading scaler...')
	with open('scaler/standard_scaler.pickle', 'rb') as file:
		scaler = pickle.load(file)
		st.success('Scaler loaded!!')
	
	return model, scaler

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

		submitted = st.form_submit_button('Submit')
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

def main():
	MODEL, SCALER = load_data()

	st.title('Loan Approval')
	col_1, col_2 = st.columns(2)
	with col_1:
		df = form()

	with col_2:
		st.write('Creditability')
		if df is not None:
			prediction = predict_creditability(model=MODEL, scaler=SCALER, df=df)
			if prediction == 0:
				st.write('Not eligible')
			else:
				st.write('Eligible')

main()
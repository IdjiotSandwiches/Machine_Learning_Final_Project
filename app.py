import streamlit as st
import pandas as pd
import numpy as np
import pickle

def load_model():
	with open('../model.pickle', 'rb') as file:
	   return pickle.load(file)

def form():
	form = st.form('my_form')
	
	acc_balance = form.number_input('Account_Balance', value=0)
	credit_monthly = form.number_input('Duration_of_Credit_monthly', value=0)
	payment_status = form.number_input('Payment_Status_of_Previous_Credit', value=0)
	purporse = form.number_input('Purpose', value=0)
	credit_amount = form.number_input('Credit_Amount', value=0)
	value_savings = form.number_input('Value_Savings_Stocks', value=0)
	current_employment = form.number_input('Length_of_current_employment', value=0)
	instalment_per_cent = form.number_input('Instalment_per_cent', value=0)
	sex_martial = form.number_input('Sex_Marital_Status', value=0)
	guarantors = form.number_input('Guarantors', value=0)
	duration_address = form.number_input('Duration_in_Current_address', value=0)
	valuable_asset = form.number_input('M_valuable_available_asset', value=0)
	age = form.number_input('Age_years', value=0)
	concurrent_credits = form.number_input('Concurrent_Credits', value=0)
	apartment = form.number_input('Type_of_apartment', value=0)
	credit_this_bank = form.number_input('No_of_Credits_at_this_Bank', value=0)
	occupation = form.number_input('Occupation', value=0)
	dependents = form.number_input('No_of_dependents', value=0)
	telephone = form.number_input('Telephone', value=0)
	foreign_worker = form.number_input('Foreign_Worker', value=0)

	submitted = form.form_submit_button('Submit')
	if submitted:
		df = pd.DataFrame({
			'Account_Balance': [acc_balance],
			'Duration_of_Credit_monthly': [credit_monthly],
			'Payment_Status_of_Previous_Credit': [payment_status],
			'Purpose': [purporse],
			'Credit_Amount': [credit_amount],
			'Value_Savings_Stocks': [value_savings],
			'Length_of_current_employment': [current_employment],
			'Instalment_per_cent': [instalment_per_cent],
			'Sex_Marital_Status': [sex_martial],
			'Guarantors': [guarantors],
			'Duration_in_Current_address': [duration_address],
			'Most_valuable_available_asset': [valuable_asset],
			'Age_years': [age],
			'Concurrent_Credits': [concurrent_credits],
			'Type_of_apartment': [apartment],
			'No_of_Credits_at_this_Bank': [credit_this_bank],
			'Occupation': [occupation],
			'No_of_dependents': [dependents],
			'Telephone': [telephone],
			'Foreign_Worker': [foreign_worker]
		})
		
		return df

def predict_creditability(model, df):
	return model.predict(df)

def main():
	st.title('Loan Approval')
	model = load_model()
	df = form()
	st.write('Creditability')
	if df is not None:
		prediction = predict_creditability(model, df)
		if prediction == 0:
			st.write('Not eligible')
		else:
			st.write('Eligible')

main()
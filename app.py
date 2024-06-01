import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_extras.stylable_container import stylable_container

def load_model():
	with open('../model.pickle', 'rb') as file:
	   return pickle.load(file)

def form():
	form = st.form('my_form')
	
	with form:
		col_1, col_2 = st.columns(2)

		with col_1:
			acc_balance = st.number_input('Account_Balance', value=0)
			credit_monthly = st.number_input('Duration_of_Credit_monthly', value=0)
			payment_status = st.number_input('Payment_Status_of_Previous_Credit', value=0)
			purporse = st.number_input('Purpose', value=0)
			credit_amount = st.number_input('Credit_Amount', value=0)
			value_savings = st.number_input('Value_Savings_Stocks', value=0)
			current_employment = st.number_input('Length_of_current_employment', value=0)
			instalment_per_cent = st.number_input('Instalment_per_cent', value=0)
			sex_martial = st.number_input('Sex_Marital_Status', value=0)
			guarantors = st.number_input('Guarantors', value=0)

		with col_2:
			duration_address = st.number_input('Duration_in_Current_address', value=0)
			valuable_asset = st.number_input('M_valuable_available_asset', value=0)
			age = st.number_input('Age_years', value=0)
			concurrent_credits = st.number_input('Concurrent_Credits', value=0)
			apartment = st.number_input('Type_of_apartment', value=0)
			credit_this_bank = st.number_input('No_of_Credits_at_this_Bank', value=0)
			occupation = st.number_input('Occupation', value=0)
			dependents = st.number_input('No_of_dependents', value=0)
			telephone = st.number_input('Telephone', value=0)
			foreign_worker = st.number_input('Foreign_Worker', value=0)

		submitted = st.form_submit_button('Submit')
	if submitted:
		df = [[
			acc_balance, credit_monthly, payment_status, purporse, credit_amount, value_savings, current_employment, instalment_per_cent, sex_martial, guarantors, 
			duration_address, valuable_asset, age, concurrent_credits, apartment, credit_this_bank, occupation, dependents, telephone, foreign_worker
		]]

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
import streamlit as st
import pandas as pd

st.set_page_config(
	page_title="Exploratory Data Analysis",
	layout='wide'
)

def init():
    col_1, col_2 = st.columns(2)
    with col_1:
        data_credit = {'Creditability':[1, 0], 'Description':['credit-worthy', 'not credit-worthy']}
        Creditability = pd.DataFrame(data_credit)
        st.dataframe(Creditability, hide_index=True, use_container_width=True, height=200)
        
        data_account ={'Balacence in current account':[1, 2, 3, 4], 'Description':['No running account', 'No Balance', '0<= current_money <200 DM', '>= 200 DM']}
        Account = pd.DataFrame(data_account)
        st.dataframe(Account, hide_index=True, use_container_width=True, height=200)
        
        data_month = {'Duration in Month':[1,2,3,4,5,6,7,8,9,10], 'Description':['> 54 months', '48< months <= 54', '42 < months <=48', '36 < months <= 42', '30< months <=36', '24 < months <=30', '18 < months <=24', '12 < months<=18', '6< months<=12', '<= 6months']}
        Months = pd.DataFrame(data_month)
        st.dataframe(Months, hide_index=True, use_container_width=True, height=200)
        
        data_prev = {'Payment of previous credits':[0,1,2,3,4], 'Description':['hesitant payment of previous credits', 'problematic running account / there are further credits running but at other banks', 'no previous credits / paid back all previous credits', 'no problems with current credits at this bank', 'paid back previous credits at this bank']}
        Prev = pd.DataFrame(data_prev)
        st.dataframe(Prev, hide_index=True, use_container_width=True, height=200)
        
        data_purpose = {'Purpose of Credit':[0,1,2,3,4,5,6,7,8,9,10], 'Description':['other', 'new car', 'used car', 'items of furniture', 'radio / television', 'household appliances', 'repair', 'education', 'vacation', 'retraining', 'business']}
        Purpose = pd.DataFrame(data_purpose)
        st.dataframe(Purpose, hide_index=True, use_container_width=True, height=200)
        
        data_ammount = {'Amount of credit in DM': [1,2,3,4,5,6,7,8,9,10], 'Description':['> 20000', '15000 < Credit <= 20000', '10000 < Credit <= 15000', '7500 < Credit <= 10000', '5000 < Credit <= 7500', '2500 < Credit <= 5000', '1500 < Credit <= 2500', '1000 < Credit <= 1500', '500 < Credit <= 1000', '<=500']}
        Ammount = pd.DataFrame(data_ammount)
        st.dataframe(Ammount, hide_index=True, use_container_width=True, height=200)
        
        data_saving = {'Value of savings or stocks in DM': [1,2,3,4,5], 'Description': ['not available / no savings', '< 100', '100<= Savings < 500', '500 <= Savings < 1000' , '>= 1000']}
        Saving = pd.DataFrame(data_saving)
        st.dataframe(Saving, hide_index=True, use_container_width=True, height=200)
        
        data_employment = {'Has been employed by current employer for': [1,2,3,4,5], 'Description':['unemployed', '<= 1 year', '1 <= years < 4', '4 <= years < 7', '>= 7 years']}
        Employment = pd.DataFrame(data_employment)
        st.dataframe(Employment, hide_index=True, use_container_width=True, height=200)

        data_installment = {'Instalment in % of available income': [1,2,3,4], 'Description':['>= 35', '25 <= percentage < 35', '20 <= percentage < 25', '< 20']}
        Installment = pd.DataFrame(data_installment)
        st.dataframe(Installment, hide_index=True, use_container_width=True, height=200)

        data_marital = {'Marital Status / Sex':[1,2,3,4], 'Description':['male: divorced / living apart', 'male: single', 'male: married / widowed', 'female']}
        Marital = pd.DataFrame(data_marital)
        st.dataframe(Marital, hide_index=True, use_container_width=True, height=200)

        data_gurantor = {'Further debtors / Guarantors': [1,2,3], 'Description':['none', 'Co-Applicant', 'Guarantor']}
        Gurantor = pd.DataFrame(data_gurantor)
        st.dataframe(Gurantor, hide_index=True, use_container_width=True, height=200)
    
    with col_2:
        data_living = {'Living in current household for':[1,2,3,4], 'Description':['< 1 year', '1 <= years < 4', '4 <= years < 7', '>= 7 years']}
        Living = pd.DataFrame(data_living)
        st.dataframe(Living, hide_index=True, use_container_width=True, height=200)
        
        data_asset ={'Most valuable available assets':[1,2,3,4], 'Description':['not available / no assets', 'Car / Other', 'Savings contract with a building society / Life insurance', 'Ownership of house or land']}
        Asset = pd.DataFrame(data_asset)
        st.dataframe(Asset, hide_index=True, use_container_width=True, height=200)
        
        data_age = {'Age in years':[1,2,3,4,5], 'Description':['0 <= Age <= 25', '26 <= Age <= 39', '40 <= Age <= 59', '>= 65 Age', '60 <= Age <= 64']}
        Age = pd.DataFrame(data_age)
        st.dataframe(Age, hide_index=True, use_container_width=True, height=200)
        
        data_running = {'Further running credits':[1,2,3], 'Description':['at other banks', 'at department store or mail order house', 'no further running credits']}
        Running = pd.DataFrame(data_running)
        st.dataframe(Running, hide_index=True, use_container_width=True, height=200)
        
        data_apartment ={'Type of apartment':[1,2,3], 'Description':['free apartment', 'rented flat', 'owner-occupied flat']}
        Aparterment = pd.DataFrame(data_apartment)
        st.dataframe(Aparterment, hide_index=True, use_container_width=True, height=200)
        
        data_prev_running = {'Number of previous credits at this bank (including the running one)': [1,2,3,4], 'Description':['one', 'two or three', 'four or five', 'six or more']}
        Prev_Running = pd.DataFrame(data_prev_running)
        st.dataframe(Prev_Running, hide_index=True, use_container_width=True, height=200)
        
        data_occupation = {'Occupation':[1,2,3,4], 'Description':['unemployed / unskilled with no permanent residence', 'unskilled with permanent residence', 'skilled worker / skilled employee / minor civil servant', 'executive / self-employed / higher civil servant']}
        Occupation = pd.DataFrame(data_occupation)
        st.dataframe(Occupation, hide_index=True, use_container_width=True, height=200)
        
        data_entitled = {'Number of persons entitled to maintenance':[1,2], 'Description':['3 and more', '0 to 2']}
        Entitled = pd.DataFrame(data_entitled)
        st.dataframe(Entitled, hide_index=True, use_container_width=True, height=200)
        
        data_telephone ={'Telephone':[1,2], 'Description':['no', 'yes']}
        Telephone = pd.DataFrame(data_telephone)
        st.dataframe(Telephone, hide_index=True, use_container_width=True, height=200)
        
        data_foreign = {'Foreign worker':[1,2], 'Description':['yes', 'no']}
        Foriegn = pd.DataFrame(data_foreign)
        st.dataframe(Foriegn, hide_index=True, use_container_width=True, height=200)
    
def main():
    st.title("Data Encoding")
    init()
    
    
main()
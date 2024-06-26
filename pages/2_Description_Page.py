from config import *

def create_table(subheader, items):
    col_config = {
        'Label': st.column_config.Column(
            width='small'
        ),
        'Description': st.column_config.Column(
            width='large'
        )
    }
    st.subheader(subheader)
    st.dataframe(pd.DataFrame(items), hide_index=True, use_container_width=True, height=200, column_config=col_config)

def init():
    
    col_1, col_2 = st.columns(2)
    with col_1:
        data_credit = {'Label':[1, 0], 'Description':['Credit-worthy', 'Not Credit-worthy']}
        create_table('Creditability', data_credit)
        
        data_account = {'Label':[1, 2, 3, 4], 'Description':['No running account', 'No Balance', 'Below 200 DM', '200 DM or above']}
        create_table('Balance in current account', data_account)
        
        # data_month = {'Duration in Month':[1,2,3,4,5,6,7,8,9,10], 'Description':['More than 54 months', '49 - 54 months', '43 - 48 months', '37 - 42 months', '31 - 36 month', '25 - 30 months', '19 - 24 months', '13 - 18 months', '6 - 12 months', 'Less than 6 months']}
        # st.dataframe(pd.DataFrame(data_month), hide_index=True, use_container_width=True, height=200, column_config=col_config)
        
        data_prev = {'Label':[0,1,2,3,4], 'Description':['Hesitant payment of previous credits', 'Problematic running account / there are further credits running but at other banks', 'No previous credits / paid back all previous credits', 'No problems with current credits at this bank', 'Paid back previous credits at this bank']}
        create_table('Payment of previous credits', data_prev)
        
        data_purpose = {'Label':[0,1,2,3,4,5,6,7,8,9,10], 'Description':['Other', 'New car', 'Used car', 'Items of furniture', 'Radio / Television', 'Household appliances', 'Repair', 'Education', 'Vacation', 'Retraining', 'Business']}
        create_table('Purpose of credit', data_purpose)
        
        data_ammount = {'Label': [1,2,3,4,5,6,7,8,9,10], 'Description':['More than 20000', '15000-20000', '10000-14999', '7500-9999', '5000-7499', '2500-4999', '1500-2499', '1000-1499', '500-999', 'Less than 500']}
        create_table('Amount of credit in DM', data_ammount)
        
        data_saving = {'Label': [1,2,3,4,5], 'Description': ['Not available / No savings', 'Less than 100', '100-499', '500-1000' , 'More than 1000']}
        create_table('Value of savings or stocks in DM', data_saving)
        
        data_employment = {'Label': [1,2,3,4,5], 'Description':['Unemployed', 'Less than 1 year', '1-4 years', '4-7 years', 'More than 7 years']}
        create_table('Has been employed by current employer for', data_employment)

        data_installment = {'Label': [1,2,3,4], 'Description':['Above 35', '25-35', '20-25', 'Below 20']}
        create_table('Instalment in % of available income', data_installment)

        data_marital = {'Label':[1,2,3,4], 'Description':['Male: Divorced / Living apart', 'Male: Single', 'Male: Married / Widowed', 'Female']}
        create_table('Martial Status / Sex', data_marital)

        data_guarantor = {'Label': [1,2,3], 'Description':['None', 'Co-Applicant', 'Guarantor']}
        create_table('Further debtors / Guarantors', data_guarantor)
    with col_2:
        data_living = {'Label':[1,2,3,4], 'Description':['Less than 1 year', '1-4 years', '4-7 years', 'More than 7 years']}
        create_table('Living in current household for', data_living)
        
        data_asset = {'Label':[1,2,3,4], 'Description':['Not available / No assets', 'Car / Other', 'Savings contract with a building society / Life insurance', 'Ownership of house or land']}
        create_table('Most valuable available assets', data_asset)
        
        data_age = {'Label':[1,2,3,4,5], 'Description':['0-25', '26-39', '40-59', '60-64', 'Above 65']}
        create_table('Age in years', data_age)
        
        data_running = {'Label':[1,2,3], 'Description':['At other banks', 'At department store or mail order house', 'No further running credits']}
        create_table('Further running credits', data_running)
        
        data_apartment = {'Label':[1,2,3], 'Description':['Free apartment', 'Rented flat', 'Owner-occupied flat']}
        create_table('Type of apartment', data_apartment)
        
        data_prev_running = {'Label': [1,2,3,4], 'Description':['One', 'Two or Three', 'Four or Five', 'Six or more']}
        create_table('Number of previous credits at this bank', data_prev_running)
        
        data_occupation = {'Label':[1,2,3,4], 'Description':['Unemployed / Unskilled with no permanent residence', 'Unskilled with permanent residence', 'Skilled worker / Skilled employee / Minor civil servant', 'Executive / Self-employed / Higher civil servant']}
        create_table('Occupation', data_occupation)
        
        data_entitled = {'Label':[1,2], 'Description':['3 and more', '0-2']}
        create_table('Number of persons entitled to maintenance', data_entitled)
        
        data_telephone = {'Label':[1,2], 'Description':['No', 'Yes']}
        create_table('Telephone', data_telephone)
        
        data_foreign = {'Label':[1,2], 'Description':['Yes', 'No']}
        create_table('Foreign worker', data_foreign)
    
def main():
    st.title("Data Encoding")
    st.info('Currency in Deutsche Mark DM', icon='ℹ️')
    init()
    
if __name__ == '__main__':
    config = page_config('Label Description')
    main()
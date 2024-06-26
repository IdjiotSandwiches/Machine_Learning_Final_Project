from config import *

def main():
	st.title('LOAN CREDIT CLASSIFICATION')
	head = Image.open('img/Header.jpg')
	head = head.resize((1300,500))
	st.image(head)
	st.markdown("""
		<div style='text-align: justify;'>
		Have you ever try to get a loan for a business, house, or for general means? But don't know if you will be approved or not?
FRET NOT

Using machine learning techniques and state of the art services could be your answer! By just filling in some of your general information we could see if you will be approved to get the loan or not!
		</div>	 
	""", unsafe_allow_html=True)

	if st.button('Get Started ➤'):
			st.switch_page('pages/1_Exploratory_Data_Analysis.py')

	des1,des2 = st.columns(2)
	with des1:
		st.subheader('Data Description')
		desimg = Image.open('dimg/atades.png')
		st.image(desimg)
	with des2:
		st.markdown("""
		<div style='text-align: justify;'>
		<br>  
		</br>
		You don't know what you need to fill in? You can see the data requirements or parameters here!
		</div>	 
		""", unsafe_allow_html=True)

		if st.button('Description about data ➤'):
			st.switch_page('pages/2_Description_Page.py')

	eda1,eda2 = st.columns(2)
	with eda2:
		st.subheader('Analyzing Data')
		desimg = Image.open('img/eda.png')
		st.image(desimg)
	with eda1:
		st.markdown("""
		
		<br> 
		</br>
		<div style='text-align: justify;'>
		You want to see the data correlation or data patterns? you could use this function to see them!
		</div>	 
		""", unsafe_allow_html=True)

		if st.button('Explore the Data? ➤'):
			st.switch_page('pages/1_Exploratory_Data_Analysis.py')

	tr1,tr2 = st.columns(2)
	with tr1:
		st.subheader('Develop Your Own Model')
		desimg = Image.open('img/train.jpg')
		st.image(desimg)
	with tr2:
		st.markdown("""
		<div style='text-align: justify;'>
		<br>  
		</br>
		Preprocess your datas to make sure they are fit for training using this function and start training the model to predict your approval!
		</div>	 
		""", unsafe_allow_html=True)

		if st.button('Train Model ➤'):
			st.switch_page('pages/4_Train_Your_Model.py')
		
	pred1,pred2 = st.columns(2)
	with pred2:
		st.subheader('Predict Your Loan')
		desimg = Image.open('img/predict.jpg')
		st.image(desimg)
	with pred1:
		st.markdown("""
		<br> 
		</br>
		<div style='text-align: justify;'>
		You can see if you are approved or not with many models! you can select one with this function!		
		</div>	 
		""", unsafe_allow_html=True)

		if st.button('Predict Loan ➤'):
			st.switch_page('pages/5_Prediction_Demo.py')

if __name__ == '__main__':
	config = page_config('Home')
	main()

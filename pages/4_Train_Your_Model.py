import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
#from xgboost import XGBClassifier
from sklearn.svm import SVC
import pickle

st.set_page_config(
	page_title="Training Model",
	layout="wide"
)

class Model:
    def __init__(self, df):
        self.df = df
        self.X = None
        self.Y = None
        self.y_predict = None
        self.scaler = None
        self.x_train, self.x_test, self.y_train, self.y_test = [None] * 4
    
    # Seperate between X and Y
    def seperate_data(self):
        self.X = self.df.drop('Creditability', axis=1)
        self.Y = self.df['Creditability']

    # Train Test Split
    def split_data(self, test_size=0.2, random_state=42):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.X, self.Y, test_size=test_size, random_state=random_state
        )

    def Scaler(self, scaler, scaler_name):
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.transform(self.x_test)
        self.scaler = scaler
        self.save_scaler(self.scaler, f'scaler/user_trained/{scaler_name}.pickle')

    def save_scaler(self, scaler, path):
        with open(path, 'wb') as file:
            pickle.dump(scaler, file)
    
    # Model creation
    def create_model(self, modelused):
        self.model = modelused

    def train_model(self, model_name):
        self.model.fit(self.x_train, self.y_train)
        self.save_model(self.model, f'model/user_trained/{model_name}.pickle')
    
    def save_model(self, model, path):
        with open(path, 'wb') as file:
            pickle.dump(model, file)
    
    def model_predict(self):
        self.y_predict = self.model.predict(self.x_test)

    def predict(self, input):
        if self.scaler:
            input = self.scaler.transform(input)
        return self.model.predict(input)

    # Evaluation
    def report(self):
        cm = confusion_matrix(self.y_test, self.y_predict, labels=self.model.classes_)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=self.model.classes_)

        disp.plot(cmap="Blues")
        st.write(f"Accuracy: {round(accuracy_score(self.y_test, self.y_predict) * 100, 2)}%")
        st.pyplot()

def form_model():
    test_size = st.slider(label="Test Size",  min_value=0.10, max_value=0.90, format="%.2f")
    select_model = st.selectbox(label="Select Model", options=["RandomForestClassifer", "SVC", "LogisticRegression", "AdaBoostClassifier"])
    scaler = st.selectbox("Scaler", options=["StandardScaler", "MinMaxScaler"], index=0)

    if select_model == "RandomForestClassifer":
        randomforestform(Model(st.session_state["data_preprocessing"].df), scaler=scaler, test_size=test_size)
    elif select_model  == "SVC":
        svcform(Model(st.session_state["data_preprocessing"].df), scaler=scaler, test_size=test_size)
    elif select_model  == "LogisticRegression":
        logisticform(Model(st.session_state["data_preprocessing"].df), scaler=scaler, test_size=test_size)
    elif select_model  == "AdaBoostClassifier":
        adaform(Model(st.session_state["data_preprocessing"].df), scaler=scaler, test_size=test_size)

def randomforestform(model, scaler, test_size):
    with st.form("RandomForestClassifer Parameter"):
        n_est = st.number_input('Enter the number of estimators: ', min_value=0, value=100)
        m_dep = st.number_input('Enter the max depth: ', min_value=0, value=20)
        crit = st.selectbox('Enter the criterion',  ["gini", "entropy","log_loss"], index=0)
        c_wght = st.selectbox('Enter the class weight', ["balanced", "balanced_subsample"], index=0)
        model_name = st.text_input("Enter your model name", value='user_model')
        scaler_name = st.text_input("Enter your scaler name", value='user_scaler')
        if st.form_submit_button("Submit"):
            chosen_model = RandomForestClassifier(n_estimators=n_est, max_depth=m_dep, criterion=crit, class_weight=c_wght)
            model.seperate_data()
            model.split_data(test_size=test_size)
            if scaler == "StandardScaler":
                chosen_scaler = StandardScaler()
            else:
                chosen_scaler = MinMaxScaler()
            model.Scaler(chosen_scaler, scaler_name)
            model.create_model(chosen_model)
            model.train_model(model_name)
            model.model_predict()
            model.report()
            st.session_state["model"] = model
            st.success("Model Train Successful")   

def svcform(model, scaler, test_size):
    with st.form("SVC Parameter"):
        kernels = st.selectbox("Enter the kernel choice", ["linear", "poly", "rbf", "sigmoid"], index=0)
        model_name = st.text_input("Enter your model name", value='user_model')
        scaler_name = st.text_input("Enter your scaler name", value='user_scaler')
        if st.form_submit_button("Submit"):
            chosen_model = SVC(kernel=kernels)
            model.seperate_data()
            model.split_data(test_size=test_size)
            if scaler == "StandardScaler":
                chosen_scaler = StandardScaler()
            else:
                chosen_scaler = MinMaxScaler()
            model.Scaler(chosen_scaler, scaler_name)
            model.create_model(chosen_model)
            model.train_model(model_name)
            model.model_predict()
            model.report()
            st.session_state["model"] = model

def logisticform(model, scaler, test_size):
    with st.form("Logistic Regression Parameter"):
        c = st.number_input('Enter the regularization parameter (C): ', min_value= 1.00, format="%.2f")
        solvers = st.selectbox('Enter the solver: ', ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'], index=0)
        model_name = st.text_input("Enter your model name", value='user_model')
        scaler_name = st.text_input("Enter your scaler name", value='user_scaler')
        if st.form_submit_button("Submit"):
            chosen_model = LogisticRegression(C=c, solver=solvers)
            model.seperate_data()
            model.split_data(test_size=test_size)
            if scaler == "StandardScaler":
                chosen_scaler = StandardScaler()
            else:
                chosen_scaler = MinMaxScaler()
            model.Scaler(chosen_scaler, scaler_name)
            model.create_model(chosen_model)
            model.train_model(model_name)
            model.model_predict()
            model.report()
            st.session_state["model"] = model

def adaform(model, scaler, test_size):
    with st.form("LOgistic Regression Parameter"):
        n_est = st.number_input('Enter the number of estimators: ', min_value=0, value=100)
        l_rate = st.number_input('Enter the learning rate: ', min_value= 0.01, value= 0.05, format="%.2f")
        model_name = st.text_input("Enter your model name", value='user_model')
        scaler_name = st.text_input("Enter your scaler name", value='user_scaler')
        if st.form_submit_button("Submit"):
            chosen_model = AdaBoostClassifier(n_estimators=n_est, learning_rate=l_rate)
            model.seperate_data()
            model.split_data(test_size=test_size)
            if scaler == "StandardScaler":
                chosen_scaler = StandardScaler()
            else:
                chosen_scaler = MinMaxScaler()
            model.Scaler(chosen_scaler, scaler_name)
            model.create_model(chosen_model)
            model.train_model(model_name)
            model.model_predict()
            model.report()
            st.session_state["model"] = model

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Training Model')

if st.session_state.get("data_preprocessing"):
    form_model()
else:
    if st.button('Preprocess Data First'):
        st.switch_page('pages/3_Data Preprocessing.py')
        
if st.session_state.get("model"):
    if st.button('Predict Data'):
        st.switch_page('pages/5_Prediction_Demo.py')

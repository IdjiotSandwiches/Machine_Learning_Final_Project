import streamlit as st
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
#from xgboost import XGBClassifier
from sklearn.svm import SVC
import pickle
import plotly.express as px

st.set_page_config(
	page_title="Training Model",
	layout="wide"
)

class Model:
    def __init__(self, dp):
        self.dp = dp
        self.X = None
        self.Y = None
        self.y_predict = None
    
    # Model creation
    def create_model(self, modelused):
        self.model = modelused

    def train_model(self, model_name):
        self.model.fit(self.dp.x_train, self.dp.y_train)
        self.save_model(self.model, f'model/user_trained/{model_name}.pickle')
    
    def save_model(self, model, path):
        with open(path, 'wb') as file:
            pickle.dump(model, file)
    
    def model_predict(self):
        self.y_predict = self.model.predict(self.dp.x_test)

    def predict(self, input):
        input = self.dp.scaler.transform(input)
        return self.model.predict(input)

    # Evaluation
    def report(self):
        st.subheader(f"Accuracy: {round(accuracy_score(self.dp.y_test, self.y_predict) * 100, 2)}%")
        st.subheader("Confusion Matrix:")
        cm = confusion_matrix(self.dp.y_test, self.y_predict, labels=self.model.classes_)
        # disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=self.model.classes_)
        # disp.plot(cmap="Blues")
        fig = px.imshow(cm, text_auto=True)
        st.plotly_chart(fig, theme="streamlit")
        

def form_model():
    select_model = st.selectbox(label="Select Model", options=["RandomForestClassifer", "SVC", "LogisticRegression", "AdaBoostClassifier"])

    if select_model == "RandomForestClassifer":
        randomforestform(Model(st.session_state["data_preprocessing"]))
    elif select_model  == "SVC":
        svcform(Model(st.session_state["data_preprocessing"]))
    elif select_model  == "LogisticRegression":
        logisticform(Model(st.session_state["data_preprocessing"]))
    elif select_model  == "AdaBoostClassifier":
        adaform(Model(st.session_state["data_preprocessing"]))

def randomforestform(model):
    with st.form("RandomForestClassifer Parameter"):
        n_est = st.number_input('Enter the number of estimators: ', min_value=0, value=100)
        m_dep = st.number_input('Enter the max depth: ', min_value=0, value=20)
        crit = st.selectbox('Enter the criterion',  ["gini", "entropy","log_loss"], index=0)
        c_wght = st.selectbox('Enter the class weight', ["balanced", "balanced_subsample"], index=0)
        model_name = st.text_input("Enter your model name", value='user_model')
        if st.form_submit_button("Submit"):
            chosen_model = RandomForestClassifier(n_estimators=n_est, max_depth=m_dep, criterion=crit, class_weight=c_wght)
            model.create_model(chosen_model)
            model.train_model(model_name)
            model.model_predict()
            model.report()
            st.session_state["model"] = model
            st.success("Model Train Successful")   

def svcform(model):
    with st.form("SVC Parameter"):
        kernels = st.selectbox("Enter the kernel choice", ["linear", "poly", "rbf", "sigmoid"], index=0)
        model_name = st.text_input("Enter your model name", value='user_model')
        if st.form_submit_button("Submit"):
            chosen_model = SVC(kernel=kernels)
            model.create_model(chosen_model)
            model.train_model(model_name)
            model.model_predict()
            model.report()
            st.session_state["model"] = model

def logisticform(model):
    with st.form("Logistic Regression Parameter"):
        c = st.number_input('Enter the regularization parameter (C): ', min_value= 1.00, format="%.2f")
        solvers = st.selectbox('Enter the solver: ', ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'], index=0)
        model_name = st.text_input("Enter your model name", value='user_model')
        if st.form_submit_button("Submit"):
            chosen_model = LogisticRegression(C=c, solver=solvers)
            model.create_model(chosen_model)
            model.train_model(model_name)
            model.model_predict()
            model.report()
            st.session_state["model"] = model

def adaform(model):
    with st.form("Ada Boost Parameter"):
        n_est = st.number_input('Enter the number of estimators: ', min_value=0, value=100)
        l_rate = st.number_input('Enter the learning rate: ', min_value= 0.01, value= 0.05, format="%.2f")
        model_name = st.text_input("Enter your model name", value='user_model')
        if st.form_submit_button("Submit"):
            chosen_model = AdaBoostClassifier(n_estimators=n_est, learning_rate=l_rate)
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
        st.switch_page('pages/3_Data_Preprocessing.py')
        
if st.session_state.get("model"):
    if st.button('Predict Data', use_container_width=True, type='primary'):
        st.switch_page('pages/5_Prediction_Demo.py')

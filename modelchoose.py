import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.utils import resample, shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
#from xgboost import XGBClassifier
from sklearn.svm import SVC

class DataPreprocessing:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        
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
            n_samples=len(credible),
            random_state=42
        )
        self.df = pd.concat([credible, non_credible])
    
    def shuffle(self):
        self.df = shuffle(self.df)

		
class Model:
    def __init__(self, df):
        self.df = df
        self.X = None
        self.Y = None
        self.y_predict = None
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

    def Scaler(self):
        scaler = StandardScaler()
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.transform(self.x_test)

        self.save_scaler(scaler, 'scaler/standard_scaler.pickle')

    def save_scaler(self, scaler, path):
        with open(path, 'wb') as file:
            pickle.dump(scaler, file)
    
    # Model creation
    def create_model(self, modelused):
        self.model = modelused
        # self.model = RandomForestClassifier(
        #     n_estimators=200,
        #     max_depth=15,
        #     criterion='entropy',
        #     class_weight=None
        # )

    def train_model(self):
        self.model.fit(self.x_train, self.y_train)
        self.save_model(self.model, 'model/model.pickle')
    
    def model_predict(self):
        self.y_predict = self.model.predict(self.x_test)

    # Evaluation
    def report(self):
        cm = confusion_matrix(self.y_test, self.y_predict, labels=self.model.classes_)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=self.model.classes_)

        print(f'Classification Report:\n{classification_report(self.y_test, self.y_predict)}')
        disp.plot()
        plt.show()

    def save_model(self, model, path):
        with open(path, 'wb') as file:
            pickle.dump(model, file)


def data_preprocessing(file_path, null_handle, resample, shuffle):
    data_prep = DataPreprocessing(file_path=file_path)
    data_prep.load_data()
    if null_handle == 1:
        data_prep.drop_na()
    else:
        data_prep.mean_na()
    if resample==1:
        data_prep.resampling()
    if shuffle==1:
        data_prep.shuffle()
	
    return data_prep


def training_model(df, test_split, scaled, modelused):
    model = Model(df)
    model.seperate_data()
    model.split_data(test_split)
    if scaled == 1:
        model.Scaler()
        
    model.create_model(modelused)
    model.train_model()

    return model


def evaluation(model):
	model.model_predict()
	model.report()
	

def get_parameters():
    # Preprocessing
    dataprep = []
    null_handling = int(input('1. Drop, 2. Mean'))
    resampling = int(input('0. No, 1. Yes'))
    shuffling_data = int(input('0. No, 1. Yes'))
    dataprep.extend([null_handling, resampling, shuffling_data])
    
    # Model
    model_spec = []
    test_split = float(input('Enter the test split ratio (between 0-1): '))
    scaled = int(input('0. No, 1. Yes'))
    model_selection = int(input('Enter the model selection (1. Random Forest, 2. SVC, 3. Logreg, 4. XGB, 5. AdaBoost): '))
    
    if model_selection == 1:
        n_est = int(input('Enter the number of estimators: '))
        m_dep = int(input('Enter the max depth: '))
        crit = str(input('Enter the criterion ("gini", "entropy","log_loss"): '))
        c_wght = str(input('Enter the class weight ("None","Balanced"): '))
        chosen_model = RandomForestClassifier(n_estimators=n_est, max_depth=m_dep, crit=crit, class_weight=c_wght)
    
    elif model_selection == 2:
        kernels = input('Enter the kernel choice ("linear", "poly", "rbf", "sigmoid"): ')
        chosen_model = SVC(kernel=kernels)
    
    elif model_selection == 3:
        c = float(input('Enter the regularization parameter (C): '))
        solvers = input("'liblinear', 'lbfgs', 'saga': ")
        chosen_model = LogisticRegression(C=c, solver=solvers)
    
    elif model_selection == 5:
        n_est = int(input('Enter the number of estimators: '))
        l_rate = float(input('Enter the learning rate: '))
        chosen_model = AdaBoostClassifier(n_estimators=n_est, learning_rate=l_rate)
    
    model_spec.extend([test_split, scaled, chosen_model])
    
    return dataprep, model_spec

def main():
	file_path = 'dataset/german.csv'
	dataprep,model_choose=get_parameters()
	data_prep = data_preprocessing(file_path, dataprep[0],dataprep[1],dataprep[2])
	model = training_model(data_prep.df, model_choose[0],model_choose[1],model_choose[2])
	evaluation(model)

main()

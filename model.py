import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.utils import resample, shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.ensemble import RandomForestClassifier

class DataPreprocessing:
	def __init__(self, file_path):
		self.file_path = file_path
		self.df = None
		
	def load_data(self):
		self.df = pd.read_csv(self.file_path, sep=';')

	def drop_na(self):
		self.df.dropna(inplace=True)

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
	def create_model(self):
		self.model = RandomForestClassifier(
			n_estimators=200,
			max_depth=15,
			criterion='entropy',
			class_weight=None
		)

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

def data_preprocessing(file_path):
	data_prep = DataPreprocessing(file_path=file_path)
	data_prep.load_data()
	data_prep.drop_na()
	data_prep.resampling()
	data_prep.shuffle()

	return data_prep

def training_model(df):
	model = Model(df)
	model.seperate_data()
	model.split_data()
	model.Scaler()
	model.create_model()
	model.train_model()

	return model

def evaluation(model):
	model.model_predict()
	model.report()

def main():
	file_path = 'dataset/german.csv'
	data_prep = data_preprocessing(file_path=file_path)
	model = training_model(data_prep.df)
	evaluation(model)

main()
import streamlit as st
import pandas as pd
import numpy as np
import pickle, time, os
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from sklearn.utils import resample, shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.svm import SVC

def page_config(title):
	st.set_page_config(
		page_title=title,
		layout="wide",
	)
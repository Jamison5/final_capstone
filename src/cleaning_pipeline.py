import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import scipy.stats as stats 
import seaborn as sns 
import sklearn as skl 
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn import metrics
import math 
from pandas.plotting import scatter_matrix
import plotly.express as px


# df = pd.read_excel('../data/globalterrorismdb_0522dist.xlsx')


# df2 = df[['iyear', 'imonth', 'iday', 'country', 'country_txt', 'region', 'region_txt',
#         'provstate', 'city', 'attacktype1', 'attacktype1_txt', 'targtype1',
#         'targtype1_txt', 'targsubtype1', 'targsubtype1_txt', 'target1', 'natlty1', 'natlty1_txt',
#         'gname', 'weaptype1', 'weaptype1_txt']]

# df2['targsubtype1'].fillna(0.0, inplace=True)

# df2['city'].fillna('Unknown', inplace=True)

# df2['targsubtype1_txt'].fillna('Unknown', inplace=True)

# df2['target1'].fillna('Unknown', inplace=True)

# df2['natlty1_txt'].fillna('Unidentified', inplace=True)

# df2['natlty1'].fillna(0.0, inplace=True)


def preprocess_data(filename):
    '''
       Creates a DataFrame from input filepath that is composed of seleced columns. 
       
       Note: This function assumes you are working on the globalterrorism database
       and that the data bases structure has not been significantly changed.
    '''
    columns = ['iyear', 'imonth', 'iday', 'country', 'country_txt', 'region', 'region_txt',
               'provstate', 'city', 'attacktype1', 'attacktype1_txt', 'targtype1',
               'targtype1_txt', 'targsubtype1', 'targsubtype1_txt', 'target1', 'natlty1', 'natlty1_txt',
               'gname', 'weaptype1', 'weaptype1_txt']
    
    df = pd.read_excel(filename, usecols=columns)
    
    df.fillna({
        'targsubtype1': 0.0,
        'city': 'Unknown',
        'targsubtype1_txt': 'Unknown',
        'target1': 'Unknown',
        'natlty1_txt': 'Unidentified',
        'natlty1': 0.0
        }, inplace=True)
    
    return df


filepath = '../data/globalterrorismdb_0522dist.xlsx'
terrorism_df = preprocess_data(filepath)

taliban_atk_df = terrorism_df[terrorism_df['gname'] == 'Taliban'].reset_index(drop=True)
unknown_atk_df = terrorism_df[terrorism_df['gname'] == 'Unknown'].reset_index(drop=True)

if __name__ == '__main__':
    print(terrorism_df.head())
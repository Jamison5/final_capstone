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


def analyze_terrorism_data(filepath, group_names):
    
    '''
       Uses preprocess_data() to create a dataframe cleaned to required specifications,
       iterates over a list of stings which match desired groups from gname column. 
    '''
    
    terrorism_df = preprocess_data(filepath)
    
    for group_name in group_names:
        group_atk_df = terrorism_df[terrorism_df['gname'] == group_name].reset_index(drop=True)
        
        plt.figure()
        plt.hist(group_atk_df['iyear'], label=group_name)
        plt.legend()
        plt.xlabel('Year')
        plt.ylabel('Frequency')
        plt.title(f'Histogram of Attack Years for {group_name}')
    
    plt.show()


def plot_top_categories(data, column_name, num_categories, title):
    
    '''Takes in a DataFrame, allows you to input a column_name as a string, a catagory or value
       from that column and a title for your graph. Produces a bar graph that visualizes the 
       top counts of your chosen catagory. For example: inputing weaptype1_txt will show a bar
       graph which contains the most used weapon types in a dataframe.
    '''
    
    category_counts = data[column_name].value_counts().nlargest(num_categories)
    
    plt.bar(category_counts.index, category_counts.values)
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title(title)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    



if __name__ == '__main__':
    # creates a veriable filepath to input in latter functions
    filepath = '../data/globalterrorismdb_0522dist.xlsx'
    
    # Creates a lis of group names to create multiple histogram plots from using analyze_terrorism_data()
    group_names = ['Taliban', 'Unknown', 'Islamic State of Iraq and the Levant (ISIL)', 'Shining Path (SL)',
                   'Al-Shabaab', "New People's Army (NPA)", 'Farabundo Marti National Liberation Front (FMLN)',
                   'Boko Haram', 'Houthi extremists (Ansar Allah)', 'Irish Republican Army (IRA)']

    # creates a cleaned dataframe
    terrorism_df = preprocess_data(filepath)
    taliban_df = terrorism_df[terrorism_df['gname']=='Taliban']

    # creates a bar graph showing the most active terrorist groups
    # most_active_groups = terrorism_df['gname'].value_counts().nlargest(10)
    # plt.bar(most_active_groups.index, most_active_groups.values)
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # creates a histogram showing the amount of terrorist attacks by year
    # plt.hist(terrorism_df['iyear'], bins=10)
    # plt.xlabel('Year')
    # plt.ylabel('Count')
    # plt.title('Occurrences by Year')
    # plt.show()

    # Creates histograms of group activity through years.
    # analyze_terrorism_data(filepath, group_names)

    plot_top_categories(taliban_df, 'weaptype1_txt', 10, 'Most Used Weapons in Taliban Attakcs')
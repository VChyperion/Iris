import sklearn
import numpy as np
import pandas as pd
import seaborn as sns

# Load the dataset 
data = pd.read_csv('iris.csv') 

def outlier_removal(data):
    # Calculating the IQR
    Q1 = np.percentile(data['sepal.width'], 25, 
                    method = 'midpoint') 
    
    Q3 = np.percentile(data['sepal.width'], 75, 
                    method = 'midpoint') 
    IQR = Q3 - Q1

    print("The Old Shape: ", data.shape)

    # Upper bound 
    upper = np.where(data['sepal.width'] >= (Q3+1.5*IQR)) 
    
    # Lower bound 
    lower = np.where(data['sepal.width'] <= (Q1-1.5*IQR)) 
    
    # Removing the Outliers 
    data.drop(upper[0], inplace = True) 
    data.drop(lower[0], inplace = True) 
    
    print("New Shape: ", data.shape) 
    
    sns.boxplot(x='SepalWidthCm', data=data)
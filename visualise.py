# Imports
import seaborn as sns
import matplotlib.pyplot as plt

def visualise_bar(data):
    sns.countplot(x='variety', data=data, ) 
    plt.show()

def visualise_scatter(data):
    sns.scatterplot(x='sepal.length', y='sepal.width', 
                    hue='variety', data=data, ) 
    
    # Placing Legend outside the Figure 
    plt.legend(bbox_to_anchor=(1, 1), loc=2) 
  
    plt.show()

def visualise_petal(data):
    sns.scatterplot(x='petal.length', y='petal.width', 
                hue='variety', data=data, ) 
  
    # Placing Legend outside the Figure 
    plt.legend(bbox_to_anchor=(1, 1), loc=2) 
  
    plt.show()
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
    
def visualise_pairplot(data):
    sns.pairplot(data.drop(['sepal.length'], axis = 1),  
                 hue='variety', height=2)
    
    plt.show()
    
def visualise_histogram(data):
    fig, axes = plt.subplots(2, 2, figsize=(10,10)) 
  
    axes[0,0].set_title("Sepal Length") 
    axes[0,0].hist(data['sepal.length'], bins=7) 
    
    axes[0,1].set_title("Sepal Width") 
    axes[0,1].hist(data['sepal.width'], bins=5); 
    
    axes[1,0].set_title("Petal Length") 
    axes[1,0].hist(data['petal.length'], bins=6); 
    
    axes[1,1].set_title("Petal Width") 
    axes[1,1].hist(data['petal.width'], bins=6);
    
    plt.show()
    
def visualise_histogram_distplot(data):
    plot = sns.FacetGrid(data, hue="variety") 
    plot.map(sns.histplot, "sepal.length").add_legend() 
    
    plot = sns.FacetGrid(data, hue="variety") 
    plot.map(sns.histplot, "sepal.width").add_legend() 
    
    plot = sns.FacetGrid(data, hue="variety") 
    plot.map(sns.histplot, "petal.length").add_legend() 
    
    plot = sns.FacetGrid(data, hue="variety") 
    plot.map(sns.histplot, "petal.width").add_legend() 
    
    plt.show()
    
# Heat map is broken and i will fix in the future (maybe)
def visualise_heatmap(data):
    sns.heatmap(data.corr(), annot=True)
    plt.show()

def visualise_boxplot(data):
    def boxplot(y):
        sns.boxplot(x="variety", y=y, data=data) 
    
    plt.figure(figsize=(10,10)) 
            
    # Adding the subplot at the specified 
    # grid position 
    plt.subplot(221) 
    boxplot('sepal.length') 
    plt.title('Sepal Length')
        
    plt.subplot(222) 
    boxplot('sepal.width') 
    plt.title('Sepal Length')
    
    plt.subplot(223) 
    boxplot('petal.length') 
    plt.title('Petal Length')   
    
    plt.subplot(224) 
    boxplot('petal.width') 
    plt.title('Petal Width')
    
    plt.show()
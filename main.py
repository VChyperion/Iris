# Exploratory Data Analysis on an Iris Dataset
# Src - https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/

# Imports
import pandas as pd
from visualise import visualise_bar, visualise_scatter, visualise_petal, visualise_pairplot, visualise_histogram, visualise_histogram_distplot, visualise_heatmap, visualise_boxplot
from outlier import outlier_removal

# Read the data
data = pd.read_csv("iris.csv")

class DataAnalyser:
    
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)
        
    def get_head(self):
        return self.data.head()
    
    def get_shape(self):
        return self.data.shape

    def get_info(self):
        return self.data.info() # info() prints directly and does not need a print statement

    def get_describe(self):
        return self.data.describe()

    def check_null(self):
        return self.data.isnull().sum()

    def locate_duplicates(self):
        return self.data.drop_duplicates(subset="variety")

    def value_counts(self):
        return self.data["variety"].value_counts()
    
    def visualise(self, option):
        if option == 8:
            visualise_bar(self.data)
        elif option == 9:
            visualise_scatter(self.data)
        elif option == 10:
            visualise_petal(self.data)
        elif option == 11:
            visualise_pairplot(self.data)
        elif option == 12:
            visualise_histogram(self.data)
        elif option == 13:
            visualise_histogram_distplot(self.data)
        elif option == 14:
            visualise_heatmap(self.data)
        elif option == 15:
            visualise_boxplot(self.data)
        else:
            print("Invalid Graphing option")

    def outlier(self, option):
        if option == 16:
            outlier_removal(self.data)
        

# Open and read from the csv file

    def main(self):
        
        # Print menu for clarity while using CLI
        print("\nMenu for functions in the IRIS program")
        print("1. Head ")
        print("2. Shape")
        print("3. Info")
        print("4. Describe")
        print("5. Check Null")
        print("6. Duplicates")
        print("7. Unique Values")
        print("8. Bar")
        print("9. Scatter")
        print("10. Petal")
        print("11. Pairplot")
        print("12. Histogram")
        print("13. Histogram w. Distplot Plot")
        print("14. Heatmap")
        print("15. Box Plot")
        print("16. Removing Outliers")
        print("0. End the Program")
        
        # Variable to set the while to infinite
        loop = False
        while not loop:
            try:      
                option = int(input("\nEnter an option (1-16): "))
            
                if option == 1:
                    # Print first 5 record
                    print(self.get_head())

                elif option == 2: 
                    # Print the shape of the dataset (Columns & Rows)
                    print(self.get_shape())

                elif option == 3: 
                    # Get the columns and data types
                    print(self.get_info())
                        
                elif option == 4: 
                    # Statistical Summary of the dataset
                    print(self.get_describe())
                        
                elif option == 5: 
                    # Checking for missing/null values
                    print(self.check_null())
                        
                elif option == 6:
                    # Locate any duplicates
                    print(self.locate_duplicates())
                        
                elif option == 7:
                    # Return counts of unique values
                    print(self.value_counts())
                
                elif option in [8, 9, 10, 11, 12, 13, 14, 15]:
                    # The graph functions - ref line 37
                    self.visualise(option)
                    
                elif option == 16:
                    self.outlier(option)
                
                elif option == 0:
                    print("Exiting the program.")
                    loop = True
                        
                else: 
                    print("Invalid Option")
                    loop = True
                
            except ValueError:
                print("ValueError :*( Restarting Program")

     

# Usage - Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_analyser = DataAnalyser("iris.csv")
    data_analyser.main()
    
    


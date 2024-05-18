# Exploratory Data Analysis on an Iris Dataset
# Src - https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/

# Imports
import pandas as pd
from visualise import visualise_bar
from visualise import visualise_scatter
from visualise import visualise_petal


# Read the data
data = pd.read_csv("iris.csv")

# Call the visualisation
graphs = input("Which graphs do you want to see? (B,S,P): ")
if graphs == "B":
    visualise_bar(data)     
elif graphs == "S": 
    visualise_scatter(data)
elif graphs == "P":
    visualise_petal(data)
else:
    pass

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

# Open and read from the csv file

    def main(self):
        # Variable to set the while to infinite
        try: 
            option = int(input("Enter an option (1-7): "))
        
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
                    
            else: 
                print("Didnt work dummy")
                loop = True
            
        except ValueError:
            print("ValueError :*( We will rerun main")
     

# Usage - Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_analyser = DataAnalyser("iris.csv")
    data_analyser.main()
    
    


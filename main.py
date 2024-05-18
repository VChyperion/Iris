# Exploratory Data Analysis on an Iris Dataset
# Src - https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/


# Imports
import pandas as pd

read = pd.read_csv("iris.csv")

# Print first 5 records
print(read.head())

# Print the shape of the dataset (Columns & Rows)
print(read.shape)


def main():
    print("Im cooking")
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Hi PyCharm')


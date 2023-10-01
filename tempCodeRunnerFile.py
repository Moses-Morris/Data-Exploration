import pandas as pandas
import pandasql
import matplotlib.pyplot as plt


#load csv file 
file =  pandas.read_excel('data.xlsx')

#remove missing values
fullFile = file.dropna()

#fill the missing values if necessary
#fillFile = file.fillna(file.mean())

# Remove duplicates based on all columns
file_no_duplicates = fullFile.drop_duplicates()


# Set Pandas display options to show all rows and columns
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

# Print the entire DataFrame
print(file_no_duplicates)

# Choose a column for creating  a histogram
column = 'column'  

# Create a histogram using the specified column
plt.figure(figsize=(10, 12))
file[column].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')

# labels and title
plt.xlabel(column)
plt.ylabel('Frequency')
plt.title('Instagram Success')

# Show the histogram
plt.show()
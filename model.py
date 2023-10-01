import pandas as pandas


#load csv file 
file =  panda.read_excel('data.xlsx')

#remove missing values
fullFile = file.dropna()

#fill the missing values if necessary
#fillFile = file.fillna(file.mean())

# Remove duplicates based on all columns
file_no_duplicates = fullFile.drop_duplicates()

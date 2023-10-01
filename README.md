# Measuring the Success of Instagram TV Product BASED ON METRICS


# Process:
1. Data Collection and Preparation. - We can perform web scraping or record data as it is generated.
2. Exploratory Data Analysis. - We can use Data Statisytics to derive insights. 
3. Data Visualization. - We can use graphs and charts to visualize the info.


# DATA PROCESSING:

1. import libraries

    - import pandas as pd
    - import pandasql    # let us use pandas and sql together.
    - import matplotlib.pyplot as plt


2. Read File. - Read the file 

    - file = read_excel('data.xlsx')

3. Load and Explore the Data Set
    1. Get the info
        - file.info()
    2. Print values
        - file.head(25)   # prints first 25 values.
        - file.tail()          # prints last rows.
   3. Histogram
        - plt.figure(figsize=(10, 12))
        - file[column].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')

4. Show Histogram
    1. Set labels and title
        - plt.xlabel(column)
        - plt.ylabel('Frequency')
        - plt.title('Instagram Success')
    2. Show the histogram
        - plt.show()
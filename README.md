# Measuring the Success of Instagram TV Product BASED ON METRICS

**Week 1 Project**
# Process:
1. Data Collection and Preparation. - We can perform web scraping or record data as it is generated.
2. Exploratory Data Analysis. - We can use Data Statisytics to derive insights. 
3. Data Visualization. - We can use graphs and charts to visualize the info.


# DATA PROCESSING:

1. import libraries

    ```python
        import pandas as pd
        import pandasql    # let us use pandas and sql together.
        import matplotlib.pyplot as plt
    ``` 


2. Read File. - Read the file 

    ```python
    file = read_excel('data.xlsx')
    ``` 

3. Load and Explore the Data Set
    1. Get the info
        ```python
        file.info()
        ``` 
    2. Print values
        ```python
        file.head(25)   # prints first 25 values.
        file.tail()          # prints last rows.
        ```
   3. Histogram
        ```python
            plt.figure(figsize=(10, 12))
            file[column].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')
        ```

4. Show Histogram
    1. Set labels and title
        ```python
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title('Instagram Success')
        ```
        - 
    2. Show the histogram
        ```python
            plt.show()
        ```
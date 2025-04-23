# Import necessary libraries
import pandas as pd
import numpy as np
import jupyter

# Function to clean and preprocess the dataset
def clean_data():
    
    # Load the dataset from a specified CSV file path
    df = pd.read_csv('/Users/prajaktapohare/Library/CloudStorage/OneDrive-RoshanDevs/Python Project/Dataset.csv')
    print(df)

    # Display the number of rows and columns in the dataset     
    print("Number of rows:" ,df.shape[0])
    print("Number of columns:" ,df.shape[1])

    print(df.info())


    #find the mean and mode of missing cell's columns
    mean_age = round(df['Age'].mean(), 0)
    print("Mean Age:", mean_age)

    mode_gender = df['Gender'].mode()[0]
    print("Mode gender:", mode_gender)

    mean_gpa = round(df['University_GPA'].mean(), 2)
    print("Mean U_GPA:", mean_gpa)

    mode_field = df['Field_of_Study'].mode()[0]
    print("Mode Field:", mode_field)

    mode_job = df['Current_Job_Level'].mode()[0]
    print("Mode job:", mode_job)

    #Replace empty cells with mean
    df['Age']=df['Age'].fillna(mean_age)
    df['Gender']=df['Gender'].fillna(mode_gender)
    df['University_GPA']=df['University_GPA'].fillna(mean_gpa)
    df['Field_of_Study']=df['Field_of_Study'].fillna(mode_field)
    df['Current_Job_Level']=df['Current_Job_Level'].fillna(mode_job)

    # Check the updated dataset info to verify missing values are handled
    print(df.info())

    #Top 10 values
    print(df.head(10))

    #Last 10 values
    print(df.tail(10))

    # Identify rows where the 'Starting_Salary' column contains a '$' symbol
    mask = df['Starting_Salary'].astype(str).str.contains('$', regex=False)
    cells_with_symbol = df.loc[mask, ['Starting_Salary']]
    print(cells_with_symbol)

    # Print the problematic rows containing '$'

    for index, value in df.loc[mask, 'Starting_Salary'].items():
        print(f"Row {index}, Cell Value: {value}")

    df['Starting_Salary']=df['Starting_Salary'].replace('[$]','',regex=True)
    df['Starting_Salary']=df['Starting_Salary'].replace('[,]','',regex=True)

    # Convert to float or int
    df['Starting_Salary'] = pd.to_numeric(df['Starting_Salary'], errors='coerce')

    #Cross check
    print("Check the data:", df.loc[12, 'Starting_Salary'], ",", df.loc[94, 'Starting_Salary'])

    #Find the row having 'Engineer'
    mask = df['Field_of_Study'].astype(str).str.fullmatch("Engineer")
    exact_matches = df[mask]
    print(exact_matches)


    df['Field_of_Study']=df['Field_of_Study'].replace({'Engineer':'Engineering'})

    #Cross check
    print("Check the field:", df.loc[12, 'Field_of_Study'], ",", df.loc[24, 'Field_of_Study'])
    
    # Cap salaries above the 95th percentile to reduce the impact of outliers
    sales_cap = df['Starting_Salary'].quantile(0.95)
    print(sales_cap)

    df['Starting_Salary'] = np.where(df['Starting_Salary'] > sales_cap, sales_cap, df['Starting_Salary'])
    print(df)
    
    return df

# Call the function to clean the dataset
clean_data()
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import the data cleaning function from another module
from DataCleaning import clean_data
df = clean_data()

# Function to generate visualizations from the cleaned data
def visualize_data():
    
    #create a bar chart
    # Group data by Field and Gender, summing Job Offers
    Offers = df.groupby(['Field_of_Study','Gender'])['Job_Offers'].sum().reset_index().sort_values(by='Job_Offers',ascending=False)
    print(Offers)
    plt.figure(figsize=(14,6))
    sns.barplot(data=Offers, x='Field_of_Study', y='Job_Offers', hue='Gender')

    # Add plot titles and labels
    plt.title('Job Offers by Field and Gender', fontweight ='bold')
    plt.xlabel('Field of Study')
    plt.ylabel('Number of Job Offers')
    plt.show()

    #boxplot
    plt.figure(figsize=(12,6))
    # Create boxplot with mean markers and hue based on Job Level
    sns.boxplot(x='Field_of_Study', y='Starting_Salary', data = df,showmeans ='True', 
                hue='Current_Job_Level', meanprops={"marker":"o", "markerfacecolor":"white",
                "markersize":"5", "markeredgecolor":"grey"})

    # Add titles and labels
    plt.title('Salary by Field', fontweight ='bold')
    plt.xlabel('Field')
    plt.ylabel('Salary')
    plt.tight_layout()
    plt.show()


    #Create a pie chart
    # Aggregate Projects and Internships by Field
    Sales=df.groupby(['Field_of_Study'])[['Projects_Completed','Internships_Completed']].sum().reset_index()
    print(Sales)

    Field = Sales['Field_of_Study']
    Projects = Sales['Projects_Completed']
    Internships = Sales['Internships_Completed']

    fig, axs = plt.subplots(1,2,figsize =(10,7))

    # Pie chart for Projects
    axs[0].pie(Projects, labels=Field, autopct ='%1.1f%%', startangle=90)
    axs[0].set_title('Projects by Field')

    # Pie chart for Internships
    axs[1].pie(Internships, labels=Field, autopct ='%1.1f%%', startangle=90)
    axs[1].set_title('Internships by Field')

    plt.show()
    
    return df

# Call the function to display visualizations
visualize_data()
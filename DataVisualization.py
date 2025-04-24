# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import the data cleaning function from another module

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

    #Create a Funnel
    # Define the labels for different job levels
    labels =["Entry", "Executive", "Mid", "Senior"]
    
    # Count how many individuals fall under each job level
    level_counts = df['Current_Job_Level'].value_counts()
    
    df1 = pd.DataFrame({"Labels": labels, "Value": level_counts})
    
    # Set a clean, minimalistic visual style for the plot
    with plt.style.context("fivethirtyeight"):
        fig = plt.figure(figsize=(10,8))
        
        colors = ["#a9d18e", "#ffc000", "#ed7d31", "#5b9bd5"]
        plt.fill_betweenx(y=[1, 3.8], x1=[10,12], x2=[8,6], color=colors[0]);
        plt.fill_betweenx(y=[4, 6.8], x1=[12,14], x2=[6,4], color=colors[1]);
        plt.fill_betweenx(y=[7, 9.8], x1=[14,16], x2=[4,2], facecolor=colors[2], edgecolor="black", linewidth=5);
        plt.fill_betweenx(y=[10, 12.8], x1=[16,18], x2=[2,0], color=colors[3]);
        
        plt.xticks([],[]);
        plt.yticks([2,5,8,11], df1["Labels"][::-1]);
        
        for y, value in zip([2,5,8,11], df1["Value"][::-1]):
            plt.text(9, y, value, fontsize=16, fontweight="bold", color="white", ha="center");
        
        plt.grid(visible=False);
        
        # Add label and title
        plt.ylabel("Stages");
        plt.title("Sales Funnel", loc="center", fontsize=25, fontweight="bold");
        plt.show()

# Call the function to display visualizations
visualize_data()
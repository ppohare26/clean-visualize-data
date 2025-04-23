# clean-visualize-data
This project performs data cleaning and visualization on a dataset containing information about individuals' educational backgrounds and employment outcomes. It is divided into two main parts: data cleaning and data visualization.


---

## 📊 Part 1: Data Cleaning (`DataCleaning.py`)

This script reads a raw CSV dataset and performs the following:

- Loads the dataset using `pandas`
- Displays basic information such as row/column count and missing values
- Calculates:
  - Mean of **Age** and **University GPA**
  - Mode of **Gender**, **Field of Study**, and **Current Job Level**
- Replaces missing values using calculated statistics
- Cleans `Starting_Salary` by removing symbols (`$`, `,`) and converting to numeric
- Corrects field naming inconsistencies (e.g., changing "Engineer" to "Engineering")
- Caps extreme salaries above the 95th percentile to reduce skew

The cleaned DataFrame is returned and used by the visualization module.

---

## 📈 Part 2: Data Visualization (`DataVisualization.py`)

This script imports the cleaned dataset and performs various visualizations:

1. **Bar Chart**  
   - Shows total job offers by field of study and gender
2. **Box Plot**  
   - Displays salary distributions across fields of study, grouped by current job level
3. **Pie Charts**  
   - One for total projects completed by field  
   - One for total internships completed by field

All visualizations are built using `matplotlib` and `plotly`.

---

## 🚀 How to Run

1. Ensure Python is installed (recommended: Python 3.9+)
2. Install required libraries:

```bash
pip install pandas numpy matplotlib plotly
```
3. Save your dataset as Dataset.csv in the same directory.
4. Run the scripts

### Data Quality Validation Project

This project focuses on automated data quality validation for three datasets: `customers`, `products`, and `transactions`. 
The goal is to detect and report common data issues that may affect analytics or reporting.

### Business Context

Company XYZ sells products online and collects transactional data from various sources. This data
goes into a data warehouse and is used by the analytics department to create reports and predictive
models. Recently, a number of inaccuracies have been noticed in the reports due to data errors such
as missing values, duplicate records, incorrect date formats, etc.
The task is to design a process that automatically detects and reports on data quality issues.

### Solution Overview

The solution includes:

- **Initial Exploration**: Performed exploratory data analysis (EDA) on all datasets. Some data discrepancies were identified immediately, even before running quality checks.
- **Data Analysis**: Reviewing the structure and content of each dataset.
- **Data Quality Checks**: Implementing rules to identify:
  - Missing values
  - Duplicate rows
  - Invalid date formats
  - Negative or incorrect numeric values
  - Invalid email formats
  - Referential integrity issues
- **Automation**: A Python script runs all checks and generates a detailed CSV report.
- **SQL Validation**: Additional SQL queries were used to confirm issues and analyze relationships between datasets.
- **Insights**: Key findings are summarized based on the results of checks.

All insights and recommendations can be found in the folder **Solution proposal and insights**.


### Output

- A report named `data_quality_report.csv` is generated with the status of each check.
- All results are printed for review in the console.


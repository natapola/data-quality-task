#!/usr/bin/env python
# coding: utf-8

# ### Task for Data Quality Engineer

# #### Data Quality Checks
# This notebook performs data validation on customer, product, and transaction datasets.

# In[1]:


import pandas as pd


# In[2]:


customer_df = pd.read_csv("C:/Users/IntelliBoard/Downloads/Task for Data Quality Engineer/Task for Data Quality Engineer/Data/customers.csv", sep=';')
products_df = pd.read_csv("C:/Users/IntelliBoard/Downloads/Task for Data Quality Engineer/Task for Data Quality Engineer/Data/products.csv", sep=';')
transactions_df = pd.read_csv("C:/Users/IntelliBoard/Downloads/Task for Data Quality Engineer/Task for Data Quality Engineer/Data/transactions.csv", sep=';')


# In[3]:


customer_df.head(10)


# In[4]:


products_df.head(10)


# In[5]:


transactions_df.head(10)


# In[8]:


import re

# Load CSV files
customers= pd.read_csv("C:/Users/IntelliBoard/Downloads/Task for Data Quality Engineer/Task for Data Quality Engineer/Data/customers.csv", sep=';')
products = pd.read_csv("C:/Users/IntelliBoard/Downloads/Task for Data Quality Engineer/Task for Data Quality Engineer/Data/products.csv", sep=';')
transactions = pd.read_csv("C:/Users/IntelliBoard/Downloads/Task for Data Quality Engineer/Task for Data Quality Engineer/Data/transactions.csv", sep=';')



# Store tables in a dictionary
tables = {
    "transactions": transactions,
    "products": products,
    "customers": customers
}



# Create an empty list to store the report
report = []

def add_report(table, check, status, comment):
    row = {
        "Table": table,
        "Check": check,
        "Status": status,
        "Comment": comment
    }
    report.append(row)


    
# Check for missing values
def check_nulls(table_name, data_in_table):
    null_counts = data_in_table.isnull().sum()
    for column, count in null_counts.items():
        if count > 0:
            add_report(table_name, f"Missing values in '{column}'", "FAIL", f"{count} null values")
        else:
            add_report(table_name, f"Missing values in '{column}'", "OK", "No nulls")


            

# Check for duplicate rows
def check_duplicates(table_name, data_in_table):
    duplicate_count = data_in_table.duplicated().sum()
    if duplicate_count > 0:
        add_report(table_name, "Duplicate rows", "FAIL", f"{duplicate_count} duplicates found")
    else:
        add_report(table_name, "Duplicate rows", "OK", "No duplicates")      


        
        
# Check if date column has valid format
def check_date_format(table_name, data_in_table, column):
    invalid_count = 0

    for value in data_in_table[column]:
        try:
            pd.to_datetime(value)
        except:
            invalid_count += 1

    if invalid_count > 0:
        add_report(table_name, f"Date format in '{column}'", "FAIL", f"{invalid_count} invalid date values")
    else:
        add_report(table_name, f"Date format in '{column}'", "OK", "Valid format")



        
        
# Check if price and amount are greater than 0
def check_positive_values():
    if "price" in products.columns:
        count = products[products["price"] <= 0].shape[0]
        if count > 0:
            add_report("products", "price > 0", "FAIL", f"{count} non-positive prices")
        else:
            add_report("products", "price > 0", "OK", "All prices are positive")
    else:
        add_report("products", "price > 0", "SKIPPED", "Column not found")

    if "amount" in transactions.columns:
        count = transactions[transactions["amount"] <= 0].shape[0]
        if count > 0:
            add_report("transactions", "amount > 0", "FAIL", f"{count} non-positive amounts")
        else:
            add_report("transactions", "amount > 0", "OK", "All amounts are positive")
    else:
        add_report("transactions", "amount > 0", "SKIPPED", "Column not found")


        

        
# Check foreign keys: product_id and customer_id in transactions
def check_foreign_keys():
    # Check product_id exists in products
    if "product_id" in transactions.columns and "product_id" in products.columns:
        for_product_check = transactions["product_id"].isin(products["product_id"])
        if not for_product_check.all():
            missing_count = (~for_product_check).sum()
            add_report("transactions", "product_id in products", "FAIL", f"{missing_count} missing")
        else:
            add_report("transactions", "product_id in products", "OK", "All product_id values exist in products")
    else:
        add_report("transactions", "product_id in products", "SKIPPED", "Column not found")

    # Check customer_id exists in customers
    if "customer_id" in transactions.columns and "customer_id" in customers.columns:
        for_customer_check = transactions["customer_id"].isin(customers["customer_id"])
        if not for_customer_check.all():
            missing_count = (~for_customer_check).sum()
            add_report("transactions", "customer_id in customers", "FAIL", f"{missing_count} missing")
        else:
            add_report("transactions", "customer_id in customers", "OK", "All customer_id values exist in customers")
    else:
        add_report("transactions", "customer_id in customers", "SKIPPED", "Column not found")




        
        
# Check if email addresses have valid format
def check_emails():
    email_column = "email"
    if email_column in customers.columns:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        invalid_emails = customers[~customers[email_column].str.match(pattern, na=False)]
        count = invalid_emails.shape[0]
        if count > 0:
            add_report("customers", "Valid email format", "FAIL", f"{count} invalid emails")
        else:
            add_report("customers", "Valid email format", "OK", "All emails valid")
    else:
        add_report("customers", "Valid email format", "SKIPPED", "Column not found")

        

        
        
 # Run all checks
for table_name, data_in_table in tables.items():
    check_nulls(table_name, data_in_table)
    check_duplicates(table_name, data_in_table)

check_date_format("transactions", transactions, "transaction_date")
check_positive_values()
check_foreign_keys()
check_emails()



# Save the report to a CSV file
report_df = pd.DataFrame(report)
report_df.to_csv("data_quality_report.csv", index=False)
print("Report saved as 'data_quality_report.csv'")
print(report_df)


# In[ ]:





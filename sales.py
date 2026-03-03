# ==========================================
# END-TO-END BUSINESS INTELLIGENCE SYSTEM
# Data Warehouse + ETL + OLAP (Single Cell)
# Dataset: Sample - Superstore.csv
# ==========================================

# pip install pandas sqlalchemy sqlite3

import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# ==========================================
# 1. Load Dataset
# ==========================================
df = pd.read_csv("/kaggle/input/datasets/vivek468/superstore-dataset-final/Sample - Superstore.csv", encoding='latin1')

print("Dataset Shape:", df.shape)
print(df.head())

# ==========================================
# 2. Create SQLite Data Warehouse
# ==========================================
engine = create_engine("sqlite:///bi_datawarehouse.db")
conn = sqlite3.connect("bi_datawarehouse.db")

# ==========================================
# 3. Create Dimension Tables
# ==========================================

# Date Dimension
df['Order Date'] = pd.to_datetime(df['Order Date'])

dim_date = df[['Order Date']].drop_duplicates().copy()
dim_date['Year'] = dim_date['Order Date'].dt.year
dim_date['Month'] = dim_date['Order Date'].dt.month
dim_date['Day'] = dim_date['Order Date'].dt.day

# Customer Dimension
dim_customer = df[['Customer ID','Customer Name','Segment','City','Region']].drop_duplicates()

# Product Dimension
dim_product = df[['Product ID','Product Name','Category','Sub-Category']].drop_duplicates()

# ==========================================
# 4. Create Fact Table
# ==========================================

fact_sales = df[['Order Date','Customer ID','Product ID','Sales','Quantity','Profit']]

# ==========================================
# 5. Load into Data Warehouse
# ==========================================

dim_date.to_sql("dim_date", engine, if_exists="replace", index=False)
dim_customer.to_sql("dim_customer", engine, if_exists="replace", index=False)
dim_product.to_sql("dim_product", engine, if_exists="replace", index=False)
fact_sales.to_sql("fact_sales", engine, if_exists="replace", index=False)

print("Data Warehouse Created Successfully 🚀")

# ==========================================
# 6. OLAP Queries (Business Intelligence)
# ==========================================

# Total Sales by Region
query1 = """
SELECT c.Region, SUM(f.Sales) as Total_Sales
FROM fact_sales f
JOIN dim_customer c ON f.[Customer ID] = c.[Customer ID]
GROUP BY c.Region
"""

# Monthly Sales Trend
query2 = """
SELECT d.Month, SUM(f.Sales) as Monthly_Sales
FROM fact_sales f
JOIN dim_date d ON f.[Order Date] = d.[Order Date]
GROUP BY d.Month
ORDER BY d.Month
"""

# Top Products by Revenue
query3 = """
SELECT p.[Product Name], SUM(f.Sales) as Revenue
FROM fact_sales f
JOIN dim_product p ON f.[Product ID] = p.[Product ID]
GROUP BY p.[Product Name]
ORDER BY Revenue DESC
LIMIT 5
"""

print("\nTotal Sales by Region:")
print(pd.read_sql(query1, conn))

print("\nMonthly Sales Trend:")
print(pd.read_sql(query2, conn))

print("\nTop 5 Products by Revenue:")
print(pd.read_sql(query3, conn))

conn.close()

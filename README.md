# End-to-End-Business-Intelligence-Data-Warehouse-System-Using-Python-and-SQLite
End-to-End Business Intelligence & Data Warehouse System

## Project Overview

This project implements a complete Business Intelligence (BI) system using a retail sales dataset. It includes ETL processing, star schema data warehouse modeling, and OLAP queries for business analytics.

The system transforms raw retail transaction data into structured dimension and fact tables, enabling advanced business insights.

## Objectives

- Build a structured Data Warehouse using Star Schema
- Implement ETL pipeline using Python
- Perform OLAP queries for business insights
- Analyze regional sales performance
- Identify top revenue-generating products
- Track monthly sales trends

## Dataset Information

Dataset: Superstore Sales Dataset (Kaggle)

- Total Records: 9,994
- Features: 21 columns
- Includes:
  - Order Details
  - Customer Information
  - Product Information
  - Sales, Profit, Quantity
  - Regional Data

## 🏗️ Data Warehouse Architecture

### Star Schema Design

Fact Table:
- `fact_sales`

Dimension Tables:
- `dim_date`
- `dim_customer`
- `dim_product`

This schema enables efficient analytical queries and aggregation.

## Tech Stack

- Python
- Pandas
- SQLite
- SQLAlchemy
- SQL (OLAP Queries)

## ETL Process

1. Extract raw CSV data
2. Transform:
   - Create Date Dimension
   - Create Customer Dimension
   - Create Product Dimension
3. Load data into SQLite Data Warehouse
4. Execute analytical queries

## Business Insights Generated

### Total Sales by Region
- Identifies top-performing geographical regions

### Monthly Sales Trend
- Detects seasonal demand patterns
- Highlights Q4 peak performance

### Top 5 Products by Revenue
- Identifies high-value revenue drivers

## Sample KPIs Derived

- Total Revenue
- Total Profit
- Monthly Growth Trend
- Regional Performance
- Product-Level Revenue

## How to Run

1. Download dataset from Kaggle
2. Place `Sample - Superstore.csv` in project directory
3. Install dependencies:

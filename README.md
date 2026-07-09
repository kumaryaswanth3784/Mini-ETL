# 🚀 Mini ETL Pipeline using PySpark

## 📌 Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Apache PySpark.

## 🔧 Technologies Used

- Python
- Apache Spark (PySpark)
- CSV
- Parquet

## 📂 Dataset

- emp.csv
- dept.csv

## 🔄 ETL Workflow

1. Read Employee and Department CSV files
2. Remove duplicate employee records
3. Fill missing values
4. Join employee and department data
5. Apply transformations
   - Annual Salary
   - Bonus
   - Employee Name in Uppercase
   - Load Timestamp
6. Write the final output to Parquet format

## 📁 Project Structure

```
Mini-ETL/
│
├── emp.csv
├── dept.csv
├── mini_etl.py
├── requirements.txt
└── README.md
```

## ▶️ Run

```bash
pip install -r requirements.txt
python mini_etl.py
```

## 📊 Features

- Read CSV files
- Remove duplicate records
- Handle null values
- Join DataFrames
- Apply transformations
- Write output to Parquet

## 👨‍💻 Author

**Yaswanth Kumar**

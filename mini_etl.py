from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark Session
spark = SparkSession.builder \
    .appName("Mini ETL Pipeline") \
    .getOrCreate()

# ===========================
# Extract
# ===========================

emp_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("emp.csv")

dept_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("dept.csv")

print("Employee Data")
emp_df.show()

print("Department Data")
dept_df.show()

# ===========================
# Remove Duplicate Records
# ===========================

emp_df = emp_df.dropDuplicates(["EmpID"])

# ===========================
# Fill Null Values
# ===========================

emp_df = emp_df.fillna({
    "Name": "Unknown",
    "DeptID": 0,
    "Salary": 0
})

# ===========================
# Join DataFrames
# ===========================

final_df = emp_df.join(dept_df, "DeptID", "left")

# ===========================
# Transformations
# ===========================

final_df = final_df \
    .withColumn("AnnualSalary", col("Salary") * 12) \
    .withColumn("Bonus", round(col("Salary") * 0.10, 2)) \
    .withColumn("LoadDate", current_timestamp()) \
    .withColumn("EmployeeName", upper(col("Name")))

# ===========================
# Display Result
# ===========================

print("Final ETL Output")
final_df.show(truncate=False)

# ===========================
# Load
# ===========================

final_df.write \
    .mode("overwrite") \
    .parquet("Employee_Output")

print("ETL Pipeline Completed Successfully!")

spark.stop()
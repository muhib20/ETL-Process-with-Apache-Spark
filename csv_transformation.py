from pyspark.sql import SparkSession
from pyspark.sql.types import *

# Create SparkSession
spark = SparkSession.builder \
    .appName("CSV Transformation") \
    .getOrCreate()

# Define schema for the raw data
schema = StructType([
    StructField("ID", IntegerType(), nullable=True),
    StructField("Product", StringType(), nullable=True),
    StructField("Customer", StringType(), nullable=True),
    StructField("Quantity", IntegerType(), nullable=True),
    StructField("Sales", DoubleType(), nullable=True),
    StructField("Profit", DoubleType(), nullable=True),
    StructField("Discount", DoubleType(), nullable=True),
    StructField("Region", StringType(), nullable=True),
    StructField("Category", StringType(), nullable=True),
    StructField("ShippingCost", DoubleType(), nullable=True)
])

# Load CSV file into DataFrame with inferred schema and without assuming header
df = spark.read.csv("file:///home/cloud_user/Sample-Spreadsheet-10000-rows.csv", header=False, schema=schema)

# Display schema and sample data
df.printSchema()
df.show(5)

# Filter data based on quantity
transformed_df = df.filter(df["Quantity"] >= 30)

# Show transformed data
transformed_df.show()

# Stop SparkSession
spark.stop()



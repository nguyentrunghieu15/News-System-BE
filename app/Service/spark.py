from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
spark_master_url = "spark://172.23.0.9:7077"

# Create a Spark session with the specified master URL
# Rest of the code remains the same as mentioned in the previous response

# Specify the HDFS path to the CSV file
hdfs_path = "hdfs://172.23.0.4/news/app_data_articles_2024-01.csv"

spark = SparkSession.builder.master(spark_master_url).appName("Test Application").getOrCreate()

# # Define the schema
# schema = StructType([
#     StructField("source", StringType(), True),
#     StructField("author", StringType(), True),
#     StructField("title", StringType(), True),
#     StructField("description", StringType(), True),
#     StructField("url", StringType(), True),
#     StructField("urlToImage", StringType(), True),
#     StructField("publishedAt", StringType(), True),
#     StructField("content", StringType(), True),
# ])

# Read the CSV file into a DataFrame with the specified schema
articles_df = spark.read.csv(hdfs_path, header=True)

# Show the DataFrame
articles_df.show(truncate=False)
# Stop the Spark session
spark.stop()


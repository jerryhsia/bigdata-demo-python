from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.jars", "postgresql-42.3.1.jar") \
    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://10.36.248.27:8732/postgres") \
    .option("dbtable", "titanic") \
    .option("user", "postgres") \
    .option("password", "") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.show()
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext


def main(argv):
    input = argv[1]

    spark = SparkSession.builder.getOrCreate()
    df = spark.read.csv(input, header = "true")

    hotstreet = df.groupBy("source").count()

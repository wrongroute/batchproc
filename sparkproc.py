from pyspark.sql import SparkSession
# from pyspark.sql import SQLContext
import sys


def main(arg):
    input = arg

    spark = SparkSession.builder \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .master("local[*]") \
        .appName("Row Count") \
        .getOrCreate()

    df = spark.read.csv(input, header="true")
    hotstreet = df.groupBy("source").count()

    hotstreet.coalesce(1).write.csv("countstreet", sep=',', encoding='UTF-8', header='True')

 if __name__ == '__main__':
    sys.exit(main(sys.argv))

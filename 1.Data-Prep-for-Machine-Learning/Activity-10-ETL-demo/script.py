from datetime import datetime
# from pyspark.context import SparkContext
import pyspark.sql.functions as f
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from pyspark.sql import SparkSession

spark_context = SparkSession.builder.getOrCreate()
#spark_context = SparkContext.getOrCreate()

glue_context = GlueContext(spark_context)
session = glue_context.spark_session

glue_db = "awsmldb"
glue_tbl = "case_csv"
# s3://aws-ml-13123123/Case.csv
s3_write_path = "s3://aws-ml-13123123"

dt_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Start time:", dt_start)

dynamic_frame_read = glue_context.create_dynamic_frame.from_catalog(database = glue_db, table_name = glue_tbl)

data_frame = dynamic_frame_read.toDF()

data_frame = data_frame.select('province','city','infection_case','confirmed')


data_frame_aggregated = data_frame.groupBy(["province","city"]).agg(
    f.sum("confirmed").alias("TotalConfirmed"),\
    f.max("confirmed").alias("MaxFromOneConfirmedCase")\
    )

data_frame_aggregated.show(10)

data_frame_aggregated = data_frame_aggregated.repartition(1)

dynamic_frame_write = DynamicFrame.fromDF(data_frame_aggregated, glue_context, "dynamic_frame_write")

glue_context.write_dynamic_frame.from_options(
    frame = dynamic_frame_write,
    connection_type = "s3",
    connection_options = {
        "path": s3_write_path,
    },
    format = "csv"
)


dt_end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("End time:", dt_end)
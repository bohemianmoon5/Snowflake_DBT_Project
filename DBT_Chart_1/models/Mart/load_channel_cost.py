import snowflake.snowpark.functions as F
from snowflake.snowpark.functions import col, sum, datediff, coalesce, when, lit

def model(dbt, session):
    dbt.config(materialized="table")
    
    df = dbt.source("marketing", "P_CAMPAIGNS")
    
    cost_per_channel = (
        when(col("CHANNEL") == "Paid Search", 500)
        .when(col("CHANNEL") == "Display", 300)
        .when(col("CHANNEL") == "Social", 400)
        .when(col("CHANNEL") == "Email", 50)
        .when(col("CHANNEL") == "Influencer", 800)
        .when(col("CHANNEL") == "Video", 600)
        .when(col("CHANNEL") == "Mobile", 350)
        .otherwise(250)
    )
    
    result = df.group_by("CHANNEL").agg(
        sum(
            (datediff("day", col("START_DATE"), col("END_DATE")) + 1) * cost_per_channel
        ).alias("TOTAL_COST")
    ).order_by(col("TOTAL_COST").desc())
    
    return result
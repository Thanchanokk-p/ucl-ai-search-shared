## filter Next global clothing brand — due to vague meaning of 'next', added multiple filters for brand context

import duckdb

con = duckdb.connect()

con.execute("""
    CREATE OR REPLACE TABLE filtered AS
    SELECT *
    FROM 'parquet_data/*.parquet'
    WHERE 
        (
            LOWER(url) LIKE '%next.co%' OR
            LOWER(url) LIKE '%next.%' OR
            (
                LOWER(content) LIKE '%next%' AND 
                (
                    LOWER(content) LIKE '%clothing%' OR 
                    LOWER(content) LIKE '%shop%' OR 
                    LOWER(content) LIKE '%retail%' OR 
                    LOWER(content) LIKE '%fashion%'
                )
            )
        )
""")

con.execute("""
    COPY filtered TO 'filtered_data/next.parquet' (FORMAT PARQUET)
""")

print("Filtered + Exported to filtered_data/next.parquet")

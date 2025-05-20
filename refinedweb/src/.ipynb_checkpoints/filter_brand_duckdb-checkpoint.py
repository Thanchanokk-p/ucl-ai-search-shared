import duckdb

con = duckdb.connect()

# Filter and create table with better brand disambiguation
con.execute('''
    CREATE OR REPLACE TABLE filtered AS
    SELECT *
    FROM 'parquet_data/*.parquet'
    WHERE 
        -- H&M filters
        (
            LOWER(content) LIKE '%h&m%' OR 
            LOWER(url) LIKE '%hm.com%' OR 
            (LOWER(url) LIKE '%hm%' AND (
                LOWER(content) LIKE '%clothing%' OR 
                LOWER(content) LIKE '%fashion%' OR 
                LOWER(content) LIKE '%shop%'
            ))
        )
        OR
        -- Primark filters
        (
            LOWER(content) LIKE '%primark%' OR 
            LOWER(url) LIKE '%primark%'
        )
        OR
        -- Next filters
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
''')

# Save result
con.execute('''
    COPY filtered TO 'filtered_data/brand_analysis.parquet' (FORMAT PARQUET)
''')

print("Filtered + Exported to filtered_data/brand_analysis.parquet")

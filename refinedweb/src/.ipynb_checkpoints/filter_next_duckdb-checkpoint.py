import duckdb

con = duckdb.connect()

# Filter and create table
con.execute('''
    CREATE OR REPLACE TABLE filtered AS
    SELECT *
    FROM 'parquet_data/*.parquet'
    WHERE 
        LOWER(content) LIKE '%next%' OR LOWER(url) LIKE '%next%'
''')

# Save result
con.execute('''
    COPY filtered TO 'filtered_data/hm.parquet' (FORMAT PARQUET)
''')

print("Filtered + Exported to filtered_data/hm.parquet")
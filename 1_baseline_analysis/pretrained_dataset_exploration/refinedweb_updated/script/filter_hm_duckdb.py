import duckdb
from pathlib import Path

# Identify your project’s folders
SCRIPT_DIR   = Path(__file__).resolve().parent
#    └── the directory where this script lives (“…/script”)
PROJECT_ROOT = SCRIPT_DIR.parent
#    └── one level up (your project root, “…/refinedweb-shared”)
DATA_DIR     = PROJECT_ROOT / "data"
#    └── the “data” folder under your project root
PARQ_DIR     = DATA_DIR / "parquet_data"
#    └── the “parquet_data” subfolder containing your .parquet files
OUT_DIR      = DATA_DIR / "filtered_data"
#    └── the “filtered_data” folder where we want to write results

# Make sure the output directory exists
OUT_DIR.mkdir(parents=True, exist_ok=True)
#    └── create “data/filtered_data” (and any missing parents) if needed

# Open a DuckDB in-memory connection
con = duckdb.connect()

# Define and run a query to load all Parquet files, filter them, and store in a DuckDB table
con.execute(f"""
    CREATE OR REPLACE TABLE filtered_hm AS
    SELECT *
    FROM read_parquet('{PARQ_DIR.as_posix()}/*.parquet')
    WHERE
        (
            LOWER(content) LIKE '%h&m%' ESCAPE '\\'    OR
            LOWER(url)     LIKE '%h&m%' ESCAPE '\\'    OR
            LOWER(url)     LIKE '%hm.com%'             OR
            LOWER(url)     LIKE '%hm%'                 OR
            LOWER(url)     LIKE '%hm.%'
        )
        AND (
            LOWER(content) LIKE '%clothing%'           OR
            LOWER(content) LIKE '%fashion%'            OR
            LOWER(content) LIKE '%shop%'               OR
            LOWER(url)     LIKE '%hm.com%'
        )
""")


# Export the filtered results back out as a Parquet file
out_file = OUT_DIR / "hm.parquet"
con.execute(f"""
    COPY filtered_hm
    TO '{out_file.as_posix()}'
    (FORMAT PARQUET)
""")

print(f"Filtered + Exported to {out_file}")

con.close()

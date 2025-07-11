import duckdb
from pathlib import Path

# Folder structure
SCRIPT_DIR   = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR     = PROJECT_ROOT / "data"
PARQ_DIR     = DATA_DIR / "parquet_data"
OUT_DIR      = DATA_DIR / "filtered_data"

# Ensure output exists
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Open DuckDB
con = duckdb.connect()

# Filter Burberry
con.execute(f"""
    CREATE OR REPLACE TABLE filtered_burberry AS
    SELECT *
    FROM read_parquet('{PARQ_DIR.as_posix()}/*.parquet')
    WHERE
        (
            LOWER(content) LIKE '%burberry%'        OR
            LOWER(url)     LIKE '%burberry%'        OR
            LOWER(url)     LIKE '%burberry.com%'    OR
            LOWER(url)     LIKE '%burberry.%'
        )
""")

# Export
out_file = OUT_DIR / "burberry.parquet"
con.execute(f"""
    COPY filtered_burberry
    TO '{out_file.as_posix()}'
    (FORMAT PARQUET)
""")

print(f"Filtered + Exported to {out_file}")
con.close()

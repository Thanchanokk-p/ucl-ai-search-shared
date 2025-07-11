file_path="data/parquet_data/paths.txt"
output_dir="data/parquet_data"

# Optional: echo contents (for debugging)
cat "$file_path"

while read url; do
  filename=$(basename "$url")
  if [ -f "$output_dir/$filename" ]; then
    echo "Skipping $filename (already exists)"
  else
    echo "Downloading $filename"
    wget -O "$output_dir/$filename" "$url"
  fi
done < "$file_path"

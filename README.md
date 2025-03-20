# CSV to SQL Converter

This script converts CSV files from the `csv/` directory into SQL `CREATE TABLE` and `INSERT` statements, saving the output in the `sql/` directory.

## Directory Structure
```
project_root/
│-- csv/        # Place CSV files here
│-- sql/        # Generated SQL files are saved here
│-- script.py   # Python script to convert CSV to SQL
```

## Input Requirements
- CSV files should be placed in the `csv/` directory.
- The first row must contain column names.
- Ensure correct formatting (e.g., no empty headers).

## Usage
1. **Install Dependencies** (if not installed):
   ```sh
   pip install pandas
   ```
2. **Run the Script**:
   ```sh
   python script.py
   ```
3. **Output**:
   - The generated SQL file is saved in the `sql/` directory.
   - It is named after the CSV file (e.g., `csv/data.csv` → `sql/data.sql`).


## Next Steps
- Improve SQL type inference (e.g., `INTEGER` for `id`, `year`).
- Add error handling for incorrect CSV formats.
- Optimize bulk inserts for efficiency.
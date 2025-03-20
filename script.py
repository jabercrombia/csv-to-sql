import pandas as pd
import os
import glob


directory = "./csv/"

# find only csv file
csv_file_name = [os.path.basename(f) for f in glob.glob(directory + "/*.csv")]


csv_file_name = csv_file_name[0] if csv_file_name else None 

# Load CSV file
csv_file = csv_file_name.split('.')[0] 
csv_file_path = directory + csv_file_name
df = pd.read_csv(csv_file_path)

# Infer table name from file name (without extension)
table_name = csv_file.split('.')[0]

# Generate CREATE TABLE statement
def generate_create_table(df, table_name):
    create_stmt = f"CREATE TABLE {table_name} (\n"
    for column in df.columns:
        create_stmt += f"    {column} TEXT,\n"  # Defaulting to TEXT; modify as needed
    create_stmt = create_stmt.rstrip(",\n") + "\n);"
    return create_stmt

# Generate INSERT statements
def generate_insert_statements(df, table_name):
    insert_statements = []
    for _, row in df.iterrows():
        values = "', '".join(str(v).replace("'", "''") for v in row)
        insert_statements.append(f"INSERT INTO {table_name} VALUES ('{values}');")
    return insert_statements

# Generate SQL
create_table_sql = generate_create_table(df, table_name)
insert_statements_sql = "\n".join(generate_insert_statements(df, table_name))

# Save to file
with open(f"./sql/{table_name}.sql", "w") as f:
    f.write(create_table_sql + "\n\n" + insert_statements_sql)

print(f"SQL file '{table_name}.sql' generated successfully!")

from sqlalchemy import create_engine, text
from sqlalchemy.schema import CreateSchema
import pandas as pd

data_path = 'data/raw/games.csv'
opening_statistics_query = 'sql/gold/opening_statistics.sql'
result_statistics_query = 'sql/gold/result_statistics.sql'
time_control_statistics_query = 'sql/gold/time_control_statistics.sql'
create_silver_table_query = 'sql/silver/create_silver_table.sql'


df = pd.read_csv(data_path)

USERNAME = "postgres"
PASSWORD = "admin"
HOST = "localhost"
PORT = "5432"
DB_NAME = "lichess_analisys_db"

print("Creating engine... ", end="")
engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")
print("engine created succesfully\n")

def validate(df):
    print(f"All rows: {len(df)}")
    print(f"Unique game IDs: {df['id'].nunique()}")
    print(f"Duplicated game IDs: {df['id'].duplicated().sum()}")
    print(f"Fully duplicated rows: {df.duplicated().sum()}")
    print(f"Null cells: {df.isnull().sum().sum()}\n")

print("Raw data:")
validate(df)

print("Cleaning data...\n")
silver_df = df.drop_duplicates(subset=['id'], keep='first')

print("Silver layer data:")
validate(silver_df)

print("Creating silver schema and silver.gamnes table... ", end="")

with engine.begin() as con:
    with open(create_silver_table_query) as file:
        query = text(file.read())
        con.execute(query)

print("Silver schema and table created succesfully\n")

print("Loading data to silver.games table... ", end="")
silver_df.to_sql("games", engine, schema="silver", if_exists="replace", index=False)
print("succesfully loaded data to silver.games table\n")

print("Creating gold schema...", end="")
with engine.begin() as con:
    con.execute(CreateSchema("gold", if_not_exists=True))
print("Gold schema created succesfully\n")

print("Creating 3 tables for gold schema\n")

with engine.begin() as con:
    with open(opening_statistics_query) as file:
        query = text(file.read())
        con.execute(query)

with engine.begin() as con:
    with open(result_statistics_query) as file:
        query = text(file.read())
        con.execute(query)

with engine.begin() as con:
    with open(time_control_statistics_query) as file:
        query = text(file.read())
        con.execute(query)

print("Success!!")















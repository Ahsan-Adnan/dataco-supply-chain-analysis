import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgreadnan@localhost:5432/dataco_supply_chain")
df = pd.read_csv(r"D:\dataco-supply-chain\data\processed\dataco_clean.csv")
df.to_sql("dataco_orders", engine, if_exists="replace", index=False, chunksize=10000)
print("Loaded", len(df), "rows")
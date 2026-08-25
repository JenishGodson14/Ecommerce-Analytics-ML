import pandas as pd
from sqlalchemy import create_engine

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:1402@localhost:3306/ecommerce"
)

# Read cleaned CSV files
df1 = pd.read_csv("Dataset/Cleaned/channels.csv")
df2 = pd.read_csv("Dataset/Cleaned/deliveries.csv")
df3 = pd.read_csv("Dataset/Cleaned/drivers.csv")
df4 = pd.read_csv("Dataset/Cleaned/hubs.csv", encoding="latin1")
df5 = pd.read_csv("Dataset/Cleaned/orders.csv")
df6 = pd.read_csv("Dataset/Cleaned/payments.csv")
df7 = pd.read_csv("Dataset/Cleaned/stores.csv", encoding="latin1")

# Import into MySQL
df1.to_sql("channels", con=engine, if_exists="replace", index=False, chunksize=5000)
print("Channels imported")

df2.to_sql("deliveries", con=engine, if_exists="replace", index=False, chunksize=5000)
print("Deliveries imported")

df3.to_sql("drivers", con=engine, if_exists="replace", index=False, chunksize=5000)
print("Drivers imported")

df4.to_sql("hubs", con=engine, if_exists="replace", index=False, chunksize=5000)
print("Hubs imported")

df5.to_sql("orders", con=engine, if_exists="replace", index=False, chunksize=5000)
print("Orders imported")

df6.to_sql("payments", con=engine, if_exists="replace", index=False, chunksize=5000)
print("Payments imported")

df7.to_sql("stores", con=engine, if_exists="replace", index=False, chunksize=5000)
print("Stores imported")

# Test connection
with engine.connect() as connection:
    print("MySQL connection successful!")

# Close SQLAlchemy engine
engine.dispose()
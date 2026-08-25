import pandas as pd

df1 = pd.read_csv("Dataset\Raw\channels.csv")
df2 = pd.read_csv("Dataset\Raw\deliveries.csv")
df3 = pd.read_csv("Dataset\Raw\drivers.csv")
df4 = pd.read_csv("Dataset\Raw\hubs.csv",encoding="latin1")
df5 = pd.read_csv("Dataset\Raw\orders.csv")
df6 = pd.read_csv("Dataset\Raw\payments.csv")
df7 = pd.read_csv("Dataset\Raw\stores.csv",encoding="latin1")

# print(df1.head())
# print(df1.shape)
# print(df1.columns)
# print(df1.dtypes)
# print(df1.isnull().sum())
# print(df1.duplicated().sum())
# print(df1["channel_id"].duplicated().sum())


print(df2.head())
print(df2.shape)
print(df2.columns)
print(df2.dtypes)
print(df2.isnull().sum())
print(df2.duplicated().sum())
print(df2["delivery_id"].duplicated().sum())


# print(df3.head())
# print(df3.shape)
# print(df3.columns)
# print(df3.dtypes)
# print(df3.isnull().sum())
# print(df3.duplicated().sum())
# print(df3["driver_id"].duplicated().sum())


# print(df4.head())
# print(df4.shape)
# print(df4.columns)
# print(df4.dtypes)
# print(df4.isnull().sum())
# print(df4.duplicated().sum())
# print(df4["hub_id"].duplicated().sum())


# print(df5.head())
# print(df5.shape)
# print(df5.columns)
# print(df5.dtypes)
# print(df5.isnull().sum())
# print(df5.duplicated().sum())
# print(df5["order_id"].duplicated().sum())


# print(df6.head())
# print(df6.shape)
# print(df6.columns)
# print(df6.dtypes)
# print(df6.isnull().sum())
# print(df6.duplicated().sum())
# print(df6["payment_id"].duplicated().sum())


# print(df7.head())
# print(df7.shape)
# print(df7.columns)
# print(df7.dtypes)
# print(df7.isnull().sum())
# print(df7.duplicated().sum())
# print(df7["store_id"].duplicated().sum())



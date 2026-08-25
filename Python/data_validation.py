import pandas as pd

df1 = pd.read_csv(
    "Dataset/Cleaned/channels.csv",
    encoding="latin1"
)

print(df1.shape)
print(df1.isnull().sum())
print(df1.duplicated().sum())

df2 = pd.read_csv(
    "Dataset/Cleaned/deliveries.csv",
    encoding="latin1"
)

print(df2.shape)
print(df2.isnull().sum())
print(df2.duplicated().sum())

df3 = pd.read_csv(
    "Dataset/Cleaned/drivers.csv",
    encoding="latin1"
)

print(df3.shape)
print(df3.isnull().sum())
print(df3.duplicated().sum())

df4 = pd.read_csv(
    "Dataset/Cleaned/hubs.csv",
    encoding="latin1"
)

print(df4.shape)
print(df4.isnull().sum())
print(df4.duplicated().sum())

df5 = pd.read_csv(
    "Dataset/Cleaned/orders.csv",
    encoding="latin1"
)

print(df5.shape)
print(df5.isnull().sum())
print(df5.duplicated().sum())

df6 = pd.read_csv(
    "Dataset/Cleaned/payments.csv",
    encoding="latin1"
)

print(df6.shape)
print(df6.isnull().sum())
print(df6.duplicated().sum())

df7 = pd.read_csv(
    "Dataset/Cleaned/stores.csv",
    encoding="latin1"
)

print(df7.shape)
print(df7.isnull().sum())
print(df7.duplicated().sum())


print(df5[
    [
        "order_id",
        "store_id",
        "channel_id",
        "payment_order_id",
        "delivery_order_id"
    ]
].head())

print(
    (df5["order_id"] == df5["payment_order_id"]).value_counts()
)

print(
    (df5["order_id"] == df5["delivery_order_id"]).value_counts()
)

print(
    df5["store_id"].isin(df7["store_id"]).value_counts()
)

print(
    df5["channel_id"].isin(df1["channel_id"]).value_counts()
)

print(
    df2["driver_id"].dropna().isin(df3["driver_id"]).value_counts()
)

print(
    df7["hub_id"].isin(df4["hub_id"]).value_counts()
)


print(df7["store_segment"].unique())
print(df1["channel_name"].unique())
print(df1["channel_type"].unique())
print(df3["driver_type"].unique())
print(df3["driver_modal"].unique())
print(df4["hub_city"].unique())
print(df4["hub_state"].unique())
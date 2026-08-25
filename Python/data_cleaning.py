import pandas as pd



df1 = pd.read_csv("Dataset/Raw/channels.csv")

df1.to_csv("Dataset/Cleaned/channels.csv", index=False)

print("channels.csv cleaned and saved")


df2 = pd.read_csv("Dataset/Raw/deliveries.csv")

print(df2["delivery_distance_meters"].describe())

df2["delivery_distance_meters"] = df2["delivery_distance_meters"].fillna(df2["delivery_distance_meters"].median())

df2.to_csv("Dataset/Cleaned/deliveries.csv", index=False)

print("deliveries.csv cleaned and saved")


df3 = pd.read_csv("Dataset/Raw/drivers.csv")

df3.to_csv("Dataset/Cleaned/drivers.csv", index=False)

print("drivers.csv cleaned and saved")

df4 = pd.read_csv("Dataset/Raw/hubs.csv",encoding="latin1")

df4.to_csv("Dataset/Cleaned/hubs.csv", index=False)

print("hubs.csv cleaned and saved")

df5 = pd.read_csv("Dataset/Raw/orders.csv")

print(df5["order_status"].value_counts())

print(pd.crosstab(
    df5["order_status"],
    df5["order_moment_delivered"].isnull()
))

print(pd.crosstab(
    df5["order_status"],
    df5["order_moment_finished"].isnull()
))

print(pd.crosstab(
    df5["order_status"],
    df5["order_moment_accepted"].isnull()
))

print(pd.crosstab(
    df5["order_status"],
    df5["order_moment_ready"].isnull()
))

print(pd.crosstab(
    df5["order_status"],
    df5["order_moment_collected"].isnull()
))

print(pd.crosstab(
    df5["order_status"],
    df5["order_moment_in_expedition"].isnull()
))

print(pd.crosstab(
    df5["order_status"],
    df5["order_moment_delivering"].isnull()
))

print(df5["order_delivery_cost"].describe())

df5["order_delivery_cost"] = df5["order_delivery_cost"].fillna(df5["order_delivery_cost"].median())

print(df5["order_delivery_cost"].isnull().sum())

print(df5["order_metric_collected_time"].describe())

df5.loc[df5["order_metric_collected_time"] < 0, "order_metric_collected_time"] = None

print((df5["order_metric_collected_time"] < 0).sum())

df5["order_metric_collected_time"] = df5["order_metric_collected_time"].fillna(df5["order_metric_collected_time"].median())

print(df5["order_metric_collected_time"].isnull().sum())

print(df5["order_metric_paused_time"].describe())
print((df5["order_metric_paused_time"] < 0).sum())
df5.loc[
    df5["order_metric_paused_time"] < 0,
    "order_metric_paused_time"
] = None

df5["order_metric_paused_time"] = df5[
    "order_metric_paused_time"
].fillna(
    df5["order_metric_paused_time"].median()
)
print(df5["order_metric_paused_time"].isnull().sum())
print((df5["order_metric_paused_time"] < 0).sum())

print(df5["order_metric_production_time"].describe())
print((df5["order_metric_production_time"] < 0).sum())

df5["order_metric_production_time"] = df5[
    "order_metric_production_time"
].fillna(
    df5["order_metric_production_time"].median()
)

print(df5["order_metric_production_time"].isnull().sum())

print(df5["order_metric_walking_time"].describe())
print((df5["order_metric_walking_time"] < 0).sum())
df5.loc[df5["order_metric_walking_time"] < 0 ,"order_metric_walking_time"] = None
df5["order_metric_walking_time"] = df5[
    "order_metric_walking_time"
].fillna(
    df5["order_metric_walking_time"].median()
)

print(df5["order_metric_walking_time"].isnull().sum())
print((df5["order_metric_walking_time"] < 0).sum())

print(df5["order_metric_expediton_speed_time"].describe())
print((df5["order_metric_expediton_speed_time"] < 0).sum())
df5.loc[df5["order_metric_expediton_speed_time"] < 0,"order_metric_expediton_speed_time"] = None
df5["order_metric_expediton_speed_time"] = df5[
    "order_metric_expediton_speed_time"
].fillna(
    df5["order_metric_expediton_speed_time"].median()
)
print(df5["order_metric_expediton_speed_time"].isnull().sum())
print((df5["order_metric_expediton_speed_time"] < 0).sum())

print(df5["order_metric_transit_time"].describe())
print((df5["order_metric_transit_time"] < 0).sum())
df5.loc[
    df5["order_metric_transit_time"] < 0,
    "order_metric_transit_time"
] = None
df5["order_metric_transit_time"] = df5[
    "order_metric_transit_time"
].fillna(
    df5["order_metric_transit_time"].median()
)
print(df5["order_metric_transit_time"].isnull().sum())
print((df5["order_metric_transit_time"] < 0).sum())


print(df5["order_metric_cycle_time"].describe())
df5["order_metric_cycle_time"] = df5[
    "order_metric_cycle_time"
].fillna(
    df5["order_metric_cycle_time"].median()
)
print(df5["order_metric_cycle_time"].isnull().sum())

print(df5.isnull().sum())

df5.to_csv("Dataset/Cleaned/orders.csv", index=False)

print("orders.csv cleaned and saved")

df6 = pd.read_csv("Dataset/Raw/payments.csv")

print(df6["payment_fee"].describe())

df6["payment_fee"] = df6["payment_fee"].fillna(
    df6["payment_fee"].median()
)

print(df6["payment_fee"].isnull().sum())

df6.to_csv(
    "Dataset/Cleaned/payments.csv",
    index=False
)

print("payments.csv cleaned and saved")

df7 = pd.read_csv("Dataset/Raw/stores.csv",encoding="latin1")

print(df7["store_plan_price"].describe())

df7["store_plan_price"] = df7["store_plan_price"].fillna(
    df7["store_plan_price"].median()
)
print(df7["store_plan_price"].isnull().sum())

df7["store_plan_price"] = df7["store_plan_price"].fillna(
    df7["store_plan_price"].median()
)

print(df7[df7["store_latitude"].isnull() | df7["store_longitude"].isnull()])


hubs = pd.read_csv("Dataset/Raw/hubs.csv",encoding="latin1")

print(hubs[hubs["hub_id"].isin(df7.loc[
    df7["store_latitude"].isnull(),
    "hub_id"
])][["hub_id", "hub_latitude", "hub_longitude"]])

hub_lat = hubs.set_index("hub_id")["hub_latitude"]

df7["store_latitude"] = df7["store_latitude"].fillna(
    df7["hub_id"].map(hub_lat)
)

hub_lon = hubs.set_index("hub_id")["hub_longitude"]

df7["store_longitude"] = df7["store_longitude"].fillna(
    df7["hub_id"].map(hub_lon)
)

print(df7["store_latitude"].isnull().sum())
print(df7["store_longitude"].isnull().sum())

df7.to_csv(
    "Dataset/Cleaned/stores.csv",
    index=False
)


print(df1.nunique())
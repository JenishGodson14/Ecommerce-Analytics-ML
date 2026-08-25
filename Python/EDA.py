import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df1 = pd.read_csv("Dataset/Cleaned/channels.csv")
df2 = pd.read_csv("Dataset/Cleaned/deliveries.csv")
df3 = pd.read_csv("Dataset/Cleaned/drivers.csv")
df4 = pd.read_csv("Dataset/Cleaned/hubs.csv",encoding="latin1")
df5 = pd.read_csv("Dataset/Cleaned/orders.csv")
df6 = pd.read_csv("Dataset/Cleaned/payments.csv")
df7 = pd.read_csv("Dataset/Cleaned/stores.csv",encoding="latin1")


print(df5.shape)
print(df5.columns)
print(df5.dtypes)

print(df5.describe())

print(df5["order_status"].value_counts(normalize=True)*100)


print("Total Revenue:", df5["order_amount"].sum())
print("Average Order Value:", df5["order_amount"].mean())

print(df5["order_amount"].describe())

print(
    df5[["order_id", "order_amount"]]
    .sort_values("order_amount", ascending=False)
    .head(10)
)

print(
    df5.groupby("order_status")["order_amount"].agg(
        ["count", "mean", "median", "min", "max"]
    )
)

print(
    df5.groupby("order_created_month")["order_amount"]
    .agg(["count", "sum"])
)

print(
    df5["order_created_hour"]
    .value_counts()
    .sort_index()
)

print(
    df5["order_created_day"]
    .value_counts()
    .sort_index()
)

print(
    df5["order_created_year"]
    .value_counts()
    .sort_index()
)

print(
    df5.groupby("order_created_month")["order_amount"]
    .mean()
)


print(
    df5.groupby("order_created_month")["order_amount"]
    .sum()
)

print(df5["order_delivery_fee"].describe())

print(df5["order_delivery_cost"].describe())

print(
    df5[
        ["order_delivery_fee", "order_delivery_cost"]
    ].describe()
)

metric_columns = [
    "order_metric_collected_time",
    "order_metric_paused_time",
    "order_metric_production_time",
    "order_metric_walking_time",
    "order_metric_expediton_speed_time",
    "order_metric_transit_time",
    "order_metric_cycle_time"
]

print(df5[metric_columns].describe())

print(df5[metric_columns].mean())

print(
    df5[
        [
            "order_amount",
            "order_delivery_fee",
            "order_delivery_cost",
            "order_metric_cycle_time",
            "order_metric_transit_time",
            "order_metric_production_time"
        ]
    ].corr()
)

print(df3["driver_id"].nunique())

order_status = df5["order_status"].value_counts()

plt.figure(figsize=(7, 5))

order_status.plot(kind="bar")

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)

plt.show()

monthly_orders = df5.groupby("order_created_month").size()

plt.figure(figsize=(8, 5))

monthly_orders.plot(kind="bar")

plt.title("Orders by Month")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)

plt.show()

monthly_revenue = df5.groupby(
    "order_created_month"
)["order_amount"].sum()

plt.figure(figsize=(8, 5))

monthly_revenue.plot(kind="bar")

plt.title("Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)

plt.show()

hourly_orders = df5.groupby("order_created_hour").size()

plt.figure(figsize=(10, 5))

hourly_orders.plot(kind="bar")

plt.title("Orders by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)

plt.show()

hourly_revenue = df5.groupby(
    "order_created_hour"
)["order_amount"].sum()

plt.figure(figsize=(10, 5))

hourly_revenue.plot(kind="bar")

plt.title("Revenue by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)

plt.show()

plt.figure(figsize=(10, 5))

plt.hist(
    df5["order_amount"],
    bins=50
)

plt.title("Order Amount Distribution")
plt.xlabel("Order Amount")
plt.ylabel("Frequency")

plt.show()


plt.figure(figsize=(10, 5))

plt.hist(
    df5["order_metric_cycle_time"],
    bins=50
)

plt.title("Order Cycle Time Distribution")
plt.xlabel("Cycle Time")
plt.ylabel("Frequency")

plt.show()


plt.figure(figsize=(10, 5))

plt.hist(
    df2["delivery_distance_meters"],
    bins=50
)

plt.title("Delivery Distance Distribution")
plt.xlabel("Distance (meters)")
plt.ylabel("Frequency")

plt.show()

plt.figure(figsize=(8, 5))

df6["payment_method"].value_counts().plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Payments")
plt.xticks(rotation=45)

plt.show()


store_segment = df7["store_segment"].value_counts()

plt.figure(figsize=(8, 5))

store_segment.plot(kind="bar")

plt.title("Store Segment Distribution")
plt.xlabel("Store Segment")
plt.ylabel("Number of Stores")
plt.xticks(rotation=45)

plt.show()

driver_type = df3["driver_type"].value_counts()

plt.figure(figsize=(8, 5))

driver_type.plot(kind="bar")

plt.title("Driver Type Distribution")
plt.xlabel("Driver Type")
plt.ylabel("Number of Drivers")
plt.xticks(rotation=45)

plt.show()


hub_state = df4["hub_state"].value_counts()
plt.figure(figsize=(10, 5))

hub_state.plot(kind="bar")

plt.title("Hub Distribution by State")
plt.xlabel("State")
plt.ylabel("Number of Hubs")
plt.xticks(rotation=45)

plt.show()

numeric_columns = [
    "order_amount",
    "order_delivery_fee",
    "order_delivery_cost",
    "order_metric_collected_time",
    "order_metric_paused_time",
    "order_metric_production_time",
    "order_metric_walking_time",
    "order_metric_expediton_speed_time",
    "order_metric_transit_time",
    "order_metric_cycle_time"
]

plt.figure(figsize=(12, 8))

sns.heatmap(
    df5[numeric_columns].corr(),
    annot=True,
    fmt=".2f"
)

plt.title("Order Metrics Correlation Heatmap")

plt.show()

print(df1.shape)
print(df2.shape)
print(df3.shape)
print(df4.shape)
print(df5.shape)
print(df6.shape)
print(df7.shape)
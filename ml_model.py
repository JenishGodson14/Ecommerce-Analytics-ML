import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import joblib


engine = create_engine(
    "mysql+pymysql://root:1402@localhost/ecommerce"
)

query = "SELECT * FROM final_orders"

df = pd.read_sql(query, engine)

print(df.shape)
print(df.head())

print(df["order_status"].value_counts())

le = LabelEncoder()

df['order_status'] = le.fit_transform(df["order_status"])


categorical = df[[
    "store_segment",
    "channel_name",
    "channel_type",
    "driver_type",
    "driver_modal",
    "hub_city",
    "hub_state"
]]

encode = OneHotEncoder(handle_unknown="ignore",
                       sparse_output=False)

x_encode = encode.fit_transform(categorical)

print("Label encoding completed!")

numerical_features = [
    "order_amount",
    "order_delivery_fee",
    "order_delivery_cost",
    "order_created_hour",
    "order_created_day",
    "order_created_month",
    "order_created_year",
    "store_plan_price",
    "delivery_distance_meters",
    "delivery_count",
    "total_payment_amount",
    "total_payment_fee",
    "payment_count"
]

numerical = df[numerical_features]

x = np.hstack([x_encode,numerical.values])
y = df["order_status"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

rm = RandomForestClassifier(n_estimators=100,random_state=42)

rm.fit(x_train,y_train)

y_pred = rm.predict(x_test)

print("accuracy score",accuracy_score(y_test,y_pred))
print("classification report",classification_report(y_test,y_pred))
print("confusion matrix",confusion_matrix(y_test,y_pred))

print("Model trained Successfully")

joblib.dump(rm,"Python/model.pkl")
joblib.dump(encode,"Python/encoder.pkl")

print("Model saved")
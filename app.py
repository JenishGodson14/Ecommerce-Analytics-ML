import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("Python/model.pkl")
encoder = joblib.load("Python/encoder.pkl")

st.set_page_config(
    page_title="E-Commerce Order Prediction",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 E-Commerce Order Status Prediction")
st.write("Predict whether an order will be Finished or Canceled.")

st.subheader("Order Information")

col1, col2, col3 = st.columns(3)

with col1:
    store_segment = st.selectbox(
        "Store Segment",
        ["FOOD", "GOOD"]
    )

    channel_name = st.selectbox(
        "Channel Name",
        [
            "OTHER PLACE",
            "PHONE PLACE",
            "WHATS PLACE",
            "FACE PLACE",
            "FOOD PLACE",
            "STORE PLACE",
            "BERLIN PLACE",
            "MADRID PLACE",
            "THINK PLACE",
            "LISBON PLACE",
            "SUPER PLACE",
            "ALL PLACE",
            "VELOCITY PLACE",
            "EATS PLACE",
            "SHOPP PLACE",
            "MUNICH PLACE",
            "LONDON PLACE",
            "ATCHIN PLACE",
            "FULL PLACE",
            "ON PLACE",
            "REGISTER PLACE",
            "GLUB PLACE",
            "SPEED PLACE",
            "SEARCH PLACE",
            "BEATLES PLACE",
            "SAN PLACE",
            "AHORA PLACE",
            "BRAZIL PLACE",
            "OWN PLACE",
            "LONGO PLACE",
            "WEAR PLACE",
            "RONALD PLACE",
            "PANCEPS PLACE",
            "OFF PLACE",
            "CAICAI PLACE",
            "READY PLACE",
            "CHOCO PLACE",
            "PORTO PLACE",
            "CENTER PLACE",
            "RIBA PLACE"
        ]
    )

    channel_type = st.selectbox(
        "Channel Type",
        ["OWN CHANNEL", "MARKETPLACE"]
    )

    driver_type = st.selectbox(
        "Driver Type",
        ["LOGISTIC OPERATOR", "FREELANCE"]
    )

    driver_modal = st.selectbox(
        "Driver Modal",
        ["MOTOBOY", "BIKER"]
    )

with col2:
    hub_city = st.selectbox(
        "Hub City",
        [
            "PORTO ALEGRE",
            "RIO DE JANEIRO",
            "SÃO PAULO",
            "CURITIBA"
        ]
    )

    hub_state = st.selectbox(
        "Hub State",
        ["RS", "RJ", "SP", "PR"]
    )

    order_amount = st.number_input(
        "Order Amount",
        min_value=0.0,
        value=100.0
    )

    order_delivery_fee = st.number_input(
        "Delivery Fee",
        min_value=0.0,
        value=0.0
    )

    order_delivery_cost = st.number_input(
        "Delivery Cost",
        min_value=0.0,
        value=0.0
    )

with col3:
    order_created_hour = st.number_input(
        "Created Hour",
        min_value=0,
        max_value=23,
        value=12
    )

    order_created_day = st.number_input(
        "Created Day",
        min_value=1,
        max_value=31,
        value=1
    )

    order_created_month = st.number_input(
        "Created Month",
        min_value=1,
        max_value=12,
        value=1
    )

    order_created_year = st.number_input(
        "Created Year",
        min_value=2000,
        max_value=2100,
        value=2026
    )

    store_plan_price = st.number_input(
        "Store Plan Price",
        min_value=0.0,
        value=0.0
    )

st.subheader("Delivery & Payment Information")

col1, col2, col3 = st.columns(3)

with col1:
    delivery_distance_meters = st.number_input(
        "Delivery Distance",
        min_value=0.0,
        value=1000.0
    )

    delivery_count = st.number_input(
        "Delivery Count",
        min_value=0,
        value=1
    )

with col2:
    total_payment_amount = st.number_input(
        "Total Payment Amount",
        min_value=0.0,
        value=100.0
    )

    total_payment_fee = st.number_input(
        "Total Payment Fee",
        min_value=0.0,
        value=0.0
    )

with col3:
    payment_count = st.number_input(
        "Payment Count",
        min_value=0,
        value=1
    )

if st.button("🔮 Predict Order Status"):

    categorical = pd.DataFrame([{
        "store_segment": store_segment,
        "channel_name": channel_name,
        "channel_type": channel_type,
        "driver_type": driver_type,
        "driver_modal": driver_modal,
        "hub_city": hub_city,
        "hub_state": hub_state
    }])

    numerical = np.array([[
        order_amount,
        order_delivery_fee,
        order_delivery_cost,
        order_created_hour,
        order_created_day,
        order_created_month,
        order_created_year,
        store_plan_price,
        delivery_distance_meters,
        delivery_count,
        total_payment_amount,
        total_payment_fee,
        payment_count
    ]])

    categorical_encoded = encoder.transform(categorical)

    final_input = np.hstack([
        categorical_encoded,
        numerical
    ])

    prediction = model.predict(final_input)[0]
    probability = model.predict_proba(final_input)[0]

    if prediction == 0:
        result = "Canceled"
    else:
        result = "Finished"

    st.subheader("Prediction")

    if result == "Finished":
        st.success(f"✅ Order Status: {result}")
    else:
        st.error(f"❌ Order Status: {result}")

    st.write(
        f"Canceled Probability: **{probability[0] * 100:.2f}%**"
    )

    st.write(
        f"Finished Probability: **{probability[1] * 100:.2f}%**"
    )
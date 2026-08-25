# E-Commerce Analytics & Machine Learning

## 📌 Project Overview

This project analyzes e-commerce order and delivery data to uncover business insights, monitor operational performance, and predict order outcomes using **Python, SQL, Power BI, and Machine Learning**.

The project follows an end-to-end data analytics workflow, starting from raw CSV datasets and progressing through data cleaning, SQL integration, exploratory data analysis, dashboard development, and machine learning.

## 🎯 Objectives

* Analyze e-commerce order and delivery performance
* Understand revenue and order trends
* Analyze completed and canceled orders
* Identify operational patterns
* Build an interactive Power BI dashboard
* Prepare features for machine learning
* Develop a classification model for order prediction
* Create a Streamlit application for model interaction

## 🛠️ Technologies Used

* **Python** – Data cleaning, validation, EDA, and machine learning
* **Pandas** – Data manipulation
* **Scikit-learn** – Machine learning and preprocessing
* **MySQL** – Data storage and SQL analysis
* **Power BI** – Interactive dashboard
* **Streamlit** – ML application
* **Git & GitHub** – Version control

## 📂 Project Structure

```text
Ecommerce-Analytics-ML/
│
├── PowerBI/
│   └── Dashboard.pbix
│
├── Python/
│   ├── data_cleaning.py
│   ├── data_loading.py
│   ├── data_validation.py
│   ├── EDA.py
│   ├── encoder.pkl
│   ├── model.pkl
│   └── mysql_connection.py
│
├── ScreenShot/
│   └── Dashboard Screenshot
│
├── app.py
├── ecommerce_sql.sql
├── ml_model.py
├── .gitignore
└── README.md
```

> The original raw and cleaned datasets are excluded from this repository because of their size.

## 🔄 Project Workflow

```text
Raw E-Commerce Data
        ↓
Data Cleaning
        ↓
Data Validation
        ↓
MySQL Database
        ↓
SQL Data Integration
        ↓
Exploratory Data Analysis
        ↓
Power BI Dashboard
        ↓
Feature Selection & Encoding
        ↓
Machine Learning
        ↓
Prediction Application
```

## 📊 Dataset

The project uses multiple e-commerce datasets covering areas such as:

* Orders
* Deliveries
* Drivers
* Hubs
* Stores
* Payments
* Channels

The datasets were cleaned and integrated before being used for analytics and machine learning.

Due to the dataset size, the data files are **not included in this GitHub repository**.

## 🧹 Data Cleaning & Validation

Python was used to prepare the datasets for analysis.

The workflow includes:

* Checking dataset dimensions
* Handling missing values
* Identifying data types
* Cleaning categorical variables
* Validating data consistency
* Preparing datasets for SQL integration

## 🗄️ SQL Analysis

MySQL was used to store and integrate the cleaned e-commerce datasets.

The SQL file included in the repository contains the queries used for:

* Joining datasets
* Creating analytical tables
* Preparing final order-level data
* Supporting Power BI analysis

SQL file:

```text
ecommerce_sql.sql
```

## 📈 Exploratory Data Analysis

Python-based EDA was performed to understand:

* Order status distribution
* Revenue
* Average Order Value
* Order trends
* Delivery performance
* Channel performance
* Store and hub characteristics

### Key Metrics

* **Total Revenue:** 38,800,730.73
* **Average Order Value:** 105.15
* **Finished Orders:** 352,020
* **Canceled Orders:** 16,979
* **Finished Order Rate:** 95.40%
* **Canceled Order Rate:** 4.60%

## 📊 Power BI Dashboard

An interactive Power BI dashboard was developed to visualize the major business and operational KPIs.

The dashboard focuses on areas such as:

* Revenue performance
* Order volume
* Order status
* Average order value
* Delivery performance
* Channel analysis
* Store and hub analysis
* Time-based trends

Power BI file:

```text
PowerBI/Dashboard.pbix
```

## 🤖 Machine Learning

A **Random Forest Classifier** was developed for order prediction.

The machine learning workflow includes:

1. Feature selection
2. Categorical feature preparation
3. Encoding categorical variables
4. Train-test split
5. Random Forest model training
6. Model evaluation
7. Model serialization

The trained model and encoder are stored as:

```text
Python/model.pkl
Python/encoder.pkl
```

## 📌 Selected Features

The machine learning model uses categorical operational features including:

* Store Segment
* Channel Name
* Channel Type
* Driver Type
* Driver Modal
* Hub City
* Hub State

## 📈 Model Performance

The Random Forest model achieved approximately:

**99.79% accuracy**

Model evaluation included:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

> Model performance should be interpreted together with the dataset characteristics and class distribution.

## 🖥️ Streamlit Application

A Streamlit application was developed to provide an interface for interacting with the machine learning model.

Run the application using:

```bash
streamlit run app.py
```

## 📸 Dashboard Preview

![E-Commerce Dashboard](ScreenShot/Screenshot%202026-08-21%20170503.png)

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/JenishGodson14/Ecommerce-Analytics-ML.git
```

### 2. Navigate to the project

```bash
cd Ecommerce-Analytics-ML
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

Install the Python packages required by the project.

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

## 💡 Key Skills Demonstrated

* Python
* Pandas
* Data Cleaning
* Data Validation
* Exploratory Data Analysis
* MySQL
* SQL Joins
* Power BI
* Data Visualization
* Feature Selection
* Categorical Encoding
* Random Forest Classification
* Machine Learning
* Streamlit
* Git & GitHub

## 👨‍💻 Author

**JenishGodson14**

GitHub: [JenishGodson14](https://github.com/JenishGodson14)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data
df = pd.read_csv("sales.csv", encoding='latin1')

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Title
st.title("📊 Superstore Sales Dashboard")

# ======================
# 🔹 SIDEBAR FILTERS
# ======================
st.sidebar.header("Filters")

region = st.sidebar.selectbox("Select Region", df['Region'].unique())
category = st.sidebar.selectbox("Select Category", df['Category'].unique())

filtered_df = df[(df['Region'] == region) & (df['Category'] == category)]

# ======================
# 🔹 KPI CARDS
# ======================
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")
col3.metric("Total Orders", filtered_df.shape[0])

# ======================
# 🔹 CHARTS
# ======================

# Layout: 2 columns
col_left, col_right = st.columns(2)

# 📊 Sales by Category
with col_left:
    st.subheader("Sales by Category")
    fig1, ax1 = plt.subplots()
    sns.barplot(x='Category', y='Sales', data=filtered_df, ax=ax1)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=30)
    st.pyplot(fig1)

# 📊 Profit by Region
with col_right:
    st.subheader("Profit by Region")
    fig2, ax2 = plt.subplots()
    sns.barplot(x='Region', y='Profit', data=filtered_df, ax=ax2)
    st.pyplot(fig2)

# 📈 Sales Trend
st.subheader("Sales Trend Over Time")

sales_trend = filtered_df.groupby('Order Date')['Sales'].sum()

fig3, ax3 = plt.subplots()
sales_trend.plot(ax=ax3)
st.pyplot(fig3)

# ======================
# 🔹 TOP PRODUCTS
# ======================
st.subheader("Top 10 Sub-Categories by Sales")

top_products = (
    filtered_df.groupby('Sub-Category')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)

# ======================
# 🔹 DATA PREVIEW
# ======================
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head(20))
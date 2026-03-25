import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
df = pd.read_csv("sales.csv", encoding='latin1')

st.title("📊 Superstore Sales Dashboard")

# KPIs
st.subheader("Key Metrics")
st.write("Total Sales:", round(df['Sales'].sum(), 2))
st.write("Total Profit:", round(df['Profit'].sum(), 2))

# Sales by Category
st.subheader("Sales by Category")
fig1, ax1 = plt.subplots()
sns.barplot(x='Category', y='Sales', data=df, ax=ax1)
st.pyplot(fig1)

# Profit by Region
st.subheader("Profit by Region")
fig2, ax2 = plt.subplots()
sns.barplot(x='Region', y='Profit', data=df, ax=ax2)
st.pyplot(fig2)

# Sales Trend
st.subheader("Sales Trend Over Time")
df['Order Date'] = pd.to_datetime(df['Order Date'])
sales_trend = df.groupby('Order Date')['Sales'].sum()

fig3, ax3 = plt.subplots()
sales_trend.plot(ax=ax3)
st.pyplot(fig3)

# Filter
st.subheader("Filter by Category")
category = st.selectbox("Select Category", df['Category'].unique())
filtered_df = df[df['Category'] == category]

st.write(filtered_df.head())
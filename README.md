# 📊 Superstore Sales Data Analysis Dashboard

## 🔍 Overview
This project analyzes the **Superstore Sales dataset** to extract meaningful business insights using Python and an interactive dashboard built with Streamlit.

The dashboard helps visualize sales performance, profit trends, and key metrics across different regions and product categories.

---

## 🚀 Features
- 📊 **KPI Metrics**
  - Total Sales
  - Total Profit
  - Total Orders

- 📈 **Visualizations**
  - Sales by Category
  - Profit by Region
  - Sales Trend Over Time
  - Top 10 Sub-Categories by Sales

- 🎛️ **Interactive Filters**
  - Region selection
  - Category selection

- 📋 **Data Preview**
  - View filtered dataset directly

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Streamlit  

---

## 📂 Project Structure
sales-dashboard/
│── app.py
│── sales.csv
│── dashboard.png
│── README.md


---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/som203112/sales-dashboard.git
cd sales-dashboard

### Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

### Install dependencies
pip install pandas matplotlib seaborn streamlit

### Run the dashboard
streamlit run app.py
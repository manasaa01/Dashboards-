import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Sales Dashboard")

# Load sample data
@st.cache_data
def load_data():
    df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [12000, 15000, 13000, 17000, 16000, 19000],
        'Region': ['North', 'South', 'East', 'West', 'North', 'South']
    })
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
region_filter = st.sidebar.multiselect(
    "Select Region:",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

# Filter data
df_filtered = df[df['Region'].isin(region_filter)]

# Display metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df_filtered['Sales'].sum():,}")
col2.metric("Average Sales", f"${df_filtered['Sales'].mean():,.0f}")
col3.metric("Max Sales", f"${df_filtered['Sales'].max():,}")

# Charts
st.subheader("📈 Sales by Month")
fig = px.bar(df_filtered, x='Month', y='Sales', color='Region', text='Sales')
st.plotly_chart(fig, use_container_width=True)

st.subheader("🌍 Sales by Region")
fig2 = px.pie(df_filtered, names='Region', values='Sales')
st.plotly_chart(fig2, use_container_width=True)

# Show data table
st.subheader("📋 Raw Data")
st.dataframe(df_filtered)

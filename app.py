import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Nifty_Stocks.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# App title
st.title("📈 Nifty Stocks Visualization")

# Sidebar for category & symbol selection
st.sidebar.header("Filter Options")

# Select Category
categories = df["Category"].unique()
selected_category = st.sidebar.selectbox("Select Category", categories)

# Filter by category
filtered_df = df[df["Category"] == selected_category]

# Select Symbol
symbols = filtered_df["Symbol"].unique()
selected_symbol = st.sidebar.selectbox("Select Symbol", symbols)

# Final filtered data
final_df = filtered_df[filtered_df["Symbol"] == selected_symbol]

# Show dataset preview
st.subheader(f"Data for {selected_symbol} in {selected_category}")
st.dataframe(final_df)

# Plot Close Price trend
st.subheader(f"Close Price Trend - {selected_symbol}")

fig, ax = plt.subplots(figsize=(15, 8))
sb.lineplot(data=final_df, x="Date", y="Close", ax=ax)
ax.set_title(f"{selected_symbol} Close Price Over Time")
st.pyplot(fig)

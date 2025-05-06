# filepath: stock-market-simulator/src/stock_stimulator.py

import streamlit as st          
import pandas as pd             
import matplotlib.pyplot as plt 
import random                   

st.title("📈 Simple Stock Market Simulator")

st.write("""
This is a very basic stock market simulator for beginners.  
We use fake data and a simple rule:  
👉 Buy if price goes up from yesterday, Sell if it goes down.
""")

def generate_fake_stock_data(days=30):
    prices = [100]  # Start with price 100
    for _ in range(days - 1):
        change = random.choice([-1, 1]) * random.randint(1, 5)
        prices.append(prices[-1] + change)
    return prices

days = st.slider("Select number of days to simulate", 10, 60, 30)
prices = generate_fake_stock_data(days)

df = pd.DataFrame({'Day': range(1, days + 1), 'Price': prices})

df['Action'] = ['Hold'] + [''] * (len(df) - 1)
for i in range(1, len(df)):
    if df['Price'][i] > df['Price'][i - 1]:
        df.at[i, 'Action'] = 'Buy'
    else:
        df.at[i, 'Action'] = 'Sell'

st.subheader("📊 Stock Prices and Trading Actions")
st.dataframe(df)

st.subheader("📉 Stock Price Chart")

fig, ax = plt.subplots()
ax.plot(df['Day'], df['Price'], marker='o', label='Price')

for i in range(1, len(df)):
    if df['Action'][i] == 'Buy':
        ax.plot(df['Day'][i], df['Price'][i], 'g^', label='Buy' if i == 1 else "")
    elif df['Action'][i] == 'Sell':
        ax.plot(df['Day'][i], df['Price'][i], 'rv', label='Sell' if i == 1 else "")

ax.set_xlabel("Day")
ax.set_ylabel("Price")
ax.legend()
st.pyplot(fig)

st.success("Simulation complete! Try changing the number of days above.")
import yfinance as yf 
ticker = yf.Ticker("OTLK")
data = ticker.history(period="5y")
print(data.head())
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot(data.index, data['Close'])
plt.title("OTLK 5-Year stock price ")
plt.xlabel("Date")
plt.ylabel("price ($)")
plt.show()
         

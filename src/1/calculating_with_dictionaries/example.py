# example.py
#
# Example of calculating with dictionaries
import os

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Find min and max price
zip_price = zip(prices.values(), prices.keys())
print("prices: ")
print( prices )
print(i for i in zip_price)

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min price:', min_price)
print('max price:', max_price)

print('sorted prices:')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)

# plt.plot([1,2,3,4])
# plt.ylabel('numbers')
# plt.show()

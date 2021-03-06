import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure(figsize=(8,5))

gas = pd.read_csv('gas_prices.csv')

plt.title('Gas Prices over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize': 22})

plt.plot(gas.Year, gas.USA, 'b.-', label='United States')
plt.plot(gas.Year, gas.Canada, 'r.-',  label='Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-',  label='South Korea')

print(gas.Year[::3])

plt.xticks(gas.Year[::3])

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend()

plt.show()


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')
country_name = input("Введіть назву країни (Ukraine або Poland): ")
country_data = df[df['Country Name'] == country_name]


plt.figure(figsize=(10, 5))
plt.plot(country_data['Year'], country_data['Indicator Value'], marker='o', label=country_name)
plt.xlabel('Рік')
plt.ylabel('Значення показника')
plt.title(f'Динаміка показника для {country_name}')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(country_data['Year'][:18], country_data['Indicator Value'][:18], color='skyblue', label=country_name)
plt.xlabel('Рік')
plt.ylabel('Значення показника')
plt.title(f'Значення показника для {country_name} до 2020 року')
plt.legend()
plt.grid(axis='y')
plt.show()
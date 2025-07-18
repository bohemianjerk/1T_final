import pandas as pd
import matplotlib.pyplot as plt


# Используется очищенный файл
data = pd.read_csv(r'C:\Users\funny\Downloads\pure_data8.csv')

df = pd.DataFrame(data)

# Создадим график
plt.figure(figsize=(10, 6))

# Используем scatter для отображения зависимости на графике
sc = plt.scatter(df['trip_distance'], df['passenger_count'], c=df['tip_amount'], cmap='coolwarm', s=30, alpha=0.7)

plt.xlabel('trip_distance')
plt.ylabel('passenger_count')
plt.title('Зависимость tip_amount от trip_distance и passenger_count')
plt.colorbar(label='tip_amount')

# Добавим сетку
plt.grid(True)

# Сохраним график в формате PNG
plt.savefig('graph.png')

plt.show()
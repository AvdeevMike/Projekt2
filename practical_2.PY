
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из файла
yug = pd.read_csv('https://drive.google.com/file/d/17V2N7ZsF12InPI6j8oKwHMKX7pt7L2mX/view?usp=sharing', sep=",")

# Создание dataframe
df = pd.DataFrame(yug)

# Вывод первой строки
print(df.iloc[0])

# Вывод всех строк
print(df)

#Вывод общих данных
print(yug.info())
print(yug.describe())

# Построение диаграммы для указанных строк и колонок
rows = [2, 3, 4, 5, 6, 8]
columns = ['D', 'E', 'F', 'G', 'H']

for row in rows:
    fig, ax = plt.subplots()
    ax.bar(columns, df.loc[row, columns])
    ax.set_title(f'Диаграмма для строки {row}')
    plt.show()
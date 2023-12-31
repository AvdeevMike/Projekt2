
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# �������� ������ �� �����
yug = pd.read_csv('https://drive.google.com/file/d/17V2N7ZsF12InPI6j8oKwHMKX7pt7L2mX/view?usp=sharing', sep=",")

# �������� dataframe
df = pd.DataFrame(yug)

# ����� ������ ������
print(df.iloc[0])

# ����� ���� �����
print(df)

#����� ����� ������
print(yug.info())
print(yug.describe())

# ���������� ��������� ��� ��������� ����� � �������
rows = [2, 3, 4, 5, 6, 8]
columns = ['D', 'E', 'F', 'G', 'H']

for row in rows:
    fig, ax = plt.subplots()
    ax.bar(columns, df.loc[row, columns])
    ax.set_title(f'��������� ��� ������ {row}')
    plt.show()
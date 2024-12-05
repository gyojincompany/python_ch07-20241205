import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 한글 깨짐 방지 - 한글용 폰트 추가
plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

flights = sns.load_dataset("flights")
# flights.to_csv("data/flights.csv", index=False)
print(flights)

flights_df = flights.pivot(index="month", columns="year", values="passengers")
print(flights_df)

sns.heatmap(flights_df, cmap="RdYlGn_r", annot=True)
plt.show()
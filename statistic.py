import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_excel('movie_data.xlsx')

plt.scatter(df["Rate"], df["Box Office"], alpha=1)

plt.xlim(7, 8.5)
plt.ylim(0, 25000000)

lr = LinearRegression()
lr.fit(df["Rate"].values.reshape(-1, 1), df["Box Office"].values.reshape(-1, 1))

plt.plot(df["Rate"], lr.intercept_[0] + lr.coef_[0][0] * df["Rate"], color='red')

predicted_values = lr.predict(df["Rate"].values.reshape(-1, 1))
distances = np.abs(predicted_values - df["Box Office"].values.reshape(-1, 1))

distance_list = distances.flatten().tolist()

rateList = []

for i in range(len(distance_list)):
    num = distance_list[i] / predicted_values[i]
    rateList.append(num)

sum = 0
for i in rateList:
    sum += i

print(sum)

plt.show()








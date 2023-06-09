import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import chi2_contingency


from google.colab import drive
drive.mount('/content/drive/')

file_path = '/content/drive/MyDrive/movie_data.xlsx'
df = pd.read_excel(file_path)

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

df['RateCategory'] = pd.cut(df['Rate'], bins=[0, 7, 8.5, float('inf')], labels=['Low', 'Medium', 'High'])

contingency_table = pd.crosstab(df['RateCategory'], df['Box Office'])

chi2, p_value, _, _ = chi2_contingency(contingency_table)

mse = mean_squared_error(df["Box Office"], predicted_values)
r2 = r2_score(df["Box Office"], predicted_values)

n = len(df["Rate"])  
p = 1  
adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

for i in range(len(distance_list)):
    plt.plot([df["Rate"].values[i], df["Rate"].values[i]], [df["Box Office"].values[i], predicted_values[i]], color='gray', linestyle='--', alpha=0.5)
    plt.text(df["Rate"].values[i], (df["Box Office"].values[i] + predicted_values[i]) / 2, f"{distance_list[i] / 100000:.2f}", color='black', ha='center', va='center', fontsize=6)

plt.title("Movie Rating vs. Box Office")
plt.xlabel("Rating")
plt.ylabel("Box Office")

print("Chi-squared value:", chi2)
print("p-value:", p_value)

print("Mean Squared Error:", mse)
print("R-squared:", r2)
print("Adjusted R-squared:", adjusted_r2)

print(sum)

plt.show()
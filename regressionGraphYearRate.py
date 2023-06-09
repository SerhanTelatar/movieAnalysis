import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

from google.colab import drive
drive.mount('/content/drive/')

file_path = '/content/drive/MyDrive/movie_data.xlsx'
df = pd.read_excel(file_path)

df["Year"] = df["Year"].astype(int)  # Convert "Year" column to integer values

plt.figure(figsize=(14, 8))

plt.scatter(df["Year"], df["Box Office"], alpha=1)

plt.xlim(2000, 2020)
plt.ylim(0, 25000000)

lr = LinearRegression()
lr.fit(df["Year"].values.reshape(-1, 1), df["Box Office"].values.reshape(-1, 1))

plt.plot(df["Year"], lr.intercept_[0] + lr.coef_[0][0] * df["Year"], color='red')

predicted_values = lr.predict(df["Year"].values.reshape(-1, 1))
distances = np.abs(predicted_values - df["Box Office"].values.reshape(-1, 1))

mse = mean_squared_error(df["Box Office"], predicted_values)
r2 = r2_score(df["Box Office"], predicted_values)

# Calculate adjusted R-squared
n = len(df["Year"])  # Number of data points
p = 1  # Number of predictors (in this case, it's 1, which is the "Year" feature)
adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

for i in range(len(distances)):
    plt.plot([df["Year"].values[i], df["Year"].values[i]], [df["Box Office"].values[i], predicted_values[i]], color='gray', linestyle='--', alpha=0.5)
    plt.text(df["Year"].values[i], (df["Box Office"].values[i] + predicted_values[i]) / 2, f"{distance_list[i] / 100000:.2f}", color='black', ha='center', va='center', fontsize=8)

plt.xticks(df["Year"])  # Set x-axis tick labels as the integer values of "Year"

print("Mean Squared Error:", mse)
print("R-squared:", r2)
print("Adjusted R-squared:", adjusted_r2)

plt.title("Movie Rating vs. Year")
plt.xlabel("Rating")
plt.ylabel("Year")

plt.show()
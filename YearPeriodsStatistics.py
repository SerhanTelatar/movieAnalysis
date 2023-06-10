import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

from google.colab import drive
drive.mount('/content/drive/')

file_path = '/content/drive/MyDrive/movie_data.xlsx'
df = pd.read_excel(file_path)

df["Year"] = df["Year"].astype(int) 


lr = LinearRegression()
lr.fit(df["Year"].values.reshape(-1, 1), df["Box Office"].values.reshape(-1, 1))

predicted_values = lr.predict(df["Year"].values.reshape(-1, 1))
distances = np.abs(predicted_values - df["Box Office"].values.reshape(-1, 1))

mse = mean_squared_error(df["Box Office"], predicted_values)
r2 = r2_score(df["Box Office"], predicted_values)


n = len(df["Year"])  
p = 1  
adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)


grouped_stats = []
for start_year in range(2000, 2024, 5):
    end_year = start_year + 4
    period_df = df[(df["Year"] >= start_year) & (df["Year"] <= end_year)]

    if len(period_df) == 0:
        continue

    mse_period = mean_squared_error(period_df["Box Office"], lr.predict(period_df["Year"].values.reshape(-1, 1)))
    r2_period = r2_score(period_df["Box Office"], lr.predict(period_df["Year"].values.reshape(-1, 1)))


    n_period = len(period_df["Year"])  
    p_period = 1  
    adjusted_r2_period = 1 - (1 - r2_period) * (n_period - 1) / (n_period - p_period - 1)

    grouped_stats.append({
        "Start Year": start_year,
        "End Year": end_year,
        "Number of Movies": len(period_df),
        "MSE": mse_period,
        "R2": r2_period,
        "Adjusted R2": adjusted_r2_period
    })

grouped_stats_df = pd.DataFrame(grouped_stats)

print("Overall Statistics:")
print("MSE:", mse)
print("R-squared:", r2)
print("Adjusted R-squared:", adjusted_r2)
print("\nStatistics by 5-Year Periods:")
print(grouped_stats_df)

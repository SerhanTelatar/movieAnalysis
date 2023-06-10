import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive/')

file_path = '/content/drive/MyDrive/movie_data.xlsx'
df = pd.read_excel(file_path)


group1 = df[df["Year"] <= 2010]["Box Office"]
group2 = df[df["Year"] > 2010]["Box Office"]


t_statistic, p_value = stats.ttest_ind(group1, group2)


plt.figure(figsize=(8, 6))  


sns.histplot(group1, kde=True, label="<= 2010")


sns.histplot(group2, kde=True, label="> 2010")

plt.legend()


plt.title("Box Office Distribution Comparison between Groups")
plt.xlabel("Box Office")
plt.ylabel("Density")


plt.show()

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)
if p_value < 0.05:
    print("The difference in mean box office values between the two groups is statistically significant.")
else:
    print("The difference in mean box office values between the two groups is not statistically significant.")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from google.colab import drive
drive.mount('/content/drive/')

file_path = '/content/drive/MyDrive/movie_data.xlsx'
df = pd.read_excel(file_path)


group1 = df[df["Year"] <= 2010]["Box Office"]
group2 = df[df["Year"] > 2010]["Box Office"]


t_statistic, p_value = stats.ttest_ind(group1, group2)


plt.figure(figsize=(8, 6)) 


plt.boxplot([group1, group2], labels=["<= 2010", "> 2010"])


plt.title("Box Office Comparison between Groups")
plt.xlabel("Year")
plt.ylabel("Box Office")


if p_value < 0.05:
    plt.text(1.5, plt.ylim()[1] * 0.9, "Significant", ha='center', va='center', color='red')
else:
    plt.text(1.5, plt.ylim()[1] * 0.9, "Not Significant", ha='center', va='center', color='black')


plt.show()

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)
if p_value < 0.05:
    print("The difference in mean box office values between the two groups is statistically significant.")
else:
    print("The difference in mean box office values between the two groups is not statistically significant.")

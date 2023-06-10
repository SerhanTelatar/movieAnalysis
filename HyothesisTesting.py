import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import pandas as pd

from google.colab import drive
drive.mount('/content/drive/')

file_path = '/content/drive/MyDrive/movie_data.xlsx'
df = pd.read_excel(file_path)

df['RateCategory'] = pd.cut(df['Rate'], bins=[0, 7, 8.5, float('inf')], labels=['Low', 'Medium', 'High'])

contingency_table = pd.crosstab(df["RateCategory"], df["Box Office"])


dof = (contingency_table.shape[0] - 1) * (contingency_table.shape[1] - 1)


x = np.linspace(0, 80)


pdf = chi2.pdf(x, dof)


significance_level = 0.05
critical_value = chi2.ppf(1 - significance_level, dof)


plt.plot(x, pdf)


plt.fill_between(x, pdf, where=(x >= critical_value), interpolate=True, color='red', alpha=0.3)



plt.xlabel("Chi-Square Value")
plt.ylabel("Probability Density")
plt.title("Chi-Square Distribution with Critical Region")


plt.text(critical_value, 0.02, f"Critical Value: {critical_value:.2f}", ha='center', va='bottom', color='red')



plt.legend(["Chi-Square Distribution", "Critical Region"], loc="upper right")


chi2, p_value, dof, expected = chi2_contingency(contingency_table)
calculated_chi_square = chi2


if calculated_chi_square > critical_value:
    result = "Reject the null hypothesis"
else:
    result = "Fail to reject the null hypothesis"


if result == "Reject the null hypothesis":
    interpretation = "The graph shows that the observed association between the box office values and ratings is statistically significant. There is evidence of a relationship or dependence between the variables, indicating that they are not independent."
else:
    interpretation = "The graph does not provide sufficient evidence to reject the null hypothesis. The observed association between the box office values and ratings can be reasonably explained by chance alone, suggesting that the variables are independent."


print("Calculated Chi-Square Value:", calculated_chi_square)
print("Test Result:", result)
print("Interpretation:", interpretation)

plt.show()

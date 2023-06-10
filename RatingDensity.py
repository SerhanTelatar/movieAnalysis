import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive/')

file_path = '/content/drive/MyDrive/movie_data.xlsx'
df = pd.read_excel(file_path)


plt.figure(figsize=(8, 6))  


sns.histplot(df["Rate"], kde=True)


plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Density")

plt.show()

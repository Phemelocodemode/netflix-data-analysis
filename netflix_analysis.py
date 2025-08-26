
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_cleaned.csv")

# Top 10 countries with most content
df['country'].value_counts().head(10).plot(kind='bar', title="Top 10 Countries with Most Netflix Content")
plt.show()

# Titles released per year
df['release_year'].value_counts().sort_index().plot(kind='line', title="Netflix Titles by Release Year")
plt.show()

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
# Assuming you have a dataset named 'data.csv' containing information about algorithmic bias
data = pd.read_csv('data.csv')

# Display the first few rows of the dataset
data.head()

# Summary statistics
summary_stats = data.describe()
print(summary_stats)

# Data visualization
# Example: Bar plot of bias distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='bias_category', data=data)
plt.title('Distribution of Bias Categories')
plt.xlabel('Bias Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Example: Box plot of bias scores by demographic group
plt.figure(figsize=(10, 6))
sns.boxplot(x='demographic_group', y='bias_score', data=data)
plt.title('Bias Scores by Demographic Group')
plt.xlabel('Demographic Group')
plt.ylabel('Bias Score')
plt.xticks(rotation=45)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {'State': ['Maharashtra', 'Uttar Pradesh', 'Bihar', 'West Bengal', 'Tamil Nadu', 'Rajasthan', 'Gujarat', 'Karnataka', 'Uttaral-khand', 'Andhra Pradesh'],
        'population': [121442423, 237882715, 124799959, 91348748, 72147030, 76154056, 60439692, 67559418, 10086292, 53073056],
        'literacy_rate': [82.9, 73.8, 63.8, 77.1, 80.3, 66.1, 79.2, 74.4, 66.6, 68.3],
        'rural_population_percent': [54.8, 77.7, 86.7, 62.1, 36.7, 71.3, 45.9, 59.1, 69.6, 69.9]}

demographics_df = pd.DataFrame(data)
print(demographics_df.info())
print(demographics_df.describe())
total_population = demographics_df['population'].sum()
print("Total Population of the Listed States:", total_population)
average_literacy_rate = demographics_df['literacy_rate'].mean()
print("Average Literacy Rate:", average_literacy_rate)
correlation = demographics_df['literacy_rate'].corr(demographics_df['rural_population_percent'])
print("Correlation between Literacy Rate and Rural Population Percentage:", correlation)
plt.figure( figsize=(10, 6))
sns.barplot(x='State', y='population', data=demographics_df)
plt.title('Population Distribution by State')
plt.xticks(rotation=45)
plt.ylabel('Population')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='rural_population_percent', y='literacy_rate', data=demographics_df)
plt.title('Literacy Rate vs. Rural Population Percentage')
plt.xlabel('Rural Population Percentage')
plt.ylabel('Literacy Rate')
plt.show()
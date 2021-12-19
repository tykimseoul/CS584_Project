import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('./data/interest_data.csv')
df['ratio'] = df['실제관심'] / df['관심종목수']
fig = plt.figure(figsize=(10, 7))

sns.boxplot(y='만족도', x='관심종목수', data=df, orient='h') \
    .set(xlabel='Number of Favorites', ylabel='Satisfaction Score', title='Number of Favorites vs Satisfaction Score')

plt.show()

# show plot
fig = plt.figure(figsize=(10, 7))
sns.boxplot(y='만족도', x='실제관심', data=df, orient='h') \
    .set(xlabel='Number of Traded', ylabel='Satisfaction Score', title='Number of Actually Traded vs Satisfaction Score')
plt.show()

fig = plt.figure(figsize=(10, 7))
sns.boxplot(y='만족도', x='ratio', data=df, orient='h') \
    .set(xlabel='Traded to Favorites Ratio', ylabel='Satisfaction Score', title='Traded to Favorites Ratio vs Satisfaction Score')
plt.show()

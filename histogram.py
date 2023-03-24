import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/likert_data2.csv')

ax = sns.catplot(x='Score', hue='Method', data=df, kind="count").set(xlabel='Scores', ylabel='Frequency', title='Frequency of Satisfaction Scores of Each Method')
ax._legend.remove()
plt.legend(bbox_to_anchor=(1.01, 0.6), borderaxespad=0, title='Method')
plt.tight_layout()
plt.savefig('histogram.png', dpi=200)
plt.show()

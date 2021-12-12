# Wilcoxon signed-rank test
from scipy.stats import wilcoxon
import pandas as pd

df = pd.read_csv('./data/likert_data.csv', index_col=0)

# compare samples
stat, p = wilcoxon(df['A'], df['B'])
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Same distribution (fail to reject H0)')
else:
	print('Different distribution (reject H0)')

stat, p = wilcoxon(df['B'], df['C'])
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Same distribution (fail to reject H0)')
else:
	print('Different distribution (reject H0)')
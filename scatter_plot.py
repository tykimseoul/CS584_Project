import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 2000)

favorites_path = './data/favorites'
favorite_files = sorted([f for f in os.listdir(favorites_path) if os.path.isfile(os.path.join(favorites_path, f))])

favorites_dfs = []
for favorite_file in favorite_files:
    if favorite_file == '.DS_Store':
        continue
    print(favorite_file)
    z = re.match(r'favorites_(\d+).csv', favorite_file)
    user_id = z.groups()[0]

    df = pd.read_csv(f'{favorites_path}/{favorite_file}', index_col=0)
    df = df[['scode']]
    df.reset_index(drop=True, inplace=True)
    df['user_id'] = str(user_id)
    df['true_rank'] = df.index
    print(df.head())
    favorites_dfs.append(df)

favorites_df = pd.concat(favorites_dfs)

rankings_path = './data/rankings'
ranking_files = sorted([f for f in os.listdir(rankings_path) if os.path.isfile(os.path.join(rankings_path, f))])

rankings_dfs = []
for ranking_file in ranking_files:
    print(ranking_file)
    if ranking_file == '.DS_Store':
        continue
    z = re.match(r'X_(\w)_(\d+)_step(\d+).csv', ranking_file)
    experiment_type, user_id, experiment_seq = z.groups()[0], int(z.groups()[1]), int(z.groups()[2])

    if experiment_type != 'B' or experiment_seq != 5:
        continue

    df = pd.read_csv(f'{rankings_path}/{ranking_file}', index_col=0)
    df = df[['scode']]

    df['user_id'] = str(user_id)
    df['pred_rank'] = df.index
    print(df.head())
    rankings_dfs.append(df)

rankings_df = pd.concat(rankings_dfs)

full_df = favorites_df.merge(rankings_df, on=['scode', 'user_id'])
print(full_df)

plt.figure()
sns.scatterplot(data=full_df, x='true_rank', y='pred_rank', hue='user_id', alpha=0.5) \
    .set(xlabel='True Rank', ylabel='Predicted Rank', title='True vs Predicted Rank')
# sns.regplot(data=full_df, x='true_rank', y='pred_rank', scatter=False)
plt.plot([0, 30], [0, 30], linewidth=2, alpha=0.5)

# plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5), ncol=1)
plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0, title='User')
plt.tight_layout()

plt.savefig('scatter_color.png', dpi=200)
plt.show()

plt.figure()
sns.scatterplot(data=full_df, x='true_rank', y='pred_rank', alpha=0.5) \
    .set(xlabel='True Rank', ylabel='Predicted Rank', title='True vs Predicted Rank')
# sns.regplot(data=full_df, x='true_rank', y='pred_rank', scatter=False)
plt.plot([0, 30], [0, 30], linewidth=2, alpha=0.5)

plt.tight_layout()

plt.savefig('scatter.png', dpi=200)
plt.show()

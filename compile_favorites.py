import os
import re

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 2000)

favorites_path = './data/favorites'
favorites_files = sorted([f for f in os.listdir(favorites_path) if os.path.isfile(os.path.join(favorites_path, f))])

favorites_dfs = []
for favorites_file in favorites_files:
    print(favorites_file)
    if favorites_file == '.DS_Store':
        continue
    z = re.match(r'favorites_(\d).csv', favorites_file)
    user_id = z.groups()[0]

    df = pd.read_csv(f'{favorites_path}/{favorites_file}', index_col=0)
    df['user_id'] = user_id
    print(df.head())
    favorites_dfs.append(df)

favorites_df = pd.concat(favorites_dfs)

favorites_df.reset_index(drop=True, inplace=True)

print(favorites_df.head())
favorites_df.to_csv('./data/favorites_data.csv')

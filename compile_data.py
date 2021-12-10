import os
import re
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 2000)

rankings_path = './data/rankings'
ranking_files = sorted([f for f in os.listdir(rankings_path) if os.path.isfile(os.path.join(rankings_path, f))])

experiment_type_map = {'A': 'Base', 'B': 'Ranked Full Features', 'C': 'Ranked Partial Features'}

ranking_dfs = []
for ranking_file in ranking_files:
    print(ranking_file)
    z = re.match(r'X_(\w)_(\d)_step(\d).csv', ranking_file)
    experiment_type, user_id, experiment_seq = z.groups()[0], int(z.groups()[1]), int(z.groups()[2])

    if experiment_type == 'A':
        if experiment_seq == 5:
            continue
        experiment_seq += 1

    df = pd.read_csv(f'{rankings_path}/{ranking_file}', index_col=0)
    df.drop(['pricedollar', 'changepctparenthesis', 'color'], axis=1, inplace=True)
    df['exp_type'] = experiment_type_map[experiment_type]
    df['user_id'] = user_id
    df['exp_seq'] = experiment_seq
    print(df.head())
    ranking_dfs.append(df)

ranking_df = pd.concat(ranking_dfs)

ranking_df['price'] = ranking_df['price'].str.replace(',', '').astype(float)
ranking_df['change'] = ranking_df['change'].astype(float)
ranking_df['volume'] = ranking_df['volume'].str.replace(',', '').astype(int)
ranking_df['changepct'] = ranking_df['changepct'].str.replace('%', '').astype(float)
ranking_df['color'] = ranking_df['change'].apply(lambda r: '#E24A4A' if r > 0 else '#3485FF')

ranking_df.reset_index(drop=True, inplace=True)

print(ranking_df.head())
ranking_df.to_csv('./data/ranking_data.csv')

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# print(df.head(16))

# print(df.columns)

# print(df[['Name', 'Type 1', 'HP']][0:4])

# print(df.iloc[300:304])

# for index, row in df.iterrows():
#    print(index, row)

#print(df.loc[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Ghost')])

# df.sort_values(by=['Type', 'HP'], ascending=[1, 0)

# df = df.drop(columns=['Total'])

#df['Total'] = df.iloc[:, 4:9].sum(axis=1)

#poisontypes = df.loc[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Poison') & (df['HP'] >70)]
#print(poisontypes.iloc[:800])

#cols = list(df.columns)
#df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
#df.head(15)

#df.to_csv('new_df.csv', index = False)

#new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] >70)]
#new_df = new_df.reset_index(drop = True)
#print(new_df)

#no_megas = df.loc[~df['Name'].str.contains('Mega')]
#print(no_megas)
#no_megas.to_csv('no_megas.csv')

import re

#df.loc[df['Type 1'].str.contains("Fire|Grass", flags = re.I, regex = True)]

nameFilt = df.loc[df['Name'].str.contains("^pi[a-z]*", flags = re.I, regex = True)]
print(nameFilt)




import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# print(df.head(16))

# print(df.columns)

# print(df[['Name', 'Type 1', 'HP']][0:4])

# print(df.iloc[300:304])

# for index, row in df.iterrows():
#    print(index, row)

# print(df.loc[(df['Type 1'] == 'Fire') | (df['Type 2'] == 'Fire')])

# df.sort_values(by=['Type', 'HP'], ascending=[1, 0)

# df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:9].sum(axis=1)

print(df.head(5))




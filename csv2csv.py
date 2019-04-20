import pandas as pd

df1 = pd.read_csv('/home/sinisterrapist/Desktop/train.csv')
df = df1[['CRITICAL FLAG', 'CAMIS']]
print(df)
df.to_csv('output.csv', sep=',')


import pandas as pd


df = pd.DataFrame(index=['A','B','C','D'], columns=['x','y','z'])
df['x'] = [1,2,3,4] # column grab and assign
df.loc['A'] = [1,2,3] # index grab and assign



print(df)

"""
vertically (row-wise)
horizontally (column wise)
pd.concate([df1, df2], axis=0, ignore_index=True)
"""
import pandas as pd

df_Region1 = pd.DataFrame({
    'CustomerID':[1,2],
    'Name': ['Gopal', 'Raju']
})
#region2
df_Region2 = pd.DataFrame({
    'CustomerID':[3,4],
    'Name': ['Shyam', 'Baburao']
})

df_concate = pd.concat([df_Region1, df_Region2],axis=0,ignore_index=True)
print(df_concate)

df_concate = pd.concat([df_Region1, df_Region2],axis=1,ignore_index=True)
print(df_concate)
import pandas as pd
#customer dataframe 
df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name': ['Ramesh', 'Suresh', 'Kalpesh']
})
#order dataframe
df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount': [250,450,350]
})

# df.merge(df1,df2, on= "Column_Name", how="type of join")
df_merge = pd.merge(df_customers,df_orders, on="CustomerID", how="inner") #Only Match Data Show
print(df_merge)

df_merge = pd.merge(df_customers,df_orders, on="CustomerID", how="outer") #not match Data fill with Nan
print(df_merge)

df_merge = pd.merge(df_customers,df_orders, on="CustomerID", how="left") 
print(df_merge)

df_merge = pd.merge(df_customers,df_orders, on="CustomerID", how="right")
print(df_merge)
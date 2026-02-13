# import pandas as pd
# data = {
#     "Name": ['Ram',None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
#     "Age" : [28,34,22,30,29,40,25,32],
#     "Salary": [50000, 60000,None,52000, 49000, None,48000, 58000],
#     "Performance Score": [85,90,78,92,None,95,80,89]
# }
# df = pd.DataFrame(data)
# # print(df)

# # df.dropna(axis=0, inplace=True)
# # df.dropna(axis=0,inplace=True)#Removing Rows Null vaues
# print(df)

# # df,fillna(value, inplace=True)
# print(f"After Fill Nan")
# df.fillna({
#     'Name':"Unknown",
#     "Salary": 0,
#     "Performance Score":0
# }, inplace=True)

# print(df)


import pandas as pd
data = {
    "Name": ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age" : [28,None, 22, 30, 29, 40,25,32],
    "Salary": [50000, None, 45000,52000, 49000, 70000,48000, 58000],
    "Performance_Score": [85, None, 78,92,88,95,80,89]
}
df = pd.DataFrame(data)
print(df)

numeric_columns = df.select_dtypes(include="number")
df[numeric_columns.columns] = numeric_columns.fillna(0, inplace=True)
df["Name"] = df["Name"].fillna("Unknown")
# df.fillna(0, inplace=True)
print(df)
import pandas as pd
data = {
    "Name": ['Ram',None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age" : [28,34,22,30,29,40,25,32],
    "Salary": [50000, 60000,None,52000, 49000, None,48000, 58000],
    "Performance Score": [85,90,78,92,None,95,80,89]
}
df=pd.DataFrame(data)
print(df.isnull().sum())
import pandas as pd
df=pd.read_csv("dis.csv")#load file data
print(df.head())#show 5 1st rows
print(df.shape)#total rows and columns
print(df.isnull().sum())#check missing val
print(df["Temp"].mean())#avg val\
df["Soil_Moisture"] = pd.to_numeric(df["Soil_Moisture"], errors="coerce")
df["Rainfall"] = df["Rainfall"].fillna(df["Rainfall"].mean())#filling val in NaN
df["NDVI"] = df["NDVI"].fillna(df["NDVI"].mean()) #filing val in NaN
df["Soil_Moisture"] = df["Soil_Moisture"].fillna(df["Soil_Moisture"].mean())#filling val in NaN
print(df.isnull().sum())#checking val
print(df[df["Rainfall"] < 200])#shows rainfall under 200
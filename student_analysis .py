import numpy as np

# rows = students, columns = subjects
import pandas as pd
df=pd.read_csv("student-por.csv")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistics:")
print(df.describe())


print("\nAverage Final Grade:", df['G3'].mean())

pass_count = len(df[df['G3'] >= 10])
fail_count = len(df[df['G3'] < 10])

print("Pass:", pass_count)
print("Fail:", fail_count)


top_students = df.sort_values(by='G3', ascending=False).head(5)
print("\nTop 5 Students:")
print(top_students[['G1','G2','G3']])


print("\nAverage grade by study time:")
print(df.groupby('studytime')['G3'].mean())

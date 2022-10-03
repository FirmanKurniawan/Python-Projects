import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv")
print(csv_data.mean())
print("Dataset yang masih terdapat nilai kosong ! :")
print(csv_data.head(10))

csv_data=csv_data.fillna(csv_data.mean())
print("Dataset yang sudah diproses Handling Missing Values dengan Mean :")
print(csv_data.head(10))

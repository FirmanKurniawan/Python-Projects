# https://www.kaggle.com/code/shavilyarajput/gold-price-dataset/notebook
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("FINAL_USO.csv")

X = df.iloc[:, 1:4]
y = df.iloc[:, 5]

# prepocessing process
# fungsi isna melihat data null , memberikan dalam format boolean
# fungsi notna melihat data yang tidak kosong , memberikan info dalam format boolean
X.isna().sum()
# X.shape melihat ukuran baris dan kolom yaitu pada dataset ini terdapat 1718 baris dan 5 kolom


# split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.8, random_state=40
)
X_test.shape

# make a model
model_regressor = LinearRegression()
model_regressor = model_regressor.fit(X_train.values, y_train)

# predict the data
y_pred = model_regressor.predict(X_test.values)

# check evaluasi model
print(model_regressor.score(X_test.values, y_test))

# check evaluesi model use mean squere error
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
print("%", mse)

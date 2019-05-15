from sklearn.datasets import load_boston
boston = load_boston()

import pprint
pprint.pprint(boston)

import pandas as pd

df_x = pd.DataFrame(boston.data, columns = boston.feature_names)
df_y = pd.DataFrame(boston.target)

from sklearn import linear_model
model = linear_model.LinearRegression()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state = 4)

model.fit(x_train, y_train)
result = model.predict(x_test)
print(result[5], y_test)
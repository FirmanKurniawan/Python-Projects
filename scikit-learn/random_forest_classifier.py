import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn import ensemble
from sklearn import metrics
from sklearn.model_selection import train_test_split

iris = load_iris()

X = iris["data"]
Y = iris["target"]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

clf = ensemble.RandomForestClassifier(random_state=42, n_estimators=100)
clf.fit(x_train, y_train)

accuracy = metrics.accuracy_score(y_test, clf.predict(x_test)) * 100
print("Accuracy", round(accuracy, 1))

metrics.plot_confusion_matrix(
  clf,
  x_test,
  y_test,
  display_labels=iris["target_names"],
  cmap="Blues",
  normalize="true",
)
plt.show()

from sklearn import tree
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

dataset = load_iris()
x = dataset.data
y = dataset.target
x_train, x_test, y_train, y_test = train_test_split(x, y)

clf = tree.DecisionTreeClassifier(random_state=0, max_depth=2)

fig = clf.fit(x_train, y_train)
tree.plot_tree(
    fig, feature_names=dataset.feature_names, class_names=dataset.target_names
)
plt.show()

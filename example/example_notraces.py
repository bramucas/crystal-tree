from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

from crystal_tree import CrystalTree

# Loads dataset
X, y = load_iris(return_X_y=True, as_frame=True)

# Trains decision tree
clf = DecisionTreeClassifier()
clf.fit(X,y)

# Translates the classifier into an explainable logic program
crys_tree = CrystalTree(clf)

# Print explanations of input X (two arbitrary rows)
for e in crys_tree.explain(X.iloc[[0, 54]], feature_names=X.columns.tolist()):
    print(e.ascii_tree())

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

from crystal_tree import CrystalTree, Trace

def setup_labels(tree: CrystalTree):
    """Just setups some traces"""
    tree.add_trace(Trace("Predicted iris-virginica", "prediction", target_class=0))
    tree.add_trace(Trace("Predicted iris-versicolor", "prediction", target_class=1))
    tree.add_trace(Trace("Predicted iris-setosa", "prediction", target_class=2))

# Loads dataset
X, y = load_iris(return_X_y=True, as_frame=True)

# Trains decision tree
clf = DecisionTreeClassifier()
clf.fit(X,y)

# Translates the classifier into an explainable logic program
crys_tree = CrystalTree(clf)

# Apply the labels used by the tree
setup_labels(crys_tree)

# Print explanations of input X (first two rows)
for e in crys_tree.explain(X.iloc[[0, 54]]):
    print(e.ascii_tree())

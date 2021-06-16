# crystal-tree

The goal of crystal-tree package is to provide simple natural language explanations for the predictions from decision trees. 

This simple python package provides an object for translating a (for now [scikit-learn](https://scikit-learn.org/stable/)'s) decision tree into an explainable logic program for [xclingo](https://github.com/bramucas/xclingo).

![crystal-tree usage pipeline](doc/cystal-tree-flowchart.png)

## Install
*Use python3*

* Download/clone the repository
* Move into the repository directory
* Then:

```
python -m pip install .
```

## Usage

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

from crystal_tree import CrystalTree

# Loads dataset
X, y = load_iris(return_X_y=True)

# Trains decision tree
clf = DecisionTreeClassifier()s
clf.fit(X,y)

# Translates the classifier into an explainable logic program
crys_tree = CrystalTree(clf)
crys_tree.write_in_files(
    extra="extra.lp",  # output paths for the translation
    paths="paths.lp",
    traces="traces.lp",
)
```

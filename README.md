# crystal-tree
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bramucas/crystal-tree/binder?labpath=example%2Fexamples.ipynb)

The goal of crystal-tree package is to provide simple, crystal-clear, natural language explanations for the predictions from classification Decision Trees. 

This simple python package provides an object for obtaining explanations from a (for now [scikit-learn](https://scikit-learn.org/stable/)'s) Decision Tree Classifier.

The implementations consists in the translation of the Decision Tree into an explainable logic program for [xclingo](https://github.com/bramucas/xclingo).

Given an input, the CrystalTree object will provide the prediction from the original tree, justified by a summarized version of the conditions checked by the tree to ultimately produce the prediction. The explanations are provided as python objects which can be easily represented as text. The text used for the explanations admit some personalization, which allows the user to adapt them particular contexts (different languages, different levels of expertise, etc.)

Try it out without installing anything in [Crystal-tree Binder](https://mybinder.org/v2/gh/bramucas/crystal-tree/binder?labpath=example%2Fexamples.ipynb)


## Installation

```
python -m pip install crystal-tree
```

## Usage

The following program will train a Decision Tree into the task of predicting types of flowers (throught the well-known Iris dataset), and then it will some explanations as an example.
The program requires the following modules to be installed:
```
python -m pip instll sklearn pandas
```

```python
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
for e in crys_tree.explain(X.iloc[[0, 54]]):
    print(e.ascii_tree())
```

This will produce the following output.
```
  *
  |__Predicted class 0 for instance 0
  |  |__petal width (cm) <= 0.8

  *
  |__Predicted class 1 for instance 1
  |  |__petal length (cm) <= 4.9
  |  |__petal width (cm) in (0.8,1.6]
```

More examples concerning personalization of explanations can be found in the ```examples/``` directory in this repository. 
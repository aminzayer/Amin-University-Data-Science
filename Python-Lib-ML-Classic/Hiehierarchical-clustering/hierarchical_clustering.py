from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import numpy as np
X = np.array([[1, 3], [4, 2], [5, 6], [3, 1], [7, 2], [3, 3], ])

#Plotting Data
labels = range(1, 7)
plt.figure(figsize=(7, 3))
plt.subplots_adjust(bottom=0.1)
plt.scatter(X[:, 0], X[:, 1], label='True Position')

for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-3, 3),
        textcoords='offset points', ha='right', va='bottom')
plt.show()

## Use Hierarchical Algorithm Single Method
linked = linkage(X, 'single')
labelList = range(1, 7)
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top',labels=labelList,distance_sort='descending',show_leaf_counts=True)
plt.show()

# Use Hierarchical Algorithm Complete Method
linked = linkage(X, 'complete')
labelList = range(1, 7)
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.show()

# Use Hierarchical Algorithm Average Method
linked = linkage(X, 'average')
labelList = range(1, 7)
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.show()

# Use Hierarchical Algorithm Ward Method
linked = linkage(X, 'ward')
labelList = range(1, 7)
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.show()

# Use Hierarchical Algorithm Centroid Method
linked = linkage(X, 'centroid')
labelList = range(1, 7)
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.show()

# Use Hierarchical Algorithm Median Method
linked = linkage(X, 'median')
labelList = range(1, 7)
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.show()


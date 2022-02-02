# Use Hierarchical Algorithm Single & Avrage & Complete Method
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
import sys
import os
import json
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", module="matplotlib")


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def hierarchical_clustering(data, linkage, no_of_clusters):
    #first step is to calculate the initial distance matrix
    #it consists distances from all the point to all the point
    color = ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'w']
    #initial_distances = pairwise_distances(data, metric='euclidean')
    initial_distances = pairwise_distances(data, metric='cityblock')
    #making all the diagonal elements infinity
    np.fill_diagonal(initial_distances, sys.maxsize)
    clusters = find_clusters(initial_distances, linkage)

    #plotting the clusters
    iteration_number = initial_distances.shape[0] - no_of_clusters
    clusters_to_plot = clusters[iteration_number]
    arr = np.unique(clusters_to_plot)

    indices_to_plot = []
    fig = plt.figure()
    fig.suptitle('Scatter Plot for clusters')
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    for x in np.nditer(arr):
        indices_to_plot.append(np.where(clusters_to_plot == x))
    p = 0

    print(clusters_to_plot)
    for i in range(0, len(indices_to_plot)):
        for j in np.nditer(indices_to_plot[i]):
            ax.scatter(data[j, 0], data[j, 1], c=color[p])
        p = p + 1

    plt.show()


def cal_dist_from_centroid(index, row_index, col_index):
     # Calculate Distance From Centroid
    return 

def find_clusters(input, linkage):
    clusters = {}
    row_index = -1
    col_index = -1
    array = []

    for n in range(input.shape[0]):
        array.append(n)

    clusters[0] = array.copy()

    #finding minimum value from the distance matrix
    #note that this loop will always return minimum value from bottom triangle of matrix
    for k in range(1, input.shape[0]):
        min_val = sys.maxsize
        

        for i in range(0, input.shape[0]):
            for j in range(0, input.shape[1]):
                if(input[i][j] <= min_val):
                    min_val = input[i][j]
                    row_index = i
                    col_index = j
        print("\nLevel ",k," Matrix :","\n")
        s = [[str(round(e)) for e in row] for row in input]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table),"\n")


        #once we find the minimum value, we need to update the distance matrix
        #updating the matrix by calculating the new distances from the cluster to all points

        #for Single Linkage
        if(linkage == "single" or linkage == "Single"):
            for i in range(0, input.shape[0]):
                if(i != col_index):
                    #we calculate the distance of every data point from newly formed cluster and update the matrix.
                    temp = min(input[col_index][i], input[row_index][i])
                    #we update the matrix symmetrically as our distance matrix should always be symmetric
                    input[col_index][i] = temp
                    input[i][col_index] = temp

        #for Complete Linkage
        elif(linkage == "Complete" or linkage == "complete"):
            for i in range(0, input.shape[0]):
                if(i != col_index and i != row_index):
                    temp = min(input[col_index][i], input[row_index][i])
                    input[col_index][i] = temp
                    input[i][col_index] = temp

        #for Average Linkage
        elif(linkage == "Average" or linkage == "average"):
            for i in range(0, input.shape[0]):
                if(i != col_index and i != row_index):
                    temp = (input[col_index][i]+input[row_index][i])/2
                    input[col_index][i] = temp
                    input[i][col_index] = temp

        elif(linkage == "Centroid" or linkage == "centroid"):
            for i in range(0, input.shape[0]):
                if(i != col_index and i != row_index):
                    dist_centroid = cal_dist_from_centroid(i, row_index, col_index)
                    input[col_index][i] = dist_centroid
                    input[i][col_index] = dist_centroid

        #set the rows and columns for the cluster with higher index i.e. the row index to infinity
        #Set input[row_index][for_all_i] = infinity
        #set input[for_all_i][row_index] = infinity
        for i in range(0, input.shape[0]):
            input[row_index][i] = sys.maxsize
            input[i][row_index] = sys.maxsize

        
        #Manipulating the dictionary to keep track of cluster formation in each step
        #if k=0,then all datapoints are clusters
        
        minimum = min(row_index, col_index)
        maximum = max(row_index, col_index)
        for n in range(len(array)):
            if(array[n] == maximum):
                array[n] = minimum
        clusters[k] = array.copy()

    return clusters


clearConsole()
#Our Dataset
data = np.array([4, 3, 1, 5, 8, 3, 6, 8, 5, 9]).reshape(5, 2)
#data = np.array([1, 2, 3, 1, 7, 5, 3, 3, 8, 8, 3, 9 ,2 ,2]).reshape(7, 2)
#data = np.array([1, 3, 4, 2, 5, 6, 3, 1, 7, 2, 3, 3]).reshape(6, 2)
print(data)

# Visualising Data
# fig = plt.figure()
# fig.suptitle('Scatter Plot for clusters')
# ax = fig.add_subplot(1, 1, 1)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.scatter(data[:, 0], data[:, 1])
# plt.show()


# initial_distances = pairwise_distances(data, metric='cityblock')
initial_distances = np.array([0, 5, 4, 8, 10, 5, 0, 6, 2, 7, 4, 6, 0, 9, 4, 8, 2, 9, 0, 3, 10, 7, 4, 3, 0]).reshape(5, 5)
print(initial_distances)
np.fill_diagonal(initial_distances, sys.maxsize)
clusters = find_clusters(initial_distances, "complete")
print(json.dumps(clusters, indent=2))
#plotting the clusters

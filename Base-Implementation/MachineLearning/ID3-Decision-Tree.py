from turtle import clear
import pandas as pd
import numpy as np
import os
import json

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def calc_total_entropy(train_data, label, class_list):
    total_row = train_data.shape[0]
    total_entr = 0
    total_class_print = ""
    total_Entropy_print = ""

    for c in class_list:
        total_class_count = train_data[train_data[label] == c].shape[0]
        total_class_entr = - (total_class_count/total_row) * \
            np.log2(total_class_count/total_row)
        total_class_print = " - (" + str(total_class_count) + "/" + str(
            total_row) + ")log("+str(total_class_count) + "/" + str(total_row)+")"
        total_Entropy_print += total_class_print
        total_entr += total_class_entr

    #print("Total Entropy =", total_Entropy_print, " = ", total_entr)
    return total_entr


def calc_entropy(feature_value_data, label, class_list):
    class_count = feature_value_data.shape[0]
    entropy = 0

    for c in class_list:
        label_class_count = feature_value_data[feature_value_data[label] == c].shape[0]

        entropy_class = 0
        if label_class_count != 0:
            probability_class = label_class_count/class_count
            entropy_class = - probability_class * np.log2(probability_class)

        entropy += entropy_class
    return entropy


def calc_info_gain(feature_name, train_data, label, class_list):
    feature_value_list = train_data[feature_name].unique()
    total_row = train_data.shape[0]
    feature_info = 0.0
    Entropy_Total_Root = calc_total_entropy(train_data, label, class_list)
    print("Total Entropy for Root =",
          label, " = ", Entropy_Total_Root)
    print("Gain Label of (", feature_name, " = ", feature_value_list, ") = ", Entropy_Total_Root -
          feature_info, " - [", end=" "),

    for feature_value in feature_value_list:
        feature_value_data = train_data[train_data[feature_name]
                                        == feature_value]
        feature_value_count = feature_value_data.shape[0]
        feature_value_entropy = calc_entropy(
            feature_value_data, label, class_list)
        feature_value_probability = feature_value_count/total_row
        feature_info += feature_value_probability * feature_value_entropy
        print(" (", str(feature_value_count), "/",
              total_row, " ) x (Entropy (", feature_value, ")=", feature_value_entropy, ") + ", end=" "),
    
    print("] = ", Entropy_Total_Root - feature_info )
    return Entropy_Total_Root - feature_info


def find_most_informative_feature(train_data, label, class_list):
    feature_list = train_data.columns.drop(label)
    max_info_gain = -1
    max_info_feature = None

    for feature in feature_list:
        feature_info_gain = calc_info_gain(
            feature, train_data, label, class_list)
        if max_info_gain < feature_info_gain:
            max_info_gain = feature_info_gain
            max_info_feature = feature
    print("------------------------------------")
    print ("Max Feature is = ",max_info_feature)
    print("------------------------------------")
    return max_info_feature


def generate_sub_tree(feature_name, train_data, label, class_list):
    feature_value_count_dict = train_data[feature_name].value_counts(
        sort=False)
    tree = {}

    for feature_value, count in feature_value_count_dict.iteritems():
        feature_value_data = train_data[train_data[feature_name]
                                        == feature_value]

        assigned_to_node = False
        for c in class_list:
            class_count = feature_value_data[feature_value_data[label] == c].shape[0]

            if class_count == count:
                tree[feature_value] = c
                train_data = train_data[train_data[feature_name]
                                        != feature_value]
                assigned_to_node = True
        if not assigned_to_node:
            tree[feature_value] = "?"

    return tree, train_data


def make_tree(root, prev_feature_value, train_data, label, class_list):
    if train_data.shape[0] != 0:
        max_info_feature = find_most_informative_feature(
            train_data, label, class_list)
        tree, train_data = generate_sub_tree(
            max_info_feature, train_data, label, class_list)
        next_root = None

        if prev_feature_value != None:
            root[prev_feature_value] = dict()
            root[prev_feature_value][max_info_feature] = tree
            next_root = root[prev_feature_value][max_info_feature]
        else:
            root[max_info_feature] = tree
            next_root = root[max_info_feature]

        for node, branch in list(next_root.items()):
            if branch == "?":
                feature_value_data = train_data[train_data[max_info_feature] == node]
                make_tree(next_root, node, feature_value_data,
                          label, class_list)


def id3(train_data_m, label):
    train_data = train_data_m.copy()
    tree = {}
    class_list = train_data[label].unique()
    make_tree(tree, None, train_data_m, label, class_list)

    return tree


def id3_withLabel(train_data_m, label,feature):
    train_data = train_data_m.copy()
    tree = {}
    class_list = train_data[label].unique()
    make_tree(tree, feature, train_data_m, label, class_list)
    return tree

def predict(tree, instance):
    if not isinstance(tree, dict):
        return tree
    else:
        root_node = next(iter(tree))
        feature_value = instance[root_node]
        if feature_value in tree[root_node]:
            return predict(tree[root_node][feature_value], instance)
        else:
            return None


def evaluate(tree, test_data_m, label):
    correct_preditct = 0
    wrong_preditct = 0
    for index, row in test_data_m.iterrows():
        result = predict(tree, test_data_m.iloc[index])
        if result == test_data_m[label].iloc[index]:
            correct_preditct += 1
        else:
            wrong_preditct += 1
    accuracy = correct_preditct / (correct_preditct + wrong_preditct)
    return accuracy


# data = pd.DataFrame([['x1', 'a1', 'b1', 'c1', '+'],
#                      ['x2', 'a2', 'b2', 'c1', '-'],
#                      ['x3', 'a1', 'b2', 'c2', '+'],
#                      ['x4', 'a3', 'b1', 'c1', '+'],
#                      ['x5', 'a3', 'b2', 'c1', '-'],
#                      ['x6', 'a2', 'b1', 'c2', '-']],
#                     columns=['sample', 'A', 'B', 'C', 'Class'])

# attribute = np.array(data)[:, 1:-1]
# print("\nInstances are:\n", attribute)
# target = np.array(data)[:, -1]
# print("\nTarget Values are: ", target)
# train_data = np.array(data)[:, 1:]
# print("\nInstances are:\n", train_data)

# importing the dataset from the disk
# train_data_m = pd.read_csv(
#     "ML-Coding-Practice-Example/University-Projects/dataset.csv")

# # making an array of all the attributes
# data = np.array(train_data_m)
# #print("\n Attributes : \n", data)

# class_label = np.array(train_data_m)[:, -1]
# #print("\n Class : \n", class_label)

# tree = id3(train_data_m, 'Class')
# print(tree)

# train_data_m = pd.read_csv(
#     "ML-Coding-Practice-Example/University-Projects/Car-Example.csv")

# # making an array of all the attributes
# data = np.array(train_data_m)
# #print("\n Attributes : \n", data)


# class_label = np.array(train_data_m)[:, -1]
# #print("\n Class : \n", class_label)

# tree = id3(train_data_m, 'Class')
# print(tree)

# Clear Console
clearConsole()


train_data_p = pd.read_csv(
    "ML-Coding-Practice-Example/University-Projects/Data-ID3.csv")

print(train_data_p)
# making an array of all the attributes
data = np.array(train_data_p)
#print("\n Attributes : \n", data)

print(train_data_p)
class_label = np.array(train_data_p)[:, -1]
#print("\n Class : \n", class_label)

tree = id3(train_data_p, 'Class')
print(json.dumps(tree, indent=1))
print (tree)

# tree = id3_withLabel (train_data_p,"F1", 'Class')
# print(json.dumps(tree, indent=1))
# print(tree)

from math import *


def euclidean_distance(x, y):
    print("√", end=" "),
    for i in x:
        print("(", x[i-1], "-", y[i-1], ")²+", end=" "),

    print("=", end=" "),

    return sqrt(sum(pow(a-b, 2) for a, b in zip(x, y)))


def manhattan_distance(x, y):
    for i in x:
        print("|", x[i-1], "-", y[i-1], "| +", end=" "),

    print("=", end=" "),
    return sum(abs(a-b) for a, b in zip(x, y))


def minkowski_distance(a, b, p):
    print("max [", end=" "),
    for i in a:
        print("|", a[i-1], "-", b[i-1], "| +", end=" "),

    print("=", end=" "),
    return sum(abs(e1-e2)**p for e1, e2 in zip(a, b))**(1/p)


def Cosine_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    denominator = round(sqrt(len(set(x))) * sqrt(len(set(y))), 2)
    print("\n|", set(x), " ∩ ", set(y), " = ", intersection_cardinality,
          "| / √|", set(x), "| * √|", set(y), " = ", denominator, "| \n")
    print("similarity Cosine is = ", intersection_cardinality,
          " / ", denominator, end=" = "),
    print(round(intersection_cardinality/float(denominator), 2))
    return round(intersection_cardinality/float(denominator), 2)


def Cosine_Distance(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    denominator = round(sqrt(len(set(x))) * sqrt(len(set(y))), 2)
    print("Cosine Distance is = 1 - (", intersection_cardinality, " / ",
          denominator, ") = ", 1 - round(intersection_cardinality/denominator, 2))
    return 1 - round(intersection_cardinality/float(denominator), 2)


def jaccard_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    print("\n|", set(x), " ∩ ", set(y), " = ", intersection_cardinality,
          "| / |", set(x), " ∪ ", set(y), " = ", union_cardinality, "| \n")
    print("similarity Jacarad is = ", intersection_cardinality,
          " / ", union_cardinality, end=" = "),
    print(intersection_cardinality/float(union_cardinality))
    return intersection_cardinality/float(union_cardinality)


def Jaccard_Distance(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    print("Distance Jacarad is = 1 - (", intersection_cardinality, " / ",
          union_cardinality, ") = ", 1 - intersection_cardinality/float(union_cardinality))
    return 1 - intersection_cardinality/float(union_cardinality)


def Dice_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    denominator = len(set(x)) + len(set(y))
    print("\n2 * |", set(x), " ∩ ", set(y), " = ", intersection_cardinality,
          "| / |", set(x), " ∪ ", set(y), " = ", denominator, "| \n")
    print("Dice similarity is = ", 2 * intersection_cardinality,
          " / ", denominator, end=" = "),
    print((2*intersection_cardinality)/denominator)
    return (2*intersection_cardinality)/denominator


def Dice_Distance(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    denominator = len(set(x)) + len(set(y))
    print("Dice Distance is = 1 - (", 2 * intersection_cardinality, " / ",
          denominator, ") = ", 1 - (2*intersection_cardinality)/denominator)
    return 1 - (2*intersection_cardinality)/denominator


def N_Jaccard_simlilarity_Distance(x, y):
    X_Y = sum((a*b) for a, b in zip(x, y))
    X2_Y2 = sum(pow(a, 2) for a in x)+sum(pow(b, 2) for b in y)
    print("Numerical Jaccard similarity is =  (", X_Y,
          ") / (", X2_Y2, ") - (", X_Y, ") = ", X_Y, "/", X2_Y2 - X_Y, end=" = ")
    return X_Y / (X2_Y2 - X_Y), "Distance is = 1- Simlilarity = " + str(1 - (X_Y / (X2_Y2 - X_Y)))


def N_Dice_simlilarity_Distance(x, y):
    X_Y = sum((a*b) for a, b in zip(x, y))
    X2_Y2_P2 = sum(pow(a, 2) for a in x)+sum(pow(b, 2) for b in y)
    print("Numerical Dice similarity is = 2 * (", X_Y,
          ") / (", X2_Y2_P2, ") = ", 2 * X_Y, "/", X2_Y2_P2, end=" = ")
    return (2 * X_Y) / (X2_Y2_P2), "Distance is = 1- Simlilarity = " + str(1 - (X_Y / X2_Y2_P2))


def N_Cosine_simlilarity_Distance(x, y):
    X_Y = sum((a*b) for a, b in zip(x, y))
    SX2 = sqrt(sum(pow(a, 2) for a in x))
    SY2 = sqrt(sum(pow(b, 2) for b in y))
    print("Numerical Cosine similarity is = (", X_Y,
          ") / (", SX2, " * ", SY2, ") = ", X_Y, "/", SX2*SY2, end=" = ")
    return (X_Y) / (SX2*SY2), "Distance is = 1- Simlilarity = " + str(1 - (X_Y / SX2*SY2))

s1 = [2, 1, 1, 1]
s2 = [1, 3, 0, 2]
print(N_Jaccard_simlilarity_Distance(s1, s2))
print(N_Dice_simlilarity_Distance(s1, s2))
print(N_Cosine_simlilarity_Distance(s1, s2))


# Test Function
def Test_jaccard_similarity():
    if jaccard_similarity(["A", "B", "C"], ["A", "B", "C"])== 1:
        print ("\n1 Test Was Passed")
    else:
        print("\n1 Test Was Not Passed")

    if jaccard_similarity(["A", "B", "C"], ["E", "D", "F"]) == 0:
        print("\n2 Test Was Passed")
    else:
        print("\n2 Test Was Not Passed")

Test_jaccard_similarity()


# Test Data
print(euclidean_distance([2, 0, 1, 2], [1, 1, 1, 1]))
print(manhattan_distance([2, 0, 1, 2], [1, 1, 1, 1]))
print(minkowski_distance([2, 0, 1, 2], [1, 1, 1, 1], 1))
print(jaccard_similarity([2, 0, 1, 2], [1, 1, 1, 1]))
jaccard_similarity(["A", "B", "C"], ["A", "D", "E", "F"])
Jaccard_Distance(["A", "B", "C"], ["A", "D", "E", "F"])

Dice_similarity(["A", "B", "C"], ["A", "B","D","E","F"])
Dice_Distance(["A", "B", "C"], ["A", "B", "D", "E", "F"])
Cosine_similarity(["A", "B", "C"], ["A", "B", "D", "E", "F"])
Cosine_Distance(["A", "B", "C"], ["A", "B", "D", "E", "F"])
print(jaccard_similarity(["A", "B", "C"], ["A", "B", "C"]))
print(jaccard_similarity(["A", "B", "C"], ["D", "E", "F"]))
X = ["A", "B", "C"]
Y = ["A", "B", "C"]
X = ["A", "B", "C"]
Y = ["D", "E", "F"]

X = [2, 1, 1, 1]
Y = [1, 3, 0, 2]
jaccard_similarity(X, Y)
Jaccard_Distance(X, Y)
Dice_similarity(X, Y)
Dice_Distance(X, Y)
Cosine_similarity(X, Y)
Cosine_Distance(X, Y)

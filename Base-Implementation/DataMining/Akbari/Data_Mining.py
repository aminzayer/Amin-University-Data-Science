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
    print("\n|", set(x), " ∩ ", set(y), " = ", intersection_cardinality,"| / √|", set(x), "| * √|", set(y), " = ", denominator, "| \n")
    print("similarity Cosine is = ", intersection_cardinality," / ", denominator, end=" = "),
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
    print("\n|", set(x), " ∩ ", set(y), " = ", intersection_cardinality,"| / |", set(x), " ∪ ", set(y), " = ", union_cardinality, "| \n")
    print("similarity Jacarad is = ", intersection_cardinality," / ", union_cardinality, end=" = "),
    print(intersection_cardinality/float(union_cardinality))
    return intersection_cardinality/float(union_cardinality)


def Jaccard_Distance(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    print("Distance Jacarad is = 1 - (", intersection_cardinality, " / ",union_cardinality, ") = ", 1 - intersection_cardinality/float(union_cardinality))
    return 1 - intersection_cardinality/float(union_cardinality)


def Dice_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    denominator = len(set(x)) + len(set(y))
    print("\n2 * |", set(x), " ∩ ", set(y), " = ", intersection_cardinality,"| / |", set(x), " ∪ ", set(y), " = ", denominator, "| \n")
    print("Dice similarity is = ", 2 * intersection_cardinality," / ", denominator, end=" = "),
    print((2*intersection_cardinality)/denominator)
    return (2*intersection_cardinality)/denominator


def Dice_Distance(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    denominator = len(set(x)) + len(set(y))
    print("Dice Distance is = 1 - (", 2 * intersection_cardinality, " / ",denominator, ") = ", 1 - (2*intersection_cardinality)/denominator)
    return 1 - (2*intersection_cardinality)/denominator

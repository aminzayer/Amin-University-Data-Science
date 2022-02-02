# Python Program to Implement Candidate Elimination Algorithm to get Consistent Version Space
import numpy as np
import pandas as pd

# to read the data in the csv file or Create Data frame
# ---------------- Read File Codes ------------
#data = pd.read_csv('enjoysport.csv')
#concepts = np.array(data.iloc[:, 0:-1])
#print("\nInstances are:\n", concepts)
#target = np.array(data.iloc[:, -1])
#print("\nTarget Values are: ", target)
# ----------- Create DataFrame Codes ----------
data = pd.DataFrame([['Morning', 'Sunny', 'Warm', 'Yes', 'Mild', 'Strong', 'Yes'],
                     ['Evening', 'Rainy', 'Cold', 'No', 'Mild', 'Normal', 'No'],
                     ['Morning', 'Sunny', 'Moderate',
                         'Yes', 'Normal', 'Normal', 'Yes'],
                     ['Evening', 'Sunny', 'Cold', 'Yes', 'High', 'Strong', 'Yes'],
                     ['Morning', 'Sunny', 'Moderate', 'Yes', 'Mild', 'Strong', 'Yes']],
                    columns=['Time', 'Weather', 'Temperature', 'Company', 'Humidity', 'Wind', 'Goes'])

concepts = np.array(data)[:, :-1]
print("\nInstances are:\n", concepts)
target = np.array(data)[:, -1]
print("\nTarget Values are: ", target)


# training function to implement Candidate Elimination Algorithm
def learn(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [["?" for i in range(len(specific_h))]
                 for i in range(len(specific_h))]

    for i, h in enumerate(concepts):
        if target[i] == "yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'

        if target[i] == "no":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
        print("\nClass Target is : ", target[i], "\n specific_h : \n", specific_h,
              "\n general_h : \n", general_h, "\n")

    indices = [i for i, val in enumerate(general_h) if val == [
        '?', '?', '?', '?', '?', '?']]
    
    print("Final Level Removing :\n specific_h : \n", specific_h,
          "\n general_h : \n", general_h, "\n")

    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])

    return specific_h, general_h

# s_final, g_final = learn(concepts, target)

# print("Final Specific_h: ", s_final, sep="\n")
# print("Final General_h: ", g_final, sep="\n")


# New DataFrame For test
data = pd.DataFrame([['a1', 'b2', 'c1', 'd3', 'e2', 'f1', 'Yes'],
                     ['a1', 'b2', 'c2', 'd3', 'e1', 'f1', 'No'],
                     ['a1', 'b3', 'c1', 'd3', 'e1', 'f1', 'Yes'],
                     ['a1', 'b1', 'c1', 'd3', 'e3', 'f1', 'Yes'],
                     ['a2', 'b2', 'c1', 'd3', 'e3', 'f3', 'Yes']],
                    columns=['A', 'B', 'C', 'D', 'E', 'F', 'Target'])

concepts = np.array(data)[:, :-1]
print("\nInstances are:\n", concepts)
target = np.array(data)[:, -1]
print("\nTarget Values are: ", target)

s_final, g_final = learn(concepts, target)

print("Final Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")


# read Dataset for test
data = pd.DataFrame(pd.read_csv(
    'ML-Coding-Practice-Example/University-Projects/find-s.csv'))
concepts = np.array(data.iloc[:, :-1])
target = np.array(data.iloc[:, -1])

concepts = np.array(data)[:, :-1]
print("\nInstances are:\n", concepts)
target = np.array(data)[:, -1]
print("\nTarget Values are: ", target)

s_final, g_final = learn(concepts, target)

print("Final Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")

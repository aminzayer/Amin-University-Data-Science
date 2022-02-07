# Import pulp
from pulp import *

# Create an Instance of LpProblem
problem = LpProblem('Car Factory', LpMaximize)

# Create Decision Variables
A = LpVariable('Car A', lowBound=0, cat=LpInteger)
B = LpVariable('Car B', lowBound=0, cat=LpInteger)

#Objective Function
problem += 20000*A + 45000*B, 'Objective Function'

#Constraints
problem += 4*A + 5*B <= 30, 'Designer Constraint'
problem += 3*A + 6*B <= 30, 'Engineer Constraint'
problem += 2*A + 7*B <= 30, 'Machine Constraint'

# Car_Profit:
# MAXIMIZE
# 20000*Car_A + 45000*Car_B + 0
# SUBJECT TO
# Designer_Constraint: 4 Car_A + 5 Car_B <= 30
# Engineer_Constraint: 3 Car_A + 6 Car_B <= 30
# Machine_Constraint: 2 Car_A + 7 Car_B <= 30
# VARIABLES
# 0 <= Car_A Integer
# 0 <= Car_B Integer
print(problem)

print("Current Status: ", LpStatus[problem.status])

problem.solve()
print("Number of Car A Made: ", A.varValue)
print("Number of Car B Made: ", B.varValue)
print("Total Profit: ", value(problem.objective))

# Maximize:  Z = 2x + 4y
# Subject to the constraints:
# 3x + y <= 3
# x - y <= 4
# 2x + y <= 3
# x, y >= 0

# import the library pulp as p
import pulp as p

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMaximize)

# Create problem Variables
x = p.LpVariable("x", lowBound=0)  # Create a variable x >= 0
y = p.LpVariable("y", lowBound=0)  # Create a variable y >= 0

# Objective Function
Lp_prob += 2 * x + 4 * y

# Constraints:
Lp_prob += 3 * x + y <= 3
Lp_prob += x - y <= 4
Lp_prob += 2 * x + y <= 3

# Display the problem
print(Lp_prob)

status = Lp_prob.solve()  # Solver
print(p.LpStatus[status])  # The solution status

# Printing the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective))

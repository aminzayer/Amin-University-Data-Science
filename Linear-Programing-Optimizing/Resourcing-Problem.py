# Resourcing Problem

# We’re consulting for a boutique car manufacturer, producing luxury cars.

# They run on one month(30 days) cycles, we have one cycle to show we can provide value.

# There is one robot, 2 engineers and one detailer in the factory. The detailer has some holiday off, so only has 21 days available.

# The 2 cars need different time with each resource:

# Robot time: Car A – 3 days
# Car B – 4 days.

# Engineer time: Car A – 5 days
# Car B – 6 days.

# Detailer time: Car A – 1.5 days
# Car B – 3 days.

# Car A provides €30, 000 profit, whilst Car B offers €45, 000 profit.

# At the moment, they produce 4 of each cars per month, for €300, 000 profit. Not bad at all, but we think we can do better for them.

# This can be modelled as follows:

# Objective Maximise
# Profit = 30,000 A + 45,000 B

# Subject to:
# A ≥ 0 & B ≥ 0
# 3A + 4B ≤ 30
# 5A + 6B ≤ 60
# 1.5A + 3B ≤ 21


# import the library pulp as p
import pulp as p

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Resourcing Problem', p.LpMaximize)

# Create problem Variables
A = p.LpVariable("A", lowBound=0)  # Create a variable x >= 0
B = p.LpVariable("B", lowBound=0)  # Create a variable y >= 0

# Objective Function
Lp_prob += 30000 * A + 45000 * B

# Constraints:
Lp_prob += 3 * A + 4 * B <= 30
Lp_prob += 5 * A + 6 * B <= 60
Lp_prob += 1.5 * A + 3 * B <= 21

# Display the problem
print(Lp_prob)

status = Lp_prob.solve()  # Solver
print(p.LpStatus[status])  # The solution status

# Printing the final solution
print(p.value(A), p.value(B), p.value(Lp_prob.objective))

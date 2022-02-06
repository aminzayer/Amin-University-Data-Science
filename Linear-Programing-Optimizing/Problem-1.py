from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

model = LpProblem(name="small-problem", sense=LpMaximize)

# Initialize the decision variables
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

#expression = 2 * x + 4 * y
#constraint = 2 * x + 4 * y >= 8

model += (2 * x + y <= 20, "red_constraint")
model += (4 * x - 5 * y >= -10, "blue_constraint")
model += (-x + 2 * y >= -2, "yellow_constraint")
model += (-x + 5 * y == 15, "green_constraint")

# Add the objective function to the model
model += x + 2 * y

print(model)
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")

print(model.variables())
print(model.variables()[0])
print(model.variables()[1])

print(model.solver)
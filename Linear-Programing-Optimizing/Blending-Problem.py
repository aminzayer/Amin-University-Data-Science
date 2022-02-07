# Blending Problem
# We’re going to make some sausages!

# We have the following ingredients available to us:
# Ingredient 	Cost(€/ kg) 	Availability(kg)
# Pork 	4.32 	30
# Wheat 	2.46 	20
# Starch 	1.86 	17

# We’ll make 2 types of sausage:

#     Economy (> 40 % Pork)
#     Premium (> 60 % Pork)

# One sausage is 50 grams(0.05 kg)

# According to government regulations, the most starch we can use in our sausages is 25%

# We have a contract with a butcher, and have already purchased 23 kg pork, that must go in our sausages.

# We have a demand for 350 economy sausages and 500 premium sausages.

# We need to figure out how to most cost effectively blend our sausages.

# Let’s model our problem:

# pe = Pork in the economy sausages(kg)we = Wheat in the economy sausages(kg)se = Starch in the economy sausages(kg)pp = Pork in the premium sausages(kg)wp = Wheat in the premium sausages(kg)sp = Starch in the premium sausages(kg)

# We want to minimise costs such that:

# Cost = 4.32(pe+pp)+2.46(we+wp)+1.86(se+sp)

# With the following constraints:

# pe+we+se = 350×0.05pp+wp+sp = 500×0.05pe≥0.4(pe+we+se)pp≥0.6(pp+wp+sp)se≤0.25(pe+we+se)sp≤0.25(pp+wp+sp)pe+pp≤30we+wp≤20se+sp≤17pe+pp≥23


# import the library pulp as p
import pulp

# Instantiate our problem class
model = pulp.LpProblem("Cost minimising blending problem", pulp.LpMinimize)

# Construct our decision variable lists
sausage_types = ['economy', 'premium']
ingredients = ['pork', 'wheat', 'starch']

# Objective Function
ing_weight = pulp.LpVariable.dicts("weight kg",
                                   ((i, j)
                                    for i in sausage_types for j in ingredients),
                                   lowBound=0,
                                   cat='Continuous')

# Objective Function
model += (
    pulp.lpSum([
        4.32 * ing_weight[(i, 'pork')]
        + 2.46 * ing_weight[(i, 'wheat')]
        + 1.86 * ing_weight[(i, 'starch')]
        for i in sausage_types])
)

# Constraints
# 350 economy and 500 premium sausages at 0.05 kg
model += pulp.lpSum([ing_weight['economy', j]
                    for j in ingredients]) == 350 * 0.05
model += pulp.lpSum([ing_weight['premium', j]
                    for j in ingredients]) == 500 * 0.05

# Economy has >= 40% pork, premium >= 60% pork
model += ing_weight['economy', 'pork'] >= (
    0.4 * pulp.lpSum([ing_weight['economy', j] for j in ingredients]))

model += ing_weight['premium', 'pork'] >= (
    0.6 * pulp.lpSum([ing_weight['premium', j] for j in ingredients]))

# Sausages must be <= 25% starch
model += ing_weight['economy', 'starch'] <= (
    0.25 * pulp.lpSum([ing_weight['economy', j] for j in ingredients]))

model += ing_weight['premium', 'starch'] <= (
    0.25 * pulp.lpSum([ing_weight['premium', j] for j in ingredients]))

# We have at most 30 kg of pork, 20 kg of wheat and 17 kg of starch available
model += pulp.lpSum([ing_weight[i, 'pork'] for i in sausage_types]) <= 30
model += pulp.lpSum([ing_weight[i, 'wheat'] for i in sausage_types]) <= 20
model += pulp.lpSum([ing_weight[i, 'starch'] for i in sausage_types]) <= 17

# We have at least 23 kg of pork to use up
model += pulp.lpSum([ing_weight[i, 'pork'] for i in sausage_types]) >= 23


# Display the problem
# Solve our problem
model.solve()
print(pulp.LpStatus[model.status])

for var in ing_weight:
    var_value = ing_weight[var].varValue
    print ("The weight of {0} in {1} sausages is {2} kg".format(var[1], var[0], var_value))

# Printing the final solution
total_cost = pulp.value(model.objective)
print ("The total cost is €{} for 350 economy sausages and 500 premium sausages".format(round(total_cost, 2)))

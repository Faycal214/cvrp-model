from cvrp.cvrp import *

model = cvrp(nb_individus = 10, nb_mutation = 45, nb_iteration = 250, nb_vehicule = 3, nb_client = 6)

print(model.best_solution())

print(model.best_route())

print(model.create_graph())

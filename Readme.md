# CVRP Package

This Python package provides functionalities for solving the Capacitated Vehicle Routing Problem (CVRP) using a genetic algorithm approach.

## Installation

You can install the package using pip:

```bash
pip install cvrp-genetic

## Usage 

from cvrp_genetic import CVRP

# Initialize the CVRP instance with parameters
cvrp_solver = CVRP(nb_individus=100, nb_mutation=10, nb_iteration=100)

# Find the best solution
best_solution = cvrp_solver.best_solution()

# Get the best route
best_route = cvrp_solver.best_route()

# Create a graph of the best route
cvrp_solver.create_graph()

## Documentation
For detailed documentation and examples, refer to the documentation.

## Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests on GitHub.

## License
This project is licensed under the MIT License.
for any questions or inquiries, feel free to contact faycal213.dz@gmail.com




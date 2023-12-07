import random
import matplotlib.pyplot as plt
import numpy as np
from pyswarms.single import GlobalBestPSO
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
from pyswarms.utils.plotters.formatters import Mesher, Designer

# Define Parameters
d = 20
N = d + 1  # Number of genes in an individual
P = 500  # Size of the population
GENS = 500  # Number of generations
MIN = -5  # Generate the initial population with real-valued genes (Lowest possible value)
MAX = 10  # Generate the initial population with real-valued genes (Highest possible value)

# Lists to store the population and offspring
population = []  # Initialize the population list
offspring = []  # Initialize the offspring list


# Define an individual as a class
class Individual:
    def __init__(self, genes=None):  # Modify the constructor to accept genes as an argument
        self.genes = genes if genes is not None else [0.0] * N  # Initialize genes as a list of real numbers
        self.fitness = 0  # Initialize fitness as zero


for _ in range(P):
    tempgene = [random.uniform(MIN, MAX) for _ in range(N)]
    newind = Individual(genes=tempgene)  # Pass the generated genes as an argument
    population.append(newind)  # Add the individual to the population list


# Define a test function that calculates the utility based on genes
def test_function(ind):
    n = len(ind.genes)
    sum_part = sum((0.5 * i * ind.genes[i-1])**2 for i in range(1, n))
    return sum(x ** 2 for x in ind.genes) + sum_part


# Convert population and test_function to np.array for pyswarms
pop_position = np.array([ind.genes for ind in population])
pop_fitness = np.array([ind.fitness for ind in population])

# Define the PSO optimizer
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
optimizer = GlobalBestPSO(n_particles=P, dimensions=N, options=options)


# Define the objective function for PSO
def objective_function(position):
    fitness_values = np.array([test_function(Individual(genes=position[i])) for i in range(position.shape[0])])
    return fitness_values


# Run the PSO optimizer
best_position, _ = optimizer.optimize(objective_function, iters=GENS)


# Plot the sphere function's mesh for better plots
m = Mesher(func=fx.sphere, limits=[(-1, 1), (-1, 1)])
# Adjust figure limits
d = Designer(limits=[(-1, 1), (-1, 1), (-0.1, 1)], label=['x-axis', 'y-axis', 'z-axis'])

# Create a particle history for visualization
particle_history = np.array([m.compute_history_3d(np.array(p)) for p in optimizer.pos_history])

# Create the surface animation
animation3d = plot_surface(pos_history=particle_history,
                           mesher=m, designer=d,
                           mark=(0, 0, 0))

# Assign the animation to a variable
anim = animation3d

# Display the animation
plt.show()
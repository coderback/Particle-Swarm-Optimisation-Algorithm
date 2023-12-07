# Particle-Swarm-Optimisation-Algorithm with PySwarms

This repository contains a Python code for implementing Particle Swarm Optimization (PSO) to solve a minimization problem using the PySwarms library. PSO is a population-based optimization algorithm inspired by the social behavior of birds and fish. In particle swarm optimization a population of potential solutions are represented by particles which move through the search space in of an optimization function in order to find the optimal solution to the function. Each particle moves through the search space based on its own experience and the experience of nearby particles.

## Getting Started

These instructions will help you set up and run the PSO algorithm on your machine.

### Prerequisites

Make sure you have the required Python packages installed. You can install them using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
### Configuration
You can adjust the following parameters in the script to customize the optimization process:

- Number of genes (dimensions) in an individual (d)
- Size of the population (P)
- Number of generations (GENS)
- Range for the value of genes generated for the population (MIN and MAX)

### Results
The script will output the best position found by the PSO algorithm along with the corresponding fitness value over the specified numver of generations.

### Acknowledgments
PySwarms library for PSO implementation

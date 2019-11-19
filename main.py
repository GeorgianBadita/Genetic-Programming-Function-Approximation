from genetic_algorithm.population import *
from genetic_algorithm.ga_operations import *
from genetic_algorithm.algorithm import *
import numpy as np
import matplotlib.pyplot as plt
MAX_SIZE = 1
MAX_DEPTH = 20
FUNCTIONS = {1: ['sin','cos','e','ln','tg','tanh','abs'], 2:['+', '-', '*', '/']}
TERMINAL_SET = ['x'+str(i) for i in range(MAX_SIZE)]
DEPTH = 4

#size=200, num_selected, func_set, terminal_set, depth
def f(x):
    return np.sin(x) * x / 2

X = [[x] for x in np.arange(0, 10, 0.01)]
y = [[f(x[0])] for x in X]

pop = Population(4000, 20, FUNCTIONS, TERMINAL_SET, 6, MAX_DEPTH)
alg = Algorithm(pop, 4000, X, y, epoch_feedback=100)
best = alg.train()
print(best.gen)
y_pred = [[best.evaluate_arg(x)] for x in X]

plt.plot(X, y, color='b', dashes=[6, 2])
plt.plot(X, y_pred, color='r', dashes=[6, 3])
plt.show()

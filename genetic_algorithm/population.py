import random
from genetic_algorithm.chromosome import *
class Population:
    """
    Class for representing a population of chromosomes
    """

    def __init__(self, size, num_selected, func_set, terminal_set, depth, max_depth):
        """
        Constructor for population class
        @param: size - number of members in the population
        @param: func_set - set of functions for the population
        @param: terminal_set - set of terminals for the population
        @param: num_selected - number of chromosomes selected from the population
        @param: depth - initial depth of a tree
        @param: max_depth - maximum depth of a tree
        """
        self.size = size
        self.num_selected = num_selected
        self.list = self.create_population(self.size, func_set, terminal_set, depth)
        self.max_depth = max_depth

    def create_population(self, number, func_set, terminal_set, depth):
        pop_list = []
        for i in range(number):
            if random.random() > 0.5:
                pop_list.append(Chromosome(terminal_set, func_set, depth, 'grow'))
            else:
                pop_list.append(Chromosome(terminal_set, func_set, depth, 'full'))
        return pop_list

from genetic_algorithm.ga_operations import *

class Algorithm:
    """
    Class representing the algorithm
    """
    def __init__(self, population, iterations, inputs, outputs, epoch_feedback = 500):
        """
        Constructor for Alrogithm class
        @param: population - population for the current algorithm
        @param: iterations - number of iterations for the algorithm
        @param: inputs - inputs
        @param: outputs - outputs
        @param: epoch_feedback - number of epochs to show feedback
        """
        self.population = population
        self.iterations = iterations
        self.inputs = inputs
        self.outputs = outputs
        self.epoch_feedback = epoch_feedback
    
    def __one_step(self):
        """
        Function to do one step of the algorithm 
        """
        mother = selection(self.population, self.population.num_selected)
        father = selection(self.population, self.population.num_selected)
        #mother = roulette_selecion(self.population)
        #father = roulette_selecion(self.population)
        child = cross_over(mother, father, self.population.max_depth)
        child = mutate(child)
        child.calculate_fitness(self.inputs, self.outputs)
        self.population = replace_worst(self.population, child)

    def train(self):
        for i in range(len(self.population.list)):
            self.population.list[i].calculate_fitness(self.inputs, self.outputs)
        for i in range(self.iterations):
            if i % self.epoch_feedback == 0:
                best_so_far = get_best(self.population)
                print("Best function: {0}".format(best_so_far.gen))
                print("Best fitness: {0}".format(best_so_far.fitness))
            self.__one_step()
        return get_best(self.population)

        
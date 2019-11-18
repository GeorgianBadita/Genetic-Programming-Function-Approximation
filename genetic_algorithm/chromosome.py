import random
import math
import numpy as np


class Chromosome:
    """
    Class for representing a chromosome
    """
    def __init__(self, terminal_set, funct_set, depth, method='full'):
        """
        Constructor for Chromosome class
        @param: depth - tree depth
        @param: method - method to generate the tree, dfault is full
        @param: terminal_set - set of terminals
        @param: funct_set - set of functions
        """
        self.depth = depth
        self.gen = []
        self.terminal_set = terminal_set
        self.func_set = funct_set
        self.fitness = None
        if method == 'grow':
            self.grow()
        else:
            self.full()

    def full(self, level = 0):
        """
        Function to generate a tree in a full manner
        Every node will have exactly two children
        return: None
        """
        if level == self.depth:
            self.gen.append(random.choice(self.terminal_set))
        else:
            val = random.choice(self.func_set[1] + self.func_set[2])
            if val in self.func_set[2]:
                self.gen.append(random.choice(self.func_set[2]))
                self.full(level + 1)
                self.full(level + 1)
            else:
                self.gen.append(random.choice(self.func_set[1]))
                self.full(level + 1)
        
    def grow(self, level = 0):
        """
        Function to generate a tree in a grow manner
        Every node may be a terminal or a function
        @return: None
        """
        if level == self.depth:
            self.gen.append(random.choice(self.terminal_set))
        else:
            if random.random() > 0.3:
                val = random.choice(self.func_set[2] + self.func_set[1])
                if val in self.func_set[2]:
                    self.gen.append(val)
                    self.grow(level + 1)
                    self.grow(level + 1)
                else:
                    self.gen.append(val)
                    self.grow(level + 1)
            else:
                val = random.choice(self.terminal_set)
                self.gen.append(val)
        
    def evaluate(self, input, poz = 0):
        """
        Function to evaluate the current chromosome with a given input
        @param: input - function input (x0, x1... xn)
        @poz: current_position in genotype
        @return: 
        """
        if self.gen[poz] in self.terminal_set:
            return input[int(self.gen[poz][1:])], poz
        elif self.gen[poz] in self.func_set[2]:
            poz_op = poz
            left, poz = self.evaluate(input, poz + 1)
            right, poz = self.evaluate(input, poz + 1)
            if self.gen[poz_op] == '+':
                return left + right, poz
            elif self.gen[poz_op] == '-':
                return left - right, poz
            elif self.gen[poz_op] == '*':
                return left * right, poz
            elif self.gen[poz_op] == '^':
                return left ** right, poz
            elif self.gen[poz_op] == '/':
                return left / right, poz
        else:
            poz_op = poz
            left, poz = self.evaluate(input, poz + 1)
            if self.gen[poz_op] == 'sin':
                return np.sin(left), poz
            elif self.gen[poz_op] == 'cos':
                return np.cos(left), poz
            elif self.gen[poz_op] == 'ln':
                return np.log(left), poz
            elif self.gen[poz_op] == 'sqrt':
                return math.sqrt(left), poz

    def evaluate_arg(self, input):
        """
        Function to evaluate the current genotype to a given input
        @return: the value of self.gen evaluated at the given input
        """
        return self.evaluate[0]

    def calculate_fitness(self, inputs, outputs):
        """
        Function to claculate the fitness of a chromosome
        @param inputs: inputs of the function we want to predict
        @param outputs: outputs of the function we want to predict
        @return: the chromosome's fitness (calculated based on MSE)
        """
        diff = 0
        for i in range(len(inputs)):
            diff += (self.evaluate(input)[0] - outputs[i][0])**2
        
        if len(inputs) == 0:
            return 1e9
        self.fitness = diff/(len(inputs))
        return self.fitness
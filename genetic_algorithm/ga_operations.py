import numpy as np
import random
from genetic_algorithm.chromosome import *

def traversal(poz, chromosome):
    """
    Function to traverse the tree from the given poz
    @param: poz - start position
    @chromosome: chromosome to be traversed
    """
    if chromosome.gen[poz] in chromosome.terminal_set:
        return poz + 1
    elif chromosome.gen[poz] in chromosome.func_set[1]:
        return traversal(poz + 1, chromosome)
    else:
        new_poz = traversal(poz + 1, chromosome)
        return traversal(new_poz, chromosome)

def mutate(chromosome):
    """
    Function to mutate a chromosome
    @param: chromsome - chromosome to be mutated
    @return: the mutated chromosome
    """
    poz = np.random.randint(len(chromosome.gen))
    if chromosome.gen[poz] in chromosome.func_set[1] + chromosome.func_set[2]:
        if chromosome.gen[poz] in chromosome.func_set[1]:
            chromosome.gen[poz] = random.choice(chromosome.func_set[1])
        else:
            chromosome.gen[poz] = random.choice(chromosome.func_set[2])
    else:
        chromosome.gen[poz] = random.choice(chromosome.terminal_set)
    return chromosome

def selection(population, num_sel):
    """
    Function to select a member of the population for crossing over
    @param: population - population of chromosomes
    @param: num_sel - number of chromosome selected from the population
    @return: the selected chromosome
    """
    sample = random.sample(population.list, num_sel)
    best = sample[0]
    for i in range(1, len(sample)):
        if population.list[i].fitness < best.fitness:
            best = population.list[i]
    
    return best

def cross_over(mother, father, max_depth):
    """
    Function to cross over two chromosomes in order to obtain a child
    @param mother: - chromosome
    @param father: - chromosome
    @param max_depth - maximum_depth of a tree
    """
    child = Chromosome(mother.terminal_set, mother.func_set, mother.depth, None)
    start_m = np.random.randint(len(mother.gen))
    start_f = np.random.randint(len(father.gen))
    end_m = traversal(start_m, mother)
    end_f = traversal(start_f, father)
    child.gen = mother.gen[:start_m] + father.gen[start_f : end_f] + mother.gen[end_m :]
    if child.get_depth() > max_depth and random.random() > 0.2:
        child = Chromosome(mother.terminal_set, mother.func_set, mother.depth)
    return child


def get_best(population):
    """
    Function to get the best chromosome from the population
    @param: population to get the best chromosome from
    @return: best chromosome from population
    """
    best = population.list[0]
    for i in range(1, len(population.list)):
        if population.list[i].fitness < best.fitness:
            best = population.list[i]
    
    return best

def get_worst(population):
    """
    Function to get the worst chromosome of the population
    @param: population - 
    @return: worst chromosome from the population
    """
    worst = population.list[0]
    for i in range(1, len(population.list)):
        if population.list[i].fitness > worst.fitness:
            worst = population.list[i]
    
    return worst

def replace_worst(population, chromosome):
    """
    Function to change the worst chromosome of the population with a new one
    @param: population - population 
    @param: chromosome - chromosome to be added
    """
    worst = get_worst(population)
    if chromosome.fitness < worst.fitness:
        for i in range(len(population.list)):
            if population.list[i].fitness == worst.fitness:
                population.list[i] = chromosome
                break
    return population

def roulette_selecion(population):
    """
    Function to select a member of the population usingq roulette selection
    @param: population - population to be selected from
    """
    fitness = [chrom.fitness for chrom in population.list]
    order = [x for x in range(len(fitness))]
    order = sorted(order, key=lambda x: fitness[x])
    fs = [fitness[order[i]] for i in range(len(fitness))]
    sum_fs = sum(fs)
    max_fs = max(fs)
    min_fs = min(fs)
    p = random.random()*sum_fs
    t = max_fs + min_fs
    choosen = order[0]
    for i in range(len(fitness)):
        p -= (t - fitness[order[i]])
        if p < 0:
            choosen = order[i]
            break
    return population.list[choosen]

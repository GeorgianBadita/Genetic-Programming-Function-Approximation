from genetic_algorithm.chromosome import *

MAX_SIZE = 30
FUNCTIONS = {1: ['sin', 'cos', 'tg', 'ctg', 'ln', 'sqrt'], 2:['+', '-', '*', '/', '^']}
TERMINAL_SET = ['x'+str(i) for i in range(MAX_SIZE)]
DEPTH = 2

chrom = Chromosome(TERMINAL_SET, FUNCTIONS, DEPTH, method='grow')
chrom.gen = ['sqrt', 'x0']
print(chrom.gen)
print(TERMINAL_SET)
print(chrom.evaluate([2]))
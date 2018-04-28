# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 22:03:06 2018

@author: shifuddin
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:20:40 2018

@author: shifuddin
"""
from random import choice, uniform, shuffle, randint
import math

def initialize_total_population(total_population_size):
    
    total_population = []
    total_population_exec_time = []
    
    
    for i in range(1, (total_population_size+1)):
        total_population.append('N'+str(i))
        total_population_exec_time.append(uniform(0,10))
        
    return total_population, total_population_exec_time


def create_initial_population(total_population, initial_population_size, chromosome_size):
    initial_population = []
    
    for _ in range(initial_population_size):
        chromosome = []
        number_list = list(range(0,total_pop_size))        
        for _ in range(chromosome_size):
            shuffle(number_list)
            dna = number_list.pop(len(number_list)-1)
            chromosome.append(total_population[dna])
        
        initial_population.append(chromosome)

    return initial_population

def calculate_pool_occurance(chromose_fitness, total_population_fitness):
    occurance = 0
    if total_population_fitness > 0:
        ratio = chromose_fitness / total_population_fitness
        occurance = math.ceil((ratio*100))
    return occurance

def calculate_chromose_fitness(chromosome, target_value, total_pupolation, total_population_exec_time):
    score = 0
    for dna in chromosome:
        dna_index = total_pupolation.index(dna)
        dna_exec_time = total_population_exec_time[dna_index]
        
        if dna_exec_time <= target_value:
            score += 1
    return score

def calculate_population_fitness(init_population, target_value, total_pupolation, total_population_exec_time):
    population_fitness = []
    for chromose in init_population:
        chromosome_fitness = calculate_chromose_fitness(chromose, target_value, total_pupolation, total_population_exec_time)
        population_fitness.append(chromosome_fitness)
    return population_fitness

def calculate_fitness_mating_pool(target_value, init_population, total_pupolation, total_population_exec_time):
    
    population_fitness = calculate_population_fitness(init_population, target_value, total_pupolation, total_population_exec_time)
        
    mating_pool = []    
    
    for i in range(len(population_fitness)):
        chr_occurance = calculate_pool_occurance(population_fitness[i], sum(population_fitness))
        
        for _ in range (1, chr_occurance+1):
            mating_pool.append(i)
            
            
    return mating_pool, population_fitness

def perform_crossover(chromosome_1, chromose_2):
    mid_point = randint(1, len(chromosome_1))
    child = chromosome_1[0:mid_point] + chromose_2[mid_point:] 
    
    return child


def change_dna(child, total_pupolation):
    while True:
        random_dna = choice(total_pupolation)
        if random_dna not in child:
            break
    return random_dna
    
    
def perform_mutation (child, total_pupolation, mutation_factor):
    
    for i in range(len(child)):
        RU = uniform(0,1)
        
        if (RU < mutation_factor):
            new_dna = change_dna(child, total_pupolation)
            child [i] = new_dna
    
    return child
        

'''
Initialization
'''    
target_value = 1
total_pop_size = 20
current_generation = 0
highest_generation = 40
mutation_factor = 0.02
generation_log = []

'''
Total population and Execution time creation 
Will be replaced by actual value
'''
total_pupolation, total_population_exec_time = initialize_total_population(total_pop_size)

'''
Start of the algorithm
Step 1: Create initial population
'''
initial_population = create_initial_population(total_pupolation, 4, 3)
current_population = initial_population

'''
Continue the algorithm until current generation reaches highest generation
'''
while current_generation < highest_generation:
    
    '''
    Create mating pool
    Mating pool contains chrosomes according to their fitness value
    if one chrosome has fitness 3 and fitness of all chromosoe of current generation is 10
    In mating pool, that chromosome happens (3/10) * 100 times.
    So when we pop one chromosome for selection from the mating pool, the chromosoe which
    has more fitness has higher probability to be considered.
    '''
    mating_pool, population_fitness = calculate_fitness_mating_pool(target_value, current_population, 
                                            total_pupolation, total_population_exec_time)

    print ('Generation: ' + str(current_generation))
    
    generation_log.append(current_population + [population_fitness])
    
    '''
    Initialize new generation
    '''
    new_population = []
    
    for _ in range(len(current_population)):
        
        '''
        Select two chromose from mating pool
        '''
        best_chr_1 = current_population[ choice(mating_pool)]
        best_chr_2 = current_population[ choice(mating_pool)]
    
        '''
        Perform crossover between two chromosome.
        '''
        old_child = perform_crossover(best_chr_1, best_chr_2) 
        
        '''
        Perform mutation on the child
        '''
        mutated_child = perform_mutation(old_child, total_pupolation, mutation_factor)
        
        '''
        Add the child to new generation
        '''
        new_population.append(mutated_child)
        
    current_population = new_population
    current_generation +=1
    
    '''
    Decrease mutation factor in each generation 
    Adaptive mutation is applied so that as we get
    '''
    mutation_factor -= 0.00005

for generation in generation_log:
    print (generation)
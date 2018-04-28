# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 10:55:29 2018

@author: shifuddin
"""

import math
from string import ascii_lowercase, whitespace
from random import choice, randint, uniform

def calculate_fitness_mating_pool(population):
    '''
    Calculate fitness
    '''
    fitness = []

    for element in population:
        score = 0
        for i in range(len(element)):
            if element[i] == target_list[i]:
                score += 1
        fitness.append(score)
                 
    sum_value = sum(fitness)
    pool = []
    for i in range (len(fitness)):
        
        times = fitness[i] / sum_value
        total_times = times * 100
        
        for j in range(1, math.ceil(total_times) +1):
            pool.append(i)
            
    return fitness, pool

def create_new_child(pool, population):
    '''
    Perform crossover
    '''
    parenta = choice(pool)
    parentb = choice(pool)

    mid = randint(0,len(population[parenta]))
    child = population[parenta][0:mid] + population[parentb][mid:] 
    
    '''
    Perform mutation
    '''
    mutation_rate = 0.01
    for i in range(len(child)):
    
        mut = uniform(0,1) 
        if mut < mutation_rate:
            child[i] = choice(ascii_lowercase)
        
    return child


def initialize_population(size_population):
    population = []
    for i in range (size_population):
        dna = ''.join(choice(ascii_lowercase + whitespace) for _ in range(len(target_list)))
        population.append(list(dna))
    
    return population
'''
Create Target
'''    
target = "hello world"
target_list = list(target)

'''
Step 1 initialization
'''
population = initialize_population(100)

generation = 0
while True:
    '''
    Step 2 create fitness and mating pool
    '''
    generation += 1
    fitness, pool = calculate_fitness_mating_pool(population)
    print (generation)
    optimum = False
    best_fit = ''
    for i in range(len(fitness)):
        if fitness[i] == 11:
            optimum = True
            best_fit = population[i]
            break
    if optimum == True:
        print (best_fit)
        break

    '''
    Step 3 reproduction
    '''
    new_population = []
    for i in range (len(population)):
        child = create_new_child(pool, population)
        new_population.append(child)
    print (new_population)
    
    population = new_population
